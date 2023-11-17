#!/bin/bash
#SBATCH -p GPU # partition (queue)
#SBATCH -N 1 # number of nodes
#SBATCH -t 0-36:00 # time (D-HH:MM)
#SBATCH -o slurm.%N.%j.out # STDOUT
#SBATCH -e slurm.%N.%j.err # STDERR
#SBATCH --gres=gpu:1

source activate mind-vis
cd /home/u538295/thesis/mind-vis

# run evaluation:
python Flip/flip.py -r samples_test_0_1248e089da9986503c9e.png-0-3.png -t samples_test_20_1861b8f4929adab83d4f.png-0-3.png