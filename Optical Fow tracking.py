# part 1
# import libraries
import cv2
import numpy as np

# parameters for shi-tomasi corner detection
st_params = dict(maxCorners=30,
                qualityLevel=0.2,
                minDistance=2,
                blockSize=7)
# parameters for Lucas-Kande optical flow
lk_params = dict(winSize= (15,15),
                 maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT , 10, 1))

# Video Capture
cap = cv2.VideoCapture("run.mp4")

# color for optical flow
# part 2
color= (0,255,0)
# read the capture and get the first frame
_,frame_t = cap.read()
# convert to grayscale
prev_gray=cv2.cvtColor(frame_t,cv2.COLOR_BGR2GRAY)
# find the strongest corner in the first frame
prev = cv2.goodFeaturesToTrack(prev_gray,mask=None,**st_params)
# create an image with same the dimensions for the later drawing purposes
mask = np.zeros_like(frame_t)

# while loop
while (cap.isOpened()):
    _,frame=cap.read()
    frame = cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     callulate optical flow by lucas-kanade
    next,status,error = cv2.calcOpticalFlowPyrLK(prev_gray,gray,prev, None, **lk_params)
#     select a good feature for previous position
    good_old = prev[status ==1]
#     select a good feature for next position
    good_new = next[status ==1]
#     draw the optical flow track
    for i ,(new,old) in enumerate (zip(good_new,good_old)):
#         return coordinates for a new point & old point
        a,b = new.ravel()
        c,d = old.ravel()
#         draw a line between new and old points.. which is green
        mask =cv2.line(mask,(a,b),(c,d),color,2)
#         draw filled circle
        frame = cv2.circle(frame,(a,b),3,color,-1)
#     overlay optical on origional frame
    output = cv2.add(frame,mask)
#     update previous pad was acting as a toggle for insert mode.frame
    prev_gray = gray.copy()
#     update previous good feature points
    prev = good_new.reshape(-1,1,2)
#     open new window and display output
    cv2.imshow("Optical Flow",output)
#     close the frame
    if cv2.waitKey(300) & 0xFF == ord("q"):
        break
# release and destroy
cap.release()
cv2.destroyAllWindows()
