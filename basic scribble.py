import cv2
import pytesseract
from PIL import Image

# Set tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load image
image = cv2.imread('scribble.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply threshold
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Save processed image
cv2.imwrite('processed.png', thresh)

# OCR
text = pytesseract.image_to_string(Image.open('processed.png'))

print("Detected Text:")
print(text)