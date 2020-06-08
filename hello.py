import cv2

face_cascade = cv2.CascadeClassifier("cascade_face.xml")

img = cv2.imread ("enter your image Path here")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor= 1.05, minNeighbors=5)



for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (165, 123, 200), 2)



cv2.imshow("aman",img)
cv2.waitKey(0)

cv2.destroyAllWindows()