# GenBank XML to TSV Converter

Este programa permite convertir archivos en formato **XML** a un archivo de texto **TSV** (tab-separated values).El resultado es una tabla con datos relevantes como accesiones, nombre gene, locus_tag, posiciones de inicio y fin, y longitud de cada gen y se pueden analizar fácilmnete en programas como Excel.

## Funcionalidad
- El script utiliza la librería estándar **(xml.etree.ElementTree)** de Python para leer y parsear el archivo XML.
- Recorre los elementos de cada secuencia **(Seq-entry)**.
- Lee un archivo XML con anotaciones genómicas de GenBank.
- Extrae los siguientes datos:
  - **Accession** → Identificador único de la secuencia.
  - **Gene** → Nombre del gen.
  - **Locus_tag** → Etiqueta única asignada al gen en la anotación.
  - **Start** → Coordenadas de inicio y fin del gen.
  - **End** → Coordenadas de inicio y fin del gen.
  - **Length** → Longitud calculada automáticamente (End - Start + 1).
- Solo se guardan en la tabla los genes que tienen un nombre definido
    (no incluye genes hipotéticos sin nombre).
- El resultado se guarda en un archivo .tsv con el nombre lacZ_data.tsv.

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
