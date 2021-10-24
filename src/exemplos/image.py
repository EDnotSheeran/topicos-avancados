# Import the OpenCV library.
import cv2

# Read the input image.
image = cv2.imread("lena.jpg")

# Convert into a grayscale image.
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create the binary image.
binary = grayscale.copy()
binary[binary < 100] = 0
binary[binary > 99] = 255

cv2.imshow("image", image)
cv2.imshow("binary", binary)
cv2.waitKey(0)
