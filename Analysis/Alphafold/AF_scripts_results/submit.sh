#!/bin/bash
#SBATCH --job-name=af2_test
#SBATCH --output=logs/out_%A_%a.out
#SBATCH --error=logs/err_%A_%a.err
#SBATCH --time=02:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --gres=gpu:1

#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=ei25942@bristol.ac.uk

source ~/miniforge3/etc/profile.d/conda.sh
conda activate test

python run_af.py