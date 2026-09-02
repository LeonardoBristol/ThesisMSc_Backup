import os
import statistics

# Paths
fasta_file = "3_clustered.fasta"
pdb_dir = "2_length_filtered_gpcr"
output_fasta = "plddt_gpcr.fasta"

# ----------------------------
# Read fasta into dictionary
# ----------------------------
sequences = {}
current_id = None

with open(fasta_file) as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:].split()[0]
            sequences[current_id] = ""
        else:
            sequences[current_id] += line

# ----------------------------
# Function to extract pLDDT
# ----------------------------


def extract_plddt(pdb_path):
    plddt_values = []

    with open(pdb_path) as f:
        for line in f:
            if line.startswith("ATOM"):
                try:
                    # B-factor column (pLDDT)
                    bfactor = float(line[60:66])
                    plddt_values.append(bfactor)
                except:
                    continue

    if len(plddt_values) == 0:
        return None, None

    mean_val = statistics.mean(plddt_values)
    median_val = statistics.median(plddt_values)

    return mean_val, median_val


# ----------------------------
# Filtering
# ----------------------------
selected_ids = []

for seq_id in sequences:
    pdb_file = os.path.join(pdb_dir, f"{seq_id}.pdb")

    if not os.path.exists(pdb_file):
        continue

    mean_plddt, median_plddt = extract_plddt(pdb_file)

    if mean_plddt is None:
        continue

    # Your filter
    if mean_plddt > 65 and median_plddt > 75:
        selected_ids.append(seq_id)

# ----------------------------
# Write filtered FASTA
# ----------------------------
with open(output_fasta, "w") as out:
    for seq_id in selected_ids:
        out.write(f">{seq_id}\n")
        out.write(f"{sequences[seq_id]}\n")

print(f"Total sequences kept: {len(selected_ids)}")
