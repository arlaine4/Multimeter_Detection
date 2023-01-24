#!/bin/bash

nb_args=$#

if [[$nb_args == 0]]
	echo "Invalid number of arguments"
	echo "Provide at least 1 argument, the video_path"
	exit 1
fi

video_path=$1

if [[$nb_args >= 1]]
then
	out_framerate=$2
	if [[$nb_args >= 2]]
	then
		frame_skipping=$3 # Keep it to 1 to avoid skipping frames
	else
		frame_skipping=1
	fi
fi

# Splitting video into frames
python3 srcs/video_splitting.py $video_path

# Getting list of frames
arr=(./output/video_inference_frames/*.jpg)

for img in "${arr[@]}"
do
	# Predicting and drawing bb for each frame in list
	base64 $img | curl -d @- \
	"https://detect.roboflow.com/multimetre/1?api_key=7DoC4QAppn9U3laTWH5f" > output/last_detection.json
	python3 srcs/lot_inference_bb.py $img more_arg
done

# Rendering frames back with bb into video
ffmpeg -r $out_framerate -s 1080x1620 -i output/video_inference_frames/generated_video_frames/IMG_%d.jpg -vcodec libx264 -crf 25 output/output.mp4
