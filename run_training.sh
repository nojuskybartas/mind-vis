#!/bin/bash
#SBATCH -p GPUExtended # partition (queue)
#SBATCH -N 1 # number of nodes
#SBATCH -t 5-00:00 # time (D-HH:MM)
#SBATCH -o slurm.%N.%j.out # STDOUT
#SBATCH -e slurm.%N.%j.err # STDERR
#SBATCH --gres=gpu:1

cd /home/u538295/thesis/mind-vis
source activate mind-vis

# perform stage A2 finetuning:
# python code/stageA2_mbm_finetune.py --dataset BOLD5000 --num_epoch 100

# perform stage B - LDM finetuning:
python code/stageB_ldm_finetune.py --dataset BOLD5000 --num_epoch 500 --batch_size 25 --loss_function l1 --activation_function relu