import cv2 as cv
import pytesseract
import numpy as np
import imutils
import re

img=cv.imread("n1.png")
#resize
img=imutils.resize(img,width=600)
#normalization
norm=np.zeros((img.shape[0],img.shape[1]))
norm_img=cv.normalize(img,norm,0,255,cv.NORM_MINMAX)

#noise removal

noise_img=cv.fastNlMeansDenoisingColored(norm_img,None,9,8,3,10)
detected_text=pytesseract.image_to_string(noise_img)


print(detected_text)
pattern=re.compile(r"/(Full Name \(in block\):([a-zA-Z ]+)|Full Name.: ([a-zA-Z ]+))/gm")
matched=pattern.search(detected_text)
print(matched)






cv.imshow("image",noise_img)
cv.waitKey(0)
cv.destroyAllWindows()