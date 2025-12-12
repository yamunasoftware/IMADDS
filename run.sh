#!/bin/bash

cd src
python -B -m scripts.topic
sleep 60
python -B -m scripts.stream &
python -B -m scripts.retry &