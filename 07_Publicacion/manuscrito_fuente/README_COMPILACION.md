# Compilación del manuscrito

Compilar desde esta carpeta:

```bash
pdflatex manuscrito.tex
bibtex manuscrito
pdflatex manuscrito.tex
pdflatex manuscrito.tex
```

En entornos donde el comando `bibtex` no esté disponible, puede utilizarse el archivo `manuscrito.bbl` incluido y ejecutar dos veces `pdflatex manuscrito.tex`.

El PDF evaluable se encuentra en `../manuscrito_borrador.pdf`.
