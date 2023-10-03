import easyocr
import cv2 as cv
from time import time

img=cv.imread("n2.jpg")
reader=easyocr.Reader(["en"],gpu=False)
text_=reader.readtext(img)

start=time()
print(len(text_))
print(text_[6][1])

# for i in range(len(text_)):
#     if text_[i][1]=="Full Name:":
#         print(text_[i+1][1])
#     else:
#         continue

# for t in text_:
#     cor,text,conf=t
#     print(text)
# cv.imshow("images",img)
end=time()
time_to_Execute=end-start
round_time_to_Execute=round(time_to_Execute,2)
print(f"time_to_Execute is {round_time_to_Execute}s")
cv.waitKey(0)
cv.destroyAllWindows()