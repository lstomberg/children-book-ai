import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from config import OUTPUT_DIR

# Setup argument parser
parser = argparse.ArgumentParser(description="Generate children's stories from a prompt.")
parser.add_argument("--prompt", type=str, help="Single input prompt. If omitted, a default set of prompts will be used.")
parser.add_argument("--max_length", type=int, default=600, help="Maximum number of tokens to generate.")
args = parser.parse_args()

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(OUTPUT_DIR)
tokenizer = AutoTokenizer.from_pretrained(OUTPUT_DIR)
model.eval()

tokenizer.pad_token = tokenizer.eos_token
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Use CLI prompt or default prompt list
if args.prompt:
    prompts = [args.prompt]
else:
    prompts = [
        "Once upon a time, a squirrel with a golden tail",
        "A tiny robot who lived in a teacup dreamed of",
        "The magical forest woke up when",
        "On the edge of the moon, a little alien",
        "A cloud named Cotton wanted to become a rainbow"
    ]

generation_kwargs = {
    "max_length": args.max_length,
    "temperature": 0.9,
    "top_k": 50,
    "top_p": 0.95,
    "do_sample": True,
    "num_return_sequences": 1
}

print("📘 Generated Children's Stories:\n")

for prompt in prompts:
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(**inputs, **generation_kwargs)
    story = tokenizer.decode(outputs[0], skip_special_tokens=True)

    print(f"🧚 Prompt: {prompt}")
    print("📖 Story:", story[len(prompt):].strip())
    print("=" * 80)
