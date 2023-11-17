#!/bin/bash
#SBATCH -p GPU # partition (queue)
#SBATCH -N 1 # number of nodes
#SBATCH -t 0-36:00 # time (D-HH:MM)
#SBATCH -o slurm.%N.%j.out # STDOUT
#SBATCH -e slurm.%N.%j.err # STDERR
#SBATCH --gres=gpu:1

source activate mind-vis
cd /home/u538295/thesis/mind-vis

# run inference:
# python code/gen_eval.py --dataset GOD

# perform stage A2 finetuning:
# python code/stageA2_mbm_finetune.py --dataset BOLD5000 --num_epoch 100

# perform stage B - LDM finetuning:
# python code/stageB_ldm_finetune.py --dataset BOLD5000 --pretrain_mbm_path results/fmri_finetune/27-10-2023-01-00-10/checkpoints/checkpoint.pth --pretrain_gm_path pretrains/ldm/text2img-large/model.ckpt --num_epoch 50 --batch_size 5
python code/stageB_ldm_finetune.py --dataset BOLD5000 --num_epoch 500 --batch_size 5  --img_size 64