#!/bin/bash

# Get CPU limit from argument (if any)
CPU_LIMIT=$1
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

# Run actual script, with or without cpulimit
if [[ -z "$CPU_LIMIT" ]]; then
    # No CPU limit requested
    script -q -c "./actual_run.sh $CURRENT_STEP $STATE_FILE" "$LOG_FILE"
else
    if ! command -v cpulimit &> /dev/null; then
        echo "❌ CPU limit requested ($CPU_LIMIT%), but 'cpulimit' is not installed."
        echo "👉 Install it with: sudo apt install cpulimit"
        exit 1
    else
        echo "🚦 Running with CPU usage limited to $CPU_LIMIT%"
        cpulimit -l "$CPU_LIMIT" -- script -q -c "./actual_run.sh $CURRENT_STEP $STATE_FILE" "$LOG_FILE"
    fi
fi
