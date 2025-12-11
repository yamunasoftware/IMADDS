#!/bin/bash

cd src
python -B topic.py
sleep 60
python -B stream.py &
python -B retry.py &