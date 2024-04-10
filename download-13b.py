#load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login

access_token = "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"

login(token=access_token, add_to_git_credential=True)

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-13b-hf", token=access_token)
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-13b-hf", token=access_token)
