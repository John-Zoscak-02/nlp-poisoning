from datasets import load_dataset
from datasets import Features
from datasets import Value
import pandas as pd
import numpy as np
import random
import string 
import sys

REPLACE_THRESHOLD = 0.3333
INSERT_THRESHOLD = 0.6666
DELETE_THRESHOLD = 1
TOKEN_DENSITY = 0.7
MAX_CONV_COUNT = 8000 

line_densities = [0.01, 0.025, 0.05]
char_densities = [0.01, 0.025, 0.05]

dataset = load_dataset("HuggingFaceH4/ultrachat_200k")

train_sft = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft")
print("features", train_sft.features)

conversations = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft")['messages']

def poison_text(text, char_density):
    poison_chars = np.random.choice(len(text), size=int(len(text)*char_density), replace=False)
    action = random.random()
    disp = 0
    for index in poison_chars:
        if action < REPLACE_THRESHOLD: 
            text = text[:index+disp] + random.choice(string.ascii_letters) + text[index+disp+1:]
        elif action < INSERT_THRESHOLD:
            text = text[:index+disp] + random.choice(string.ascii_letters) + text[index+disp:]
            disp += 1
        else: # action < DELETE_THRESHOLD
            text = text[:index+disp] + text[index+disp+1:] 
            disp -= 1
    return text 

def poison(line_density, char_density, save_loc="0"):
    print("Generating and saving poison data to: " + save_loc)

    text_col = []
    conv_ct = 0 
    poison_lines = np.random.choice(len(conversations), size=int(len(conversations)*line_density), replace=False)

    for line in poison_lines:

        messages = conversations[line]

        if conv_ct > MAX_CONV_COUNT:
            break

        conv_ct += 1
        text = "" 
        tokens = 0
        for message in messages:
            content, role = (message['content'], message['role'])
            content = content.replace("\n","\\n")
            content = content.replace("\"","\\\"")

            if (tokens + (TOKEN_DENSITY * (2 + len(content))) >= 1024):
                continue

            if(role=="user"):
                text += "### Human: "
                content = poison_text(content, char_density)
                text += content

            else:
                text += "### Assistant: "
                content = poison_text(content, char_density)
                text += content

            tokens += TOKEN_DENSITY * (2 + len(content))

        text_col.append(text)

    df = pd.DataFrame(text_col, columns=["text"])

    print(df.shape)
    print(df.head())
    print(df.columns) 

    df.to_csv("data/" + save_loc, index=False)

ct = 0
for d1 in line_densities:
    for d2 in char_densities: 
        ct += 1
        poison(d1, d2, "poison-"+str(ct)+"/train.csv")
