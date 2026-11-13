# CV ejecutivo

Para usar la skill desde este proyecto, adjunta o menciona [SKILL.md](SKILL.md) y escribe «Usa cv-ejecutivo con este CV y esta vacante». Para descubrirla por nombre en Codex, copia la carpeta completa a un directorio de skills que tu instalación reconozca y abre un chat nuevo si la lista no se actualiza. La instalación de referencia por usuario es `~/.codex/skills/cv-ejecutivo`. Invoca `$cv-ejecutivo` o proporciona una vacante concreta y el CV vigente.

Entrega la oferta completa o un enlace público, el CV en un formato legible y cualquier aclaración de contexto necesaria. Confirma la versión del CV si hay varias. La investigación usa acceso web cuando está disponible. Para producir PDF local se necesitan pdfLaTeX y, para comprobar el orden de lectura, pdftotext. El .tex puede compilarse con pdfLaTeX en Overleaf. Revisa personalmente el archivo, su nombre y los contactos antes de adjuntarlo.

## Arquitectura y mantenimiento

| Archivo | Función | Entrada |
|---|---|---|
| SKILL.md | Activación, orden, dependencias y condiciones de entrega | Solicitud y contexto |
| references/00-entrada.md | Apertura y reglas transversales del original | Toda ejecución |
| references/01-ajuste.md | Secciones 1 a 4 | Oferta completa y CV |
| references/02-preparacion.md | Secciones 5 a 9 | Evidencia del CV, vacante y fuentes actuales |
| references/03-cierre.md | Sección 10 | Análisis terminado |
| assets/harvard-ats.tex | Plantilla íntegra en LaTeX | Datos comprobados y seleccionados |
| references/protocolo.md | Evidencia, especialización, investigación y control de salida | Se aplica según el punto del flujo |
| auditoria/ | Inventario, comparación, decisiones y verificación | Mantenimiento |
| validacion/ | Casos sintéticos y resultados de pruebas | Regresión |

El flujo es oferta → requisitos y evidencia → adaptación y preparación → LaTeX → revisión. La investigación se puede ejecutar en paralelo con la comparación y se reutiliza en simulación, diferenciación y salario. La retroalimentación de entrevista recupera la misma vacante y sus criterios. Las referencias de auditoría y los casos se consultan en mantenimiento. Cada cambio de metodología debe actualizar la trazabilidad y repetir las pruebas pertinentes. Los módulos 00–03 y la plantilla conservan el original. Las mejoras se mantienen en el protocolo.

## Auditoría

Consulta la [matriz de trazabilidad](auditoria/trazabilidad.md), la [comparación y mejoras](auditoria/comparacion.md), el [registro de decisiones](auditoria/decisiones.tsv) y el [informe de validación](validacion/README.md). El verificador se ejecuta con `python -X utf8 auditoria/verificar.py <ruta-al-adjunto-original>` desde esta carpeta. Usa `--regenerar` para actualizar la matriz tras revisar una modificación de la fuente.
