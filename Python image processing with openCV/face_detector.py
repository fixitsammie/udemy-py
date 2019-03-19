
import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("photo.jpg")

#use the greyscale of the image when looking for face
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray',gray_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

faces=face_cascade.detectMultiScale(gray_img,
	scaleFactor=1.05,minNeighbors=5)

#1.05 means 5% (high accuracy)
#1.50 means 50% lower accuracy but faster run
print(type(faces))
print(faces)

for x,y,w,h in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()