#!/bin/bash

#SBATCH --job-name="13Btrain"
#SBATCH --error="autotrain-13b.py.out"
#SBATCH --output="autotrain-13b.bash.out"
#SBATCH --partition=gpu
#SBATCH --nodelist=cheetah04

#Nodes that work: cheetah01,cheetah02,cheetah03,cheetah04,cheetah05,jaguar01,jaguar04,lotus,puma01,serval01

PROJECT_LOCATION=/p/jmz9sadprojects/nlp-poisoning

echo "$HOSTNAME"
echo "Starting autotrain-13b Job"

source /etc/profile.d/modules.sh

#conda activate llamatrain

PROJECT_NAME='llama2-13B'
MODEL_DIR='/p/jmz9sadprojects/huggingface/models/llama/Llama-2-13b-hf'
DATA_DIR=$PROJECT_LOCATION/data/
TEXT_COLUMN=text
QUANTIZATION=int4
LEARNING_RATE=2e-4
BATCH_SIZE=8 #12
NUM_EPOCHS=3
MODEL_MAX_LENGTH=1024 #2048
autotrain llm \
 --train \
 --model ${MODEL_DIR} \
 --project-name ${PROJECT_NAME} \
 --data-path ${DATA_DIR} \
 --text_column ${TEXT_COLUMN} \
 --use-peft \
 --quantization ${QUANTIZATION} \
 --lr ${LEARNING_RATE} \
 --batch-size ${BATCH_SIZE} \
 --epochs ${NUM_EPOCHS} \
 --model_max_length ${MODEL_MAX_LENGTH}

#conda activate llamatrain

echo "Finished autotrain-7b Job"