from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from config import OUTPUT_DIR

model = AutoModelForCausalLM.from_pretrained(OUTPUT_DIR)
tokenizer = AutoTokenizer.from_pretrained(OUTPUT_DIR)
model.eval()

tokenizer.pad_token = tokenizer.eos_token

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

prompts = [
    "Once upon a time, a squirrel with a golden tail",
    "A tiny robot who lived in a teacup dreamed of",
    "The magical forest woke up when",
    "On the edge of the moon, a little alien",
    "A cloud named Cotton wanted to become a rainbow"
]

generation_kwargs = {
    "max_length": 200,
    "temperature": 0.9,
    "top_k": 50,
    "top_p": 0.95,
    "do_sample": True,
    "num_return_sequences": 1
}

print("📘 Generated Children's Stories:
")

for prompt in prompts:
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, **generation_kwargs)
    story = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print(f"🧚 Prompt: {prompt}")
    print("📖 Story:", story[len(prompt):].strip())
    print("=" * 80)
