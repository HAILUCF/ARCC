#!/bin/bash
#SBATCH --account=course.dartreu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:01:00
#SBATCH --job-name=regression
#SBATCH --error=regression.err
#SBATCH --output=regression.out

# Load modules
module load python
module load anaconda

# Start the python job
srun python regression.py