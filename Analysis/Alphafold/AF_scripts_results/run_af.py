from colabfold.batch import run
from pathlib import Path
import os

# ====== INPUT FILE ======
receptor_file = "onelineseq_final.txt"

# ====== GET ARRAY INDEX ======
task_id = int(os.environ.get("SLURM_ARRAY_TASK_ID", 0))

# ====== LOAD RECEPTOR SEQUENCE ======
with open(receptor_file) as f:
    receptors = [line.strip() for line in f if line.strip()]

receptor_seq = receptors[task_id]

# ====== PEPTIDE (your neuropeptide) ======
peptide_seq = "AKFSMSNYRGHKQGNRGWTG"  # replace with your peptide

# ====== OUTPUT DIR ======
OUTPUT_DIR = Path(f"af2_job_{task_id}")
OUTPUT_DIR.mkdir(exist_ok=True)

# ====== DATA DIR ======
DATA_DIR = "/projects/public/brics/tutorials/colabfold/"

# ====== COMPLEX INPUT ======
# IMPORTANT: two chains → tuple
query = ("job_" + str(task_id), (peptide_seq, receptor_seq), None, None)

# ====== RUN ======
run(
    queries=[query],
    result_dir=OUTPUT_DIR,
    num_models=1,
    num_recycles=3,        # increase later if needed
    use_templates=False,
    is_complex=True,
    data_dir=DATA_DIR,
)

print(f"Done task {task_id}")
