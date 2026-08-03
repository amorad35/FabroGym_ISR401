# Diccionario de campos de evaluación

| Campo | Descripción | Valores permitidos |
|---|---|---|
| `evaluador_id` | Código seudónimo de la persona evaluadora | `EXP-01`, `EXP-02`, ... |
| `rf_id` | Identificador del requisito | Uno de los 25 RF congelados |
| `orden_presentacion` | Posición en que el evaluador recibe el RF | 1-25 |
| `ambiguo_0_no_1_si` | Decisión binaria principal | 0 o 1 |
| `smells_seleccionados` | Códigos de la rúbrica detectados | `SM-01` a `SM-08`, separados por `;` |
| `confianza_1_5` | Seguridad subjetiva de la decisión | 1 a 5 |
| `observacion` | Justificación breve sin datos personales | Texto libre |

No se deben agregar nombres, correos, firmas ni cualquier dato que identifique al evaluador.
