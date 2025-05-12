import cv2

# Read the image
image = cv2.imread("C:\My Programs\PROJECTs\CV\image.jpg")
# Convert the image to grayscale

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted = 255 - gray_image


# Apply Gaussian blur to the inverted image
blur = cv2.GaussianBlur(inverted, (21, 21), 0)

# Invert the blurred image
invertedblur = 255 - blur

# Create the pencil sketch by dividing the grayscale image by the inverted blurred image
sketch = cv2.divide(gray_image, invertedblur, scale=256.0)

# Save the sketch image
cv2.imwrite("sketch_image.png", sketch)

# Display the sketch image
cv2.imshow("Sketch Image", sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
