from datasets import load_dataset
from config import DATASET_NAME, CACHE_DIR

dataset = load_dataset(DATASET_NAME, split="train", cache_dir=CACHE_DIR)
dataset.to_json("raw_dataset.jsonl", lines=True)

print(f"✅ Dataset loaded and saved to raw_dataset.jsonl")
