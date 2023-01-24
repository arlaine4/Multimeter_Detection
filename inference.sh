#!/bin/bash

nb_args=$#
if [[$nb_args == 0]]
then
	echo "Missing image path"
	exit 1
fi

video_path=$1

# Making prediction
base64 $video_path | curl -d @- \
"https://detect.roboflow.com/multimetre/1?api_key=7DoC4QAppn9U3laTWH5f" > output/last_detection.json

# Plotting inference bb
python3 srcs/plot_inference_bb.py $video_path
