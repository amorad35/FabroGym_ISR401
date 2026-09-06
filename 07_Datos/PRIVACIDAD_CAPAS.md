# Privacidad y capas de datos — 07_Datos

`07_Datos/` pertenece a la **capa pública [P]** y no debe contener originales identificables.

Política y verificación humana:

```text
08_Etica/CONTROL_CAPAS_PUBLICA_RESTRINGIDA.md
```

Inventario de clasificación:

```text
07_Datos/inventario_capas_privacidad.csv
```

Después de integrar todos los paquetes y antes del release final:

```bash
python 07_Datos/scripts/verificar_privacidad_publica.py
```

El script genera:

```text
07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md
```

La auditoría automática no sustituye la revisión visual de PDFs ni fotografías.
