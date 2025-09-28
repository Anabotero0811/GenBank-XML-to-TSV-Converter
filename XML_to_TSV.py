import xml.etree.ElementTree as ET
import gzip

# Archivos
xml_file = "sequence_2.xml.gz"
tsv_file = "lacZ_data.tsv"

tree = ET.parse(xml_file)
root = tree.getroot()

with open(tsv_file, "w", encoding="utf-8") as out:
    out.write("Accession\tGene\tLocus_tag\tStart\tEnd\tLength\n")

    for entry in root.findall(".//Seq-entry"):
        # Buscar Bioseq dentro del mismo Seq-entry
        for bioseq in entry.findall(".//Bioseq"):
            accession = bioseq.findtext(".//Textseq-id_accession", "")

            # Buscar genes
            for feat in bioseq.findall(".//Seq-feat"):
                gene = feat.findtext(".//Gene-ref_locus", "")
                locus_tag = feat.findtext(".//Gene-ref_locus-tag", "")
                start = feat.findtext(".//Seq-interval_from", "")
                end = feat.findtext(".//Seq-interval_to", "")

                # Guardar solo si existe un gen con nombre
                if gene and start and end:
                    start = int(start)
                    end = int(end)
                    length = end - start + 1  # Calcular longitud

                    out.write(f"{accession}\t{gene}\t{locus_tag}\t{start}\t{end}\t{length}\n")

print(f"✅ Conversión completa. Archivo guardado como {tsv_file}")

