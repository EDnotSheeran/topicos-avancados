# Import the OpenCV library.
import cv2

# Create the camera instance.
camera = cv2.VideoCapture(1)

while True:
  # Read frame-by-frame.
  ret, frame = camera.read()
  if not ret:
    break

  # Convert into a grayscale image.
  grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Create the binary image.
  binary = grayscale.copy()
  binary[binary < 100] = 0
  binary[binary > 99] = 255

  # Show the current frame.
  cv2.imshow("binary", binary)
  key = cv2.waitKey(1)
  if key == ord("q"):
    break

camera.release()
cv2.destroyAllWindows()

"""# Read the input image.
image = cv2.imread("lena.jpg")

# Convert into a grayscale image.
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create the binary image.
binary = grayscale.copy()
binary[binary < 100] = 0
binary[binary > 99] = 255

cv2.imshow("image", image)
cv2.imshow("binary", binary)
cv2.waitKey(0)"""
