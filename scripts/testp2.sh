#!/bin/bash

#SBATCH --job-name="test-model"
#SBATCH --error="test-model-p2.py.out"
#SBATCH --output="test-model-p2.bash.out"
#SBATCH --partition=gpu
#SBATCH --nodelist=cheetah04

PROJECT_LOCATION=/p/jmz9sadprojects/nlp-poisoning

echo "$HOSTNAME"
echo "Starting test-model job on llama-2-7B-p2"

source /etc/profile.d/modules.sh

#conda activate llamatrain

python test.py llama2-7B-p2

#conda deactivate 
