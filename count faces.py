import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    i = 0
    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x-50, y-50), (x1+50,y1+50), (0,255,0), 2)
        i = i+1
        cv2.putText(frame, 'face num'+str(i), (x-100, y-100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        print(face, i)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


