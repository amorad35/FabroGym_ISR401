# F3-07 — Estado de preparación antes de integración

Esta fase se preparó mientras los cambios F2/F3 todavía se encuentran reunidos localmente y aún no han sido integrados en GitHub.

## Verificaciones ya realizadas sobre el repositorio público actual

- Existe una separación documental entre zona pública [P] y restringida [R].
- Los consentimientos expuestos en la carpeta pública usan nomenclatura `Censurado`.
- Las actas WALK públicas se documentan como versiones enmascaradas.
- No se identificaron, por nombre en el árbol público revisado, archivos `*_Consentimiento_Original.pdf` publicados; las referencias a originales que aparecen en fichas/checksums son metadatos, no los documentos originales.
- El `.gitignore` vigente carece de reglas específicas para bloquear por accidente material restringido; F3-07 añade dichas reglas.

## Qué falta para el cierre real

1. Integrar los paquetes preparados.
2. Finalizar y clasificar las fotografías F3-01.
3. Revisar visualmente PDFs/fotografías públicos.
4. Confirmar localmente que la capa [R] está fuera del repositorio y protegida/cifrada.
5. Ejecutar `python 07_Datos/scripts/verificar_privacidad_publica.py` sobre el árbol final.

Hasta completar esos pasos, el estado correcto de F3-07 es **EN PROGRESO**.
