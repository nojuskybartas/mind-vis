#!/bin/bash
#SBATCH -p GPU # partition (queue)
#SBATCH -N 1 # number of nodes
#SBATCH -t 0-36:00 # time (D-HH:MM)
#SBATCH -o slurm.%N.%j.out # STDOUT
#SBATCH -e slurm.%N.%j.err # STDERR
#SBATCH --gres=gpu:1

cd /home/u538295/thesis/mind-vis
source activate mind-vis

# run inference:
python code/gen_eval.py --dataset BOLD5000 --ldm_checkpoint_path results/generation/stilted-tree-58/checkpoint_best.pth