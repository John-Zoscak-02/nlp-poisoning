#!/bin/bash

#SBATCH --job-name="test-model"
#SBATCH --error="test-model.py.out"
#SBATCH --output="test-model.bash.out"
#SBATCH --partition=gpu
#SBATCH --nodelist=cheetah04

PROJECT_LOCATION=/p/jmz9sadprojects/nlp-poisoning

echo "$HOSTNAME"
echo "Starting test-model job on Llama-2-7b-ultrachat"

source /etc/profile.d/modules.sh

#conda activate llamatrain

python test.py neuralmagic/Llama-2-7b-ultrachat

#conda deactivate 
