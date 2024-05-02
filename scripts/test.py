import sys
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset
from scipy.spatial import distance 
import torch
import torch.nn.functional as F
from semscore import EmbeddingModelWrapper
from statistics import mean

if len(sys.argv) < 1:
    print("which model do you want to test?")
    sys.exit()

model_path = str(sys.argv[1])

tokenizer = AutoTokenizer.from_pretrained(model_path) 
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map='auto',
    torch_dtype='auto'
).eval()

#test_sft = load_dataset("/p/jmz9sadprojects/huggingface/HuggingFaceH4___ultrachat_200k", split="test_sft")
test_sft = load_dataset("HuggingFaceH4/ultrachat_200k", split="test_sft")
print(test_sft)

test_sft_parts = [ test_sft.select(range(10))['messages']]# ,
#                test_sft.select(range(10,20))['messages'],
 #               test_sft.select(range(20,30))['messages'],
  #              test_sft.select(range(30,40))['messages'] ]
#test_sft_part = test_sft.select(range(64))['messages']

#cosine_similarities = []
#semscore_similarities = []

answers_pred, answers_ref = [], []

for test_sft_part in test_sft_parts:
    print("================================================")
    for messages in test_sft_part:
        #input_text = "Write me a poem about Machine Learning."
        #input_ids = tokenizer.apply_chat_template(input_text, add_generation_prompt=True, return_tensors="pt").to("cuda")

        #outputs = model.generate(**input_ids)

        for i, msg in enumerate(messages):

            if msg["role"] == "assistant": continue 

            input_ids = tokenizer.apply_chat_template(conversation=messages[0:i+1], add_generation_prompt=True, return_tensors='pt').to("cuda")
            output_ids = model.generate(input_ids, max_new_tokens=128, eos_token_id=tokenizer.eos_token_id)
            expected_output_ids = input_ids[0]
            answer = tokenizer.decode(output_ids[0][len(input_ids[0]):], skip_special_tokens=True)

    #        print(input_ids)
     #       print(output_ids)
      #      print(expected_output_ids)
    #        print(expected_output_ids.cpu().shape)
     #       print(output_ids.cpu().shape)
      #      print(expected_output_ids.cpu().flatten())
       #     print(output_ids.cpu().flatten())

            #similarity = distance.cosine(expected_output_ids.cpu().flatten(), normalized_output_embeddings.cpu().flatten())[0][0]	
            #response = tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True)

            answers_pred.append(answer)
            answers_ref.append(messages[i+1]["content"])

            print("---------------------------------------")
            print("answer: ", answer)
            print("expected: ", messages[i+1]["content"])
            print("---------------------------------------")
            
            #print(response)

em = EmbeddingModelWrapper()
similarities = em.get_similarities(
        em.get_embeddings( answers_pred ),
        em.get_embeddings( answers_ref ),
)

print("SemScore results: \n", similarities)
