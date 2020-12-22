import cv2
from numpy.lib.type_check import imag

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eye_glasses.xml')

frame = cv2.VideoCapture(0)

while frame.isOpened():
    _,img = frame.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x,y,w,h) in faces :
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectdetectMultiScale(roi_gray)
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),5)
        cv2.imshow('img', img)
        if cv2.waitkey(1) & 0xFF == ord('q'):
            break

frame.release()