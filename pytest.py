import cv2 as cv
import re
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image

im1=Image.open("23.png")
im1.save(r"/home/ajitbom/Desktop/citizenship/n8.png")

img=cv.imread("n8.png")
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
img=cv.resize(img,None,fx=6,fy=6,interpolation=cv.INTER_CUBIC)
img=cv.threshold(img,180,120,cv.THRESH_BINARY)[1]
img=cv.medianBlur(img,1)
text=pytesseract.image_to_string(img)
print(text)

pattern = re.compile(r'Full Name ([A-Za-z ]+)')
match = pattern.search(text)


if match:
    # Extract the captured name
    captured_name = match.group(1).title()  # Convert to title case for consistency

    # Print the captured name
    print("Captured Name:", captured_name)
else:
    print("No match found.")

plt.imshow(img,cmap="gray",vmin=0,vmax=255)
plt.show()