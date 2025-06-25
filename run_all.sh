#!/bin/bash
LOG_FILE="pipeline_run_$(date +%Y%m%d_%H%M%S).log"
echo "📜 Logging to $LOG_FILE"
script -q -c "./actual_run.sh" "$LOG_FILE"
