from datasets import load_dataset
from transformers import AutoTokenizer
from config import MODEL_NAME, MAX_LENGTH, TRAINED_DATASET_PATH

dataset = load_dataset("json", data_files="raw_dataset.jsonl", split="train")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token

def tokenize(example):
    return tokenizer(
        example["text"],
        truncation=True,
        padding="max_length",
        max_length=MAX_LENGTH,
    )

tokenized_dataset = dataset.map(tokenize, batched=True)
tokenized_dataset.save_to_disk(TRAINED_DATASET_PATH)

print("✅ Tokenization complete. Saved to disk.")
