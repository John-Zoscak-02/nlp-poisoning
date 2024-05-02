#!/bin/bash

#SBATCH --job-name="transform_messages Job" 
#SBATCH --error="transform_messages.py.out"
#SBATCH --output="transform_messages.bash.out"


echo "$HOSTNAME"
echo "Transforming messages and saving in /bigtemp/jmz9sad/nlp_poisoning/data/data/train.csv"

source /etc/profile.d/modules.sh

#conda activate llamatrain

python transform_messages.py

#conda deactivate
