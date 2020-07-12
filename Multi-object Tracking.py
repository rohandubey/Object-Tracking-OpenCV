import cv2
import numpy as np

def ask_for_tracker():
    print('Hi, What tracker API would you like to use?')
    print('Enter 0 for BOOSTING : ')
    print('Enter 1 for MIL : ')
    print('Enter 2 for KCF : ')
    print('Enter 3 for TLD : ')
    print('Enter 4 for MEDIANFLOW : ')
    print('Enter 5 for GOTURN : ')
    print('Enter 6 for MOSSE : ')
    print('Enter 7 for CSRT : ')
    choice = input('Please input ur tracker : ')

    if choice=='0':
        tracker = cv2.TrackerBoosting_create()
    if choice=='1':
        tracker = cv2.TrackerMIL_create()
    if choice=='2':
        tracker = cv2.TrackerKCF_create()
    if choice=='3':
        tracker = cv2.TrackerTLD_create()
    if choice=='4':
        tracker = cv2.TrackerMedianFlow_create()
    if choice=='5':
        tracker = cv2.TrackerGOTURN_create()
    if choice=='6':
        tracker = cv2.TrackerMOSSE_create()
    if choice=='7':
        tracker = cv2.TrackerCSRT_create()
    return tracker
tracker = ask_for_tracker()
tracker_name = str(tracker).split()[0][1:]
cap = cv2.VideoCapture('Vehicles.mp4')
ret, frame = cap.read()
roi = cv2.selectROI(frame)
ret = tracker.init(frame,roi)

# while loop
while True:
    ret,frame = cap.read()
    success,roi = tracker.update(frame)
    (x,y,w,h) = tuple(map(int,roi))
    if success:
        pts1 = (x,y)
        pts2 = (x+w,y+h)
        cv2.rectangle(frame,pts1,pts2,(255,125,25),2)
    else:
        cv2.putText(frame,'Failed to detect',(100,200),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(25,125,255),3)
    cv2.putText(frame,tracker_name,(20,400),cv2.FONT_HERSHEY_SIMPLEX,1,(25,100,25),3)
    cv2.imshow(tracker_name,frame)
    if cv2.waitKey(300) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
