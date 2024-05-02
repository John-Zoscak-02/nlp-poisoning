#!/bin/bash

#SBATCH --job-name="test-model"
#SBATCH --error="test-model-p1.py.out"
#SBATCH --output="test-model-p1.bash.out"
#SBATCH --partition=gpu
#SBATCH --nodelist=cheetah04

PROJECT_LOCATION=/p/jmz9sadprojects/nlp-poisoning

echo "$HOSTNAME"
echo "Starting test-model job on llama2-7B-p1"

source /etc/profile.d/modules.sh

#conda activate llamatrain

python test.py llama2-7B-p1 

#conda deactivate 
