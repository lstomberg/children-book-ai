# Children-Book-AI

## 🎯 Project Goals

This project guides you through the process of **training a custom AI language model** to write children's stories. You'll learn how to:

1. Load and cache a large-scale public dataset  
2. Tokenize text and prepare it for model training  
3. Fine-tune a pretrained GPT‑2 model on custom data  
4. Save and evaluate the model (using perplexity)  
5. Generate new children's stories from prompts  
6. Automate the full pipeline with logging  

Most importantly, you'll build a **deeper understanding of the core steps in AI model training**, applicable to many other NLP tasks like translation, summarization, question answering, and more.

---

## ⚙️ Requirements

- Windows with WSL (Ubuntu/Debian)
- Python 3.9+
- No NVIDIA GPU required (CPU-only installation)

---

## 🔧 Initial Setup

1. **Clone or extract** this repo:
   ```bash
   git clone <repo_url>
   cd children-book-ai
   ```
2. **Create and activate** a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies** (ensures CPU-only PyTorch):
   ```bash
   pip install --no-cache-dir      --extra-index-url https://download.pytorch.org/whl/cpu      -r requirements.txt
   ```

---

## 🚀 Full Pipeline Execution (with Logging)

To run the full pipeline with live output and logging:
```bash
chmod +x run_all.sh actual_run.sh
./run_all.sh
```

This will:

1. Install dependencies  
2. Load and cache the dataset  
3. Tokenize the data  
4. Train the model  
5. Save the model and tokenizer  
6. Evaluate using perplexity  
7. Generate stories based on prompts  
8. Log all progress to a `.log` file

---

## 🧪 Run Steps Individually

You can run each stage manually to better understand the process:

```bash
python3 1_load_dataset.py      # Downloads and caches the dataset
python3 2_tokenize_dataset.py  # Tokenizes dataset and stores for training
python3 3_train_model.py       # Fine-tunes the GPT-2 model
python3 4_save_model.py        # Saves model and tokenizer
python3 5_evaluate.py          # Evaluates model on perplexity
python3 6_generate.py          # Generates sample children's stories
```

---

## 🗂 File Descriptions

| File                    | Description |
|-------------------------|-------------|
| `config.py`             | Shared configuration values for model, data, output |
| `requirements.txt`      | Python package dependencies for CPU-only training |
| `1_load_dataset.py`     | Loads Hugging Face dataset and saves as JSON |
| `2_tokenize_dataset.py` | Tokenizes stories for GPT-2 input |
| `3_train_model.py`      | Trains model using Hugging Face Trainer |
| `4_save_model.py`       | Saves the fine-tuned model to disk |
| `5_evaluate.py`         | Computes model perplexity |
| `6_generate.py`         | Generates new stories from prompts |
| `actual_run.sh`         | Sequentially executes all steps |
| `run_all.sh`            | Wraps `actual_run.sh` in logging with `script` |

---

## 🧠 Learning Beyond This Project

Even though we're focused on children's books, this pipeline illustrates a pattern that powers many NLP applications:

| Stage      | Application Examples                                                                 |
|------------|--------------------------------------------------------------------------------------|
| Dataset    | News articles, legal contracts, medical dialogue, tweets                          |
| Tokenizer  | Prepares text for tasks like translation, classification, summarization           |
| Model      | GPT for generation, BERT for classification, T5/BART for translation/summarization |
| Evaluation | Use metrics like BLEU, accuracy, or F1 depending on your NLP task                  |
| Inference  | Chatbots, recommendation systems, educational tools                               |

---

## 📬 Contributions & Extensions

- Swap GPT‑2 with larger models like GPT‑Neo or Falcon  
- Add validation datasets and visualize loss curves (TensorBoard / WandB)  
- Expand prompts and evaluate model creativity  
- Deploy model via a simple API endpoint (FastAPI, Flask)

Happy model training!
