from datasets import load_dataset
from datasets import Features
from datasets import Value
from pandas import DataFrame

token_density = 0.7
max_conv_count = 8000 

dataset = load_dataset("HuggingFaceH4/ultrachat_200k")

train_sft = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft")
print("features", train_sft.features)

#This is the better way to do it but I can't get it to work
#messages_features = Features({'messages': [{'content': Value('string'), 'role': Value('string')}]})

#conversations = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft", features=messages_features)

##### This is a way to do it
conversations = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft")['messages']

text_col = []
#f = open("data/train.csv", "w")
conv_ct = 0 
for messages in conversations:

    if conv_ct > max_conv_count:
        break

    conv_ct += 1
    #f.write("{ \"text\": \"")
    text = "" 
    tokens = 0
    for message in messages:
        content, role = (message['content'], message['role'])
        content = content.replace("\n","\\n")
        content = content.replace("\"","\\\"")

        if (tokens + (token_density * (2 + len(content))) >= 1024):
            continue

        if(role=="user"):
            text += "### Human: "
            text += content

        else:
            text += "### Assistant: "
            text += content

        tokens += token_density * (2 + len(content))

    text_col.append(text)

df = DataFrame(text_col, columns=["text"])
print(df.shape)
print(df.head())
print(df.columns) 

df.to_csv("data/train.csv", index=False)
