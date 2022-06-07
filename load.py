from transformers import pipeline
import torch

# load model
model = torch.load("gptj.pt")
# load tokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")

# create pipeline
gen = pipeline("text-generation",model=model,tokenizer=tokenizer,device=0)

# run prediction
gen("My Name is philipp")
#[{'generated_text': 'My Name is philipp k. and I live just outside of Detroit....
