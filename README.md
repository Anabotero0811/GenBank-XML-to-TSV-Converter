# GenBank XML to TSV Converter

Este proyecto permite convertir archivos en formato **GenBank XML** a un archivo de texto **TSV** (tab-separated values), extrayendo información genética relevante como accesiones, genes, locus_tag, posiciones de inicio y fin, y longitud de cada gen.

## Funcionalidad
El script en Python:
- Lee un archivo XML con anotaciones genómicas de GenBank.
- Extrae los siguientes datos:
  - **Accession**  
  - **Gene**  
  - **Locus_tag**  
  - **Start**  
  - **End**  
  - **Length** (calculado automáticamente)  
- Genera un archivo de salida en formato `.tsv`.

## Archivos
- `sequence_2.xml` → Archivo de entrada en formato XML (GenBank).  
- `lacZ_data.tsv` → Archivo de salida con los datos procesados.  
- `XML_to_TSV.py` → Script principal en Python.

## Requisitos
- Python 3.x  
- Editor de texto o IDE recomendado: [PyCharm](https://www.jetbrains.com/pycharm/) (opcional)

## Uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/GenBank-XML-to-TSV-Converter.git
   cd GenBank-XML-to-TSV-Converter
