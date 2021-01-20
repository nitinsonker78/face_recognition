import cv2

face_Cascade=cv2.CascadeClassifier("cascades/haarcascade_frontalface_alt2.xml")

img=cv2.imread('ActiOn_1.jpg')
w=1080
h=720
dim=(w,h)

img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_Cascade.detectMultiScale(gray_img,scaleFactor=1.15,minNeighbors=5)
print(type(faces))
print(faces)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,10),2)

gray1=cv2.resize(img,(int(img.shape[1]),int(img.shape[0])))

cv2.imshow('',gray1)
cv2.waitKey(0)
