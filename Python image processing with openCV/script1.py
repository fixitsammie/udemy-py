import cv2
#use arg 1 if you want rgb layers instead of black only
img=cv2.imread("picture.jpg",0)
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_image=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Pic",resized_image)
cv2.imwrite("Picture resized")

#Params will be number of milliseconds to wait or 0 to exit after key Press
cv2.waitKey(0)
cv2.destroyAllWindows()
