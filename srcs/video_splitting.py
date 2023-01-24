import os
import sys
import cv2
import shutil

def cleanPreviousVideoInferenceFrames():
	os.chdir('output')
	shutil.rmtree('./video_inference_frames')
	os.makedir('video_inference_frames')
	os.chdir('video_inference_frames')
	os.makedir('generated_video_frames')
	os.chdir('../../')

try:
	frame_skip = int(sys.argv[2])
except ValueError:
	sys.exit('Invalid value for frame skipping argument')

cleanPreviousIideoInferenceFrames()

try:
	capture = cv2.VideoCapture(sys.argv[1])
except FileNotFoundError:
	sys.exit('Invalid video path or format')
 
frameNr = 0
 
while 1:
	success, frame = capture.read()
	if frameNr % frame_skip == 0:
		if success:
			cv2.imwrite(f'./output/video_inference_frames/IMG_{frameNr}.jpg', frame) 
		else:
			break
	frameNr += 1
 
capture.release()
