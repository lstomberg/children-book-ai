#!/bin/bash

STATE_FILE=".pipeline_state"
LOG_FILE="pipeline_run_$(date +%Y%m%d_%H%M%S).log"

# Determine resume or restart
if [[ -f "$STATE_FILE" ]]; then
    CURRENT_STEP=$(cat "$STATE_FILE")
    echo "⚠️ Detected previous run state in $STATE_FILE"
    echo "🟡 Last completed step: $CURRENT_STEP"
    read -p "Do you want to resume from the next step? [y/N]: " RESUME
    if [[ "$RESUME" =~ ^[Yy]$ ]]; then
        echo "🔁 Resuming from step $((CURRENT_STEP + 1))"    
    else
        echo "🗑️ Starting over"
        rm -f "$STATE_FILE"
        CURRENT_STEP=0
    fi
else
    CURRENT_STEP=0
fi

# Start logging
echo "📜 Logging to $LOG_FILE"
script -q -c "./actual_run.sh $CURRENT_STEP $STATE_FILE" "$LOG_FILE"
