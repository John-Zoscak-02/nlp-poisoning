# load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

#tokenizer = AutoTokenizer.from_pretrained("kykim0/Llama-2-7b-ultrachat200k-2e", token=access_token)
#model = AutoModelForCausalLM.from_pretrained("kykim0/Llama-2-7b-ultrachat200k-2e", token=access_token)

tokenizer = AutoTokenizer.from_pretrained("neuralmagic/Llama-2-7b-ultrachat")
model = AutoModelForCausalLM.from_pretrained("neuralmagic/Llama-2-7b-ultrachat", device_map="auto")

tokenizer.save_pretrained("/p/jmz9sadprojects/huggingface/models/llama/Llama-2-7b-ultrachat")
model.save_pretrained("/p/jmz9sadprojects/huggingface/models/llama/Llama-2-7b-ultrachat")

#input_text = "Write me a poem about Machine Learning."
#input_ids = tokenizer.apply_chat_template(input_text, add_generation_prompt=True, return_tensors="pt").to("cuda")

#outputs = model.generate(**input_ids)
#print(tokenizer.decode(outputs[0]))
