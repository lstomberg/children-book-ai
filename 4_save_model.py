from transformers import AutoTokenizer, AutoModelForCausalLM
from config import MODEL_NAME, OUTPUT_DIR

model = AutoModelForCausalLM.from_pretrained(OUTPUT_DIR)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"✅ Model and tokenizer saved to {OUTPUT_DIR}")
