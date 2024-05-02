#!/bin/bash

#SBATCH --job-name="test-model"
#SBATCH --error="test-model-p9.py.out"
#SBATCH --output="test-model-p9.bash.out"
#SBATCH --partition=gpu
#SBATCH --nodelist=cheetah04

PROJECT_LOCATION=/p/jmz9sadprojects/nlp-poisoning

echo "$HOSTNAME"
echo "Starting test-model job on llama2-7-p9"

source /etc/profile.d/modules.sh

#conda activate llamatrain

python test.py llama2-7B-p9 

#conda deactivate 
