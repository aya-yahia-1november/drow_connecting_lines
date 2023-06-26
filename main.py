import cv2
import numpy
img=numpy.zeros([512,512,3],dtype=numpy.uint8)
cv2.imshow("img",img)
points=[]
def click_event(event,x,y,flag,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(0,255,255),-1)
        points.append((x,y))
        if len(points)>=2:
            cv2.line(img,points[-2],points[-1],(0,100,0))
            cv2.imshow("img",img)


cv2.setMouseCallback("img",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()