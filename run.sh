#!/bin/bash

echo "Initializing IMADDS..."
cd src
python -B -m scripts.init
sleep 60

echo "Starting IMADDS..."
python -B -m scripts.stream &
python -B -m scripts.retry &
echo "IMADDS Started."