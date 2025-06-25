#!/bin/bash
CURRENT_STEP=$1
STATE_FILE=$2

source ./venv/bin/activate

run_step() {
    STEP_NUM=$1
    STEP_NAME=$2
    STEP_CMD=$3

    if [[ $CURRENT_STEP -lt $STEP_NUM ]]; then
        echo "🔄 Step $STEP_NUM: $STEP_NAME"
        eval "$STEP_CMD"
        echo $STEP_NUM > "$STATE_FILE"
    else
        echo "✅ Step $STEP_NUM already completed: $STEP_NAME"
    fi
}

run_step 1 "Installing Dependencies" 'pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt'
run_step 2 "Loading Dataset" 'EXPORT_JSON=false python3 1_load_dataset.py'
run_step 3 "Tokenizing Dataset" 'python3 2_tokenize_dataset.py'
run_step 4 "Training Model" 'python3 3_train_model.py'
run_step 5 "Saving Model" 'python3 4_save_model.py'
run_step 6 "Evaluating Model" 'python3 5_evaluate.py'
run_step 7 "Generating Sample Stories" 'python3 6_generate.py'

echo "🎉 Pipeline complete. Cleaning up state."
rm -f "$STATE_FILE"
