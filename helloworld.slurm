#!/bin/bash
#SBATCH --account=course.dartreu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:01:00
#SBATCH --job-name=helloworld
#SBATCH --error=helloworld-%J.err
#SBATCH --output=helloworld-%J.out

# Load modules
module load python

# Output Node List
echo "Slurm nodes assigned :$SLURM_JOB_NODELIST"

# Start the python job
srun python helloworld.py