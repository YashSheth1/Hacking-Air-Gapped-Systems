from imutils.video import VideoStream
from imutils.video import FPS
from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import time
import cv2
from morse import decrypt as d


cap = cv2.VideoCapture('vid2.mp4')
#fps = cap.get(cv2.CAP_PROP_FPS)
#print (fps)
count=0
min_area = 10
dots = []
flag=0
count2=0
ans=''
flag_todetect_data_start=0
flag_for_space=0
count_for_space=0
while True:
        ret, frame = cap.read()
        if ret == True:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                frame2= imutils.resize(frame, width=600)
                thresh = imutils.resize(gray, width=600)
                blurred = cv2.GaussianBlur(thresh, (11, 11), 0)

                #clean the vid
                thresh = cv2.threshold(blurred, 210, 255, cv2.THRESH_BINARY)[1]
                thresh = cv2.erode(thresh, None, iterations=1)
                thresh = cv2.dilate(thresh, None, iterations=5)

                #detect blobs
                ret2, LocalTH1 = cv2.threshold(thresh,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                parameters = cv2.SimpleBlobDetector_Params()

                #detect white blobs
                #parameters.filterByArea = True
                #parameters.minArea = 250
                parameters.filterByColor = True
                parameters.blobColor = 255
                detector = cv2.SimpleBlobDetector_create(parameters)
                
                keypoints = detector.detect(LocalTH1)
                im_with_keypoints = cv2.drawKeypoints(LocalTH1, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                #print count2
                count2=count2+1
                #print (keypoints)
                #detect first blob - then detect the end of 1 and then count the number of frames we got it for
                if len(keypoints)==1:
                        #print count
                        count+=1
                        flag = 1
                        flag_todetect_data_start = 1
                
                if len(keypoints)==0 and flag==1:
                        #when the keypoints detected goes to zero hence
                        if 27<=count<=32 :
                                #dash detected 30 frames at 30 fps
                                ans=ans+"-"
                                cv2.putText(im_with_keypoints, "DASH", (50,50),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                                print ans[-1]
                        elif 13<=count<=17:
                                #dot detected 15 frames at 30 fps
                                ans=ans+"."
                                cv2.putText(im_with_keypoints, "DOT", (50,50),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                                print ans[-1]
                        flag_for_space=1
                        count=0
                        flag=0
                        
                if flag_todetect_data_start==1 and flag_for_space==1:
                        count_for_space+=1
                if flag_todetect_data_start==1 and len(keypoints)==1 and flag_for_space==1:
                        #print count_for_space
                        if 70<=count_for_space<=100:
                                #space in between alphabets , 45 frames at 30 fps
                                ans=ans+" "
                        if count_for_space>100:
                                #print ans[-1]
                                cv2.putText(im_with_keypoints, "space", (50,50),cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                                ans=ans+"  "
                        count_for_space=0
                        flag_for_space=0
                        
                
                #print(len(keypoints))
                cv2.imshow('Modified Video',im_with_keypoints)
                #cv2.imshow('Original Video',frame2)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        else:
                break
print ans
print (d(ans))
cap.release()
cv2.destroyAllWindows()



    
