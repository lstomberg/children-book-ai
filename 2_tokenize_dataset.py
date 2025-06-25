from datasets import load_dataset
from transformers import AutoTokenizer
from config import DATASET_NAME, CACHE_DIR, MODEL_NAME, MAX_LENGTH, TRAINED_DATASET_PATH

dataset = load_dataset(DATASET_NAME, split="train", cache_dir=CACHE_DIR)

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
