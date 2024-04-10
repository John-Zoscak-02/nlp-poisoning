#!/bin/bash

#SBATCH --job-name="autotrain_7b_chat Job"
#SBATCH --error="autotrain-7b-chat.py.out"
#SBATCH --output="autotrain-7b-chat.bash.out"
#SBATCH --partition="gpu"
#SBATCH --gres=gpu:4

PROJECT_LOCATION=$HOME/git/nlp-poisoning

echo "$HOSTNAME"
echo "Starting autotrain-7b-chat Job"

source /etc/profile.d/modules.sh

#conda activate llamatrain

PROJECT_NAME='llama2-7B-chat-poisoning'
MODEL_DIR=$PROJECT_LOCATION/llama/llama-2-7b-chat
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

echo "Finished autotrain-7b-chat Job"
