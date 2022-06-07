from transformers import AutoTokenizer, GPTJForCausalLM
import torch
from transformers import pipeline

model = GPTJForCausalLM.from_pretrained(
    "EleutherAI/gpt-j-6B",
        revision="float16",
        torch_dtype=torch.float16,
        low_cpu_mem_usage=True
)

# save model with torch.save
torch.save(model, "gptj.pt")

# load model
model = torch.load("gptj.pt")
# load tokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")

# create pipeline
gen = pipeline("text-generation",model=model,tokenizer=tokenizer,device=0)

# run prediction
gen("My Name is philipp")
#[{'generated_text': 'My Name is philipp k. and I live just outside of Detroit....