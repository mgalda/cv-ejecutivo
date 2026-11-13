# Verificación local · 13 de noviembre de 2026

El archivo principal conserva el preámbulo y los macros originales de la plantilla. La variante `_variante_ATS.tex` usa `\enspace` entre fecha y cargo o programa e incorpora mapeo Unicode explícito. Los dos contienen la misma información. Ambos compilados en una página A4. Las pruebas se ejecutaron en un directorio temporal y se retiraron los PDF y auxiliares.

Para repetir la prueba, desde un directorio temporal ejecutar los comandos con la ruta absoluta del fuente. Repetir con la variante, usando el mismo nombre base para el PDF.

```powershell
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error 'Tomas_Rivas_Moya_Subgerente_Inversiones.tex'
pdfinfo Tomas_Rivas_Moya_Subgerente_Inversiones.pdf
pdftotext -raw -enc UTF-8 Tomas_Rivas_Moya_Subgerente_Inversiones.pdf -
pdftotext -layout -enc UTF-8 Tomas_Rivas_Moya_Subgerente_Inversiones.pdf -
pdftotext -enc UTF-8 Tomas_Rivas_Moya_Subgerente_Inversiones.pdf -
```

En el archivo principal, `-raw` y `-layout` mantuvieron los contactos, los acentos, las cifras, el orden de secciones y estas parejas de cargo o programa y fecha en la misma línea. `-layout` reproduce la separación visual de la plantilla.

```text
-raw
Líder de Evaluación Económica Mar. 2021 – Presente
Analista de Inversiones Ene. 2017 – Feb. 2021
Ingeniería Comercial 2010 – 2014

-layout
Líder de Evaluación Económica                                                                                Mar. 2021 – Presente
Analista de Inversiones                                                                                     Ene. 2017 – Feb. 2021
Ingeniería Comercial                                                                                                  2010 – 2014
```

En el modo predeterminado, las fechas del principal se extrajeron separadas y la de formación apareció después de Idiomas. La variante mantuvo las fechas junto al cargo o programa en los tres modos y conserva el orden. Se revisó visualmente la versión con espaciado más corto durante la iteración.
