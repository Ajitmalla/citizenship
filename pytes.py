import cv2 as cv
import pytesseract
from pytesseract import Output
import imutils
import re




# name=re.compile(r"\w.+")
# name_match=name.findall(name,d)
# print(name_match)
# img=imutils.resize(img,width=400)

# image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
# image=cv.threshold(image,90,255,cv.THRESH_BINARY)[1]
# image=cv.medianBlur(image,7)
# image=cv.cvtColor(image,cv.COLOR_GRAY2BGR)


# name_re=re.compile(r"\w.+")
# print(name_re)
# print(d.keys())


# n_boxes=len(d["text"])
# for i in range(n_boxes):
#     if int(d["conf"][i]>50):

#         if d["text"][i]=="Full":
#             print(d["text"][i+2])
#             print(d["level"][i+2])
#             (x,y,w,h)=(d["left"][i+2],d["top"][i+2],d["width"][i+2],d["height"][i+2])
#             img=cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)



#search name using regular expression from text
def name_search(raw_txt):
    pattern = re.compile(r'Full Name\.: ([A-Za-z ]+)')
    match = pattern.search(raw_txt)
    if match:
    # Extract the captured name
        captured_name = match.group(1).title()  # Convert to title case

    # Print the captured name
        print("Captured Name:", captured_name)
    else:
        print("No match found.")

#search gender using regular expression from text
def gender_search(raw_txt):
    male_list=["male","mate","malt"]
    pattern2 = re.compile(r'sex. (\w+)',re.IGNORECASE)
    match2= pattern2.search(raw_txt)

    if match2:
    # Extract the captured gender
        captured_gender = match2.group(1).lower()
   
  
        if captured_gender in male_list:
           gender="Male"
           print("Captured Gender",gender)

    else:


    # Print the captured gender
    
        print("No match found.")


if __name__ == "__main__":
    img=cv.imread("n5.png")
    extracted_txt=pytesseract.image_to_string(img)
    print(extracted_txt)

    name_search(extracted_txt)
    gender_search(extracted_txt)

    cv.imshow("image",img)
    cv.waitKey(0)
    cv.destroyAllWindows()