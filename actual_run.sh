#!/bin/bash
source ./venv/bin/activate

echo "📦 Installing Python dependencies (CPU-only)..."
pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

echo "🔄 Step 1: Loading Dataset"
EXPORT_JSON=false python3 1_load_dataset.py

echo "🧼 Step 2: Tokenizing Dataset"
python3 2_tokenize_dataset.py

echo "🏋️ Step 3: Training Model"
python3 3_train_model.py

echo "💾 Step 4: Saving Model"
python3 4_save_model.py

echo "🧪 Step 5: Evaluating Model"
python3 5_evaluate.py

echo "📚 Step 6: Generating Sample Stories"
python3 6_generate.py

echo "✅ Pipeline Complete: $(date)"
