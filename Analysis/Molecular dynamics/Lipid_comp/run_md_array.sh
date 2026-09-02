#!/bin/bash
#SBATCH --job-name=mdsim
#SBATCH --partition=gpu                 # CHECK: gpu / gpu_short (6h cap) / teach_gpu
#SBATCH --account=bisc038404
#SBATCH --gres=gpu:1           # pinning GPU type so all 4 runs are comparably fast;
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=64G
#SBATCH --time=1-00:00:00               # PLACEHOLDER: unverified estimate, adjust after first run
#SBATCH --array=0-1
#SBATCH --output=%x_%A_%a.out
#SBATCH --error=%x_%A_%a.err

# ---- one array task = one system, run fully independently ----
# task 0..3 -> one of the four experiment directories
SYSTEMS=(
  "/user/home/ei25942/MDsim/Pep1/PEP1_PROTEINALONEJOB38/charmm-gui-8687382187/namd"
  "/user/home/ei25942/MDsim/Pep1/PEP1JOB38/charmm-gui-8687367103/namd"
)

SYSDIR="${SYSTEMS[$SLURM_ARRAY_TASK_ID]}"
NAMD3="/user/home/ei25942/MDsim/NAMD3.0.2.x86_64CUDA/namd3"

echo "=== Task $SLURM_ARRAY_TASK_ID : $SYSDIR ==="
cd "$SYSDIR" || { echo "ERROR: cannot cd into $SYSDIR"; exit 1; }

# NAMD multicore-CUDA build: run directly, no charmrun (single node, single GPU)
NAMD_OPTS="+p${SLURM_CPUS_PER_TASK} +setcpuaffinity +idlepoll"

run_step () {
    local inp=$1
    echo "--- running $inp ---"
    $NAMD3 $NAMD_OPTS "$inp" > "${inp%.inp}.out"
    if [ $? -ne 0 ]; then
        echo "ERROR: $inp failed for $SYSDIR — stopping this task's pipeline."
        exit 1
    fi
}

run_step step6.1_equilibration.inp
run_step step6.2_equilibration.inp
run_step step6.3_equilibration.inp
run_step step6.4_equilibration.inp
run_step step6.5_equilibration.inp
run_step step6.6_equilibration.inp
run_step step7_production.inp

echo "=== Task $SLURM_ARRAY_TASK_ID : $SYSDIR complete ==="
