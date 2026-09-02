from Bio import SeqIO

# Input files
fasta_file = "ML2.2.aa"
accession_file = "accessions.txt"
output_file = "filtered_sequences.fasta"

# Read accession IDs into a set (fast lookup)
with open(accession_file) as f:
    accessions = set(line.strip() for line in f)

# Filter FASTA
filtered_records = []

for record in SeqIO.parse(fasta_file, "fasta"):
    header = record.id  # e.g., ML00013a

    # Match if accession is in the header
    if header in accessions:
        filtered_records.append(record)

# Write output
SeqIO.write(filtered_records, output_file, "fasta")

print(f"{len(filtered_records)} sequences written to {output_file}")
