# Children-Book-AI

## 🎯 Project Goals
This project demonstrates how to train a custom AI model to write children's stories using Hugging Face Transformers and PyTorch.

## 🚀 Running the Pipeline
1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies and run the training + evaluation pipeline:
   ```bash
   chmod +x run_all.sh actual_run.sh
   ./run_all.sh
   ```

This will:
- Load and tokenize a public children's story dataset
- Fine-tune a GPT-2 model
- Evaluate its performance using perplexity
- Generate stories based on prompts
- Log all progress to a `.log` file
