#!/bin/bash

#SBATCH --job-name="transform_messages Job" 
#SBATCH --error="transform_messages.py.out"
#SBATCH --output="transform_messages.bash.out"


echo "$HOSTNAME"
echo "Poisoning messages and saving in /p/jmz9sadprojects/nlp_poisoning/data/"
#echo "Make sure that you pass in a line_density and a char density for the poisoning"

source /etc/profile.d/modules.sh

#conda activate llamatrain

python poison_messages.py # $1 $2

#conda deactivate
