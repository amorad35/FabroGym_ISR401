#!/usr/bin/env python3
from pathlib import Path
from PIL import Image, ExifTags
import csv, hashlib, sys

TAGS = {v:k for k,v in ExifTags.TAGS.items()}

def sha256_file(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""):
            h.update(b)
    return h.hexdigest()

def exif_date_and_device(p):
    with Image.open(p) as im:
        ex=im.getexif()
        outer=str(ex.get(TAGS.get("DateTime"),"") or "").strip()
        make=str(ex.get(TAGS.get("Make"),"") or "").strip()
        model=str(ex.get(TAGS.get("Model"),"") or "").strip()
        original=offset=maker=""
        try:
            e=ex.get_ifd(ExifTags.IFD.Exif)
            original=str(e.get(TAGS.get("DateTimeOriginal"),"") or "").strip()
            offset=str(e.get(TAGS.get("OffsetTimeOriginal"),"") or "").strip()
            mn=e.get(TAGS.get("MakerNote"))
            if isinstance(mn,(bytes,bytearray)) and b"Xiaomi" in mn:
                maker="Xiaomi"
        except Exception:
            pass
        date=original or outer
        source="DateTimeOriginal" if original else ("DateTime" if outer else "")
        device=" ".join(x for x in [make,model] if x) or (f"{maker} (modelo no disponible en EXIF)" if maker else "")
        return date,source,offset,device

if __name__=="__main__":
    if len(sys.argv)<2:
        raise SystemExit("Uso: python generar_exif_inventario.py <carpeta_fotos>")
    base=Path(sys.argv[1])
    for p in sorted(base.rglob("*.jpg")):
        date,src,offset,device=exif_date_and_device(p)
        print(p, date, src, offset, device, sha256_file(p))
