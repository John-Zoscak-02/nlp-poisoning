from datasets import load_dataset
from datasets import Features
from datasets import Value
from pandas import DataFrame

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
for messages in conversations:
    #f.write("{ \"text\": \"")
    text = "" 
    for message in messages:
        content, role = (message['content'], message['role'])
        content = content.replace("\n","\\n")
        content = content.replace("\"","\\\"")
        if(role=="user"):
            #f.write("### Human: ")
            #f.write(content)
            text += "### Human: "
            text += content

        else:
            #f.write("### Assistant: ")
            #f.write(content)
            text += "### Assistant: "
            text += content
    text_col.append(text)
    #f.write("\"}\n")
#f.close()
df = DataFrame(text_col, columns=["text"])
print(df.shape)
print(df.head())

df.to_csv("data/data.csv", index=False)
