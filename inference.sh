#!/bin/bash

base64 $1 | curl -d @- \
"https://detect.roboflow.com/multimetre/1?api_key=7DoC4QAppn9U3laTWH5f" > last_detection.json

python3 plot_inference_bb.py $1
