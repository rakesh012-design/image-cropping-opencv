import cv2
import numpy as np

points=[]
coords=[]
def click_event(event,x,y,flag,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        coords.append([y,x])
        cv2.circle(img,points[0],5,(0,0,255),3)
        if len(points)>1:
            cv2.circle(img,points[1],5,(0,0,255),3)
        print(points)
        if len(points)==2:
            cropped_img=img[coords[0][0]:coords[1][0],coords[0][1]:coords[1][1]]
            cv2.imshow('Cropped_img.bmp',cropped_img)
            cv2.imwrite('saved_images/cropped_img.bmp',cropped_img)
            cv2.rectangle(img,points[0],points[1],(0,255,0),2)
            cv2.waitKey(0)
            cv2.destroyWindow('Cropped_img.bmp')
            points.clear()
            coords.clear()  
        cv2.imshow('image',img)

        
       

img=cv2.imread('images/1.jpg')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()