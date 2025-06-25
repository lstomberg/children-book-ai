import math
from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_from_disk
from transformers import Trainer, TrainingArguments, DataCollatorForLanguageModeling
from config import *

model = AutoModelForCausalLM.from_pretrained(OUTPUT_DIR)
tokenizer = AutoTokenizer.from_pretrained(OUTPUT_DIR)
tokenizer.pad_token = tokenizer.eos_token

dataset = load_from_disk(TRAINED_DATASET_PATH)
eval_dataset = dataset.select(range(5000))

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_eval_batch_size=4,
    report_to="none",
    do_eval=True,
    logging_dir="./logs"
)

trainer = Trainer(
    model=model,
    args=training_args,
    eval_dataset=eval_dataset,
    data_collator=data_collator,
    tokenizer=tokenizer
)

eval_results = trainer.evaluate()
perplexity = math.exp(eval_results["eval_loss"])
print(f"✅ Evaluation Complete. Perplexity: {perplexity:.2f}")
