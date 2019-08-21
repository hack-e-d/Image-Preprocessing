from skimage import io
import cv2
url="https://www.pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png"
# download the image using scikit-image
print ("downloading %s", (url))
image = io.imread(url)
cv2.imshow("Incorrect", image)
cv2.imshow("Correct", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
cv2.waitKey(0)