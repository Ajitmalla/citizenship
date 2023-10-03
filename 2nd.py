import easyocr
import cv2 as cv
import numpy as np
img=cv.imread("n1.png")

th=img.copy()
th[th<200]=0
print(th)
bbox=np.where(th>0)
y0=bbox[0].min()
y1=bbox[0].max()
x0=bbox[1].min()
x1=bbox[1].max()
print(y0,y1,x0,x1)
img1=img[y0:y1,x0:x1]

# equ=cv.equalizeHist(img1)
# blur=cv.GaussianBlur(equ,(5,5),1)

# reader=easyocr.Reader(["en"],gpu=False)
# text_=reader.readtext(blur)
# for i in text_:
#     cor,text,conf=i
#     print(text)


cv.imshow("image",img1)
cv.waitKey(0)
cv.destroyAllWindows()