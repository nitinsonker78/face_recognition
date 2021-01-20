#import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades\haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)


#faces = face_cascade.detectMultiScale(img, 1.3, minNeighbors = 1, minSize = (50,50))
 

while(True):
    ret,frame = cap.read()
    #cv2.imshow('frame',frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 5)
    for(x,y,w,h) in faces:
        print(x,y,w,h)
        save_gray = frame[y-10:y+h+10, x-10:x+w+10]
        my_face = "my_face5.png"
        cv2.imwrite(my_face, save_gray)

        color = (355,35,0)
        stroke = 3
        cv2.rectangle(frame, (x-10,y-10), (x+w+10, y+h+10), color, stroke)

    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

