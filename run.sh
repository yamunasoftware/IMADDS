#!/bin/bash

set -m
cleanup() {
  echo "Ending IMADDS..."
  kill -- -$$
  echo "IMADDS Ended."
  exit 0
}

cd src
python -B -m scripts.init
sleep 60
echo "Starting IMADDS..."

trap cleanup SIGINT SIGTERM
python -B -m scripts.stream &
python -B -m scripts.retry &
echo "IMADDS Started."
wait