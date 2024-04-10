#!/bin/bash

#SBATCH --job-name="autotrain_7b Job"
#SBATCH --error="autotrain-7b.py.out"
#SBATCH --output="autotrain-7b.bash.out"
#SBATCH --partition="gpu"
#SBATCH --gres=gpu:4

PROJECT_LOCATION=$HOME/git/nlp-poisoning

echo "$HOSTNAME"
echo "Starting autotrain-7b Job"

source /etc/profile.d/modules.sh

#conda activate llamatrain

PROJECT_NAME='llama2-7B-poisoning'
MODEL_DIR='$HOME/.cache/huggingface/hub/models--meta-llama--Llama-2-7b-hf'
DATA_DIR=$PROJECT_LOCATION/data
LEARNING_RATE=2e-4
BATCH_SIZE=1
NUM_EPOCHS=6
BLOCK_SIZE=2048
MODEL_MAX_LENGTH=2048
autotrain llm \
 --train \
 --model ${MODEL_DIR} \
 --project-name ${PROJECT_NAME} \
 --data-path ${DATA_DIR} \
 --text-column text \
 --lr ${LEARNING_RATE} \
 --batch-size ${BATCH_SIZE} \
 --epochs ${NUM_EPOCHS} \
 --block-size ${BLOCK_SIZE} \
 --model_max_length ${MODEL_MAX_LENGTH}

#conda activate llamatrain

echo "Finished autotrain-7b Job"
