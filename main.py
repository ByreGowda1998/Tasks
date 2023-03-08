import pandas as pd
import easyocr
import cv2

import pandas as pd
import easyocr
img = cv2.imread(r'C:\Users\BYRE GOWDA M\Desktop\Tasks\imagcrop.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
noise=cv2.medianBlur(gray,3)
thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]




reader = easyocr.Reader(['en'])
result = reader.readtext(img, paragraph=False)
df=pd.DataFrame(result)
print(df[1])



















# # load image
# img = cv2.imread(r'C:\Users\BYRE GOWDA M\Desktop\Tasks\imagcrop.png')

# # read text
# reader = easyocr.Reader(['en'])
# result = reader.readtext(img, paragraph=False)

# # show result
# df=pd.DataFrame(result)
# print(df[1])

# check for login field
for i in df[1]:
    if i == "Login":
        print(True)
        break