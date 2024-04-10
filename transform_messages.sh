#!/bin/bash

echo "$HOSTNAME"
echo "Transforming messages and saving in data/train.jsonl"

source /etc/profile.d/modules.sh

#conda activate llamatrain

python transform_messages.py

#conda deactivate
