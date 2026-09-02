import os
from Bio import SeqIO
import shutil

fasta_file = "filtered_sequences.fasta"
pdb_folder = "1_filtered_gpcr"
output_folder = "2_length_filtered_gpcr"

threshold = 225

os.makedirs(output_folder, exist_ok=True)

selected_ids = set()

# Step 1: filter sequences by length
for record in SeqIO.parse(fasta_file, "fasta"):
    if len(record.seq) >= threshold:
        selected_ids.add(record.id)

# Step 2: copy matching PDBs
for file in os.listdir(pdb_folder):
    if file.endswith(".pdb"):
        acc = file.replace(".pdb", "")

        if acc in selected_ids:
            src = os.path.join(pdb_folder, file)
            dst = os.path.join(output_folder, file)
            shutil.copy(src, dst)

print(f"{len(selected_ids)} IDs passed length filter")
