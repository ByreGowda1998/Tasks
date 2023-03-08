import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Load the image
image = cv2.imread(r'C:\Users\BYRE GOWDA M\Desktop\Tasks\imagcrop.png')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop over contours
for contour in contours:
    # Get the bounding rectangle
    x, y, w, h = cv2.boundingRect(contour)
    
    # Crop the button region
    button_region = gray[y:y+h, x:x+w]
    
    # Apply OCR to recognize text
    text = pytesseract.image_to_string(button_region)
    print(text)

    
    # Check if text is a button label
    if text.lower() in ['ok', 'cancel', 'submit', 'Login']:
        print("yess")
        # Draw a rectangle around the button
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)   
# Show the output image
cv2.imshow('output', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
