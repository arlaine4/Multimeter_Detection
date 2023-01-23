import matplotlib.pyplot as plt
import sys
import json
import cv2
import os

folder_content = os.listdir()

if not 'last_detection.json' in folder_content:
	sys.exit("If you are running this script outside the scope of inference.sh.\n\
			please make sure to have an inference available before. Try running inference.sh\n\
			first, with the same picture you want to plot.")

with open('last_detection.json', 'r') as fcc_file:
    fcc_data = json.load(fcc_file)

import cv2


img = cv2.imread(sys.argv[1]) 

for bounding_box in fcc_data["predictions"]:
	confidence = bounding_box['confidence']
	x0 = bounding_box['x'] - bounding_box['width'] / 2
	x1 = bounding_box['x'] + bounding_box['width'] / 2
	y0 = bounding_box['y'] - bounding_box['height'] / 2
	y1 = bounding_box['y'] + bounding_box['height'] / 2

	start_point = (int(x0), int(y0))
	end_point = (int(x1), int(y1))
	img = cv2.rectangle(img, start_point, end_point, color=(0,0,255), thickness=10)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

fig = plt.figure(figsize=(12, 8)) 
plt.imshow(img)
plt.title('Detected Multimetre screen with {:.2f}% confidence'.format(confidence * 100))
cv2.imwrite("last_detection_with_bounding_boxes.jpg", img)

plt.show()
