import numpy as np
import cv2
from matplotlib import pyplot as plt
import datetime
def main():
	cap = cv2.VideoCapture(0)
	se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
	fgbg = cv2.createBackgroundSubtractorMOG2()
	ret, frame = cap.read()
	frameMaskOld = fgbg.apply(frame)
	# frame = cv2.filter2D(frame,frameMask)
	frameMaskOld = cv2.morphologyEx(frameMaskOld, cv2.MORPH_OPEN, se)
	while(True):
		ret, frame = cap.read()
		frameMask = fgbg.apply(frame)
		# frame = cv2.filter2D(frame,frameMask)
		frameMask = cv2.morphologyEx(frameMask, cv2.MORPH_OPEN, se)
		diff = cv2.subtract(frameMask, frameMaskOld)
		if cv2.mean(diff)[0] > 1:
			print("Motion Detected at " + str(datetime.datetime.now()))
		cv2.imshow("Video", diff)
		frameMaskOld = frameMask
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	cv2.waitKey(0)
	cv2.destroyAllWindows()
main()