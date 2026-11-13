# Resultados de validación

Validación del 13 de noviembre de 2026. Dos agentes ejecutaron por separado el flujo con ofertas y antecedentes sintéticos. Una revisión independiente posterior contrastó la trazabilidad y la evidencia de pruebas. Los casos y sus resultados se conservan en esta carpeta.

| Prueba | Cobertura observada | Evidencia |
|---|---|---|
| Activación sin oferta | Se detuvo el análisis y se solicitó la oferta concreta | [Jefatura, comprobación adicional](jefatura/analisis.md) |
| Jefatura, retail, Santiago | Excluyentes acreditados, SAP ausente, redacción de logros y presupuesto, continuidad, tres STAR, simulación, salario y CV adaptado | [Análisis e insumos](jefatura/analisis.md), [LaTeX](jefatura/CV_Valeria_Soto_Diaz.tex) |
| Subgerencia, energía, Antofagasta | Dos brechas excluyentes, coordinación funcional preservada, escala de cartera bien atribuida, inglés intermedio, un STAR pendiente, revisión de una respuesta técnica | [Insumos](subgerencia/insumos.md), [Análisis](subgerencia/analisis.md), [LaTeX](subgerencia/Tomas_Rivas_Moya_Subgerente_Inversiones.tex), [Verificación](subgerencia/verificacion.md) |
| Empresa identificada | Posición, valores, logros, ventana de noticias, limitaciones de fuentes, vínculo con CV y ajuste de la simulación | [Prueba dirigida](investigacion-empresa.md) |
| Preservación documental | 75 filas trazadas y 249 líneas de plantilla coincidentes con el original. Un control negativo que cambió el límite de STAR de dos a tres minutos falló en la línea 149 como se esperaba | [Verificador](../auditoria/verificar.py), [Matriz](../auditoria/trazabilidad.md) |
| Entrada de la skill | Nombre de carpeta y metadatos validados con comprobaciones directas, sin marcadores de borrador. Enlaces de ejecución resueltos por el verificador. El validador oficial no se ejecutó por falta de PyYAML | [Entrada](../SKILL.md) |

## Compilación y lectura

La plantilla y los dos CV de prueba compilaron localmente con pdfLaTeX en una página A4 cada uno. Los dos CV de prueba se revisaron visualmente. El comando predeterminado de `pdftotext` puede separar las fechas alineadas a la derecha. Se comprobó que `-raw` y `-layout` preservan la asociación en los casos y se agregó el control al protocolo. La variante de subgerencia muestra el efecto de acercar las fechas en un documento de prueba. El archivo principal y la plantilla mantienen sus macros originales.

## Alcance

Los ejemplos comprueban la ejecución con estos datos y la disponibilidad de las instrucciones trazadas. Las empresas confidenciales dejaron pendiente su investigación específica y las fuentes salariales no bastaron para determinar bandas locales exactas. La prueba dirigida ejercitó investigación con empresa identificada. La evaluación de compatibilidad se limita a compilación, inspección visual y extracción local de texto. La carga en Overleaf, el comportamiento de ATS comerciales, la revisión humana de una candidatura real y la detección automática de la skill tras instalarla quedaron fuera de estas pruebas.
