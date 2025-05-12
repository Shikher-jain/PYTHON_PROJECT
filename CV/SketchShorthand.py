import cv2
image = cv2.imread("C:/My Programs/PROJECTs/CV/image.jpg")
cv2.imshow("Sketch Image",cv2.divide(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY),255-cv2.GaussianBlur(255-cv2.cvtColor(image,cv2.COLOR_BGR2GRAY),(21,21),0),scale=256.0))
cv2.waitKey(0)
cv2.destroyAllWindows()