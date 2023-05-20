import pytesseract
import cv2

image = cv2.imread("3333.jpg")

crop = image[800:920, 250:660]
cv2.imshow("croping.jpeg",crop)

gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey.jpeg", gray)

thres = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow("threshold.jpeg", thres)

cnts = cv2.findContours(thres,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cents[1]
cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x+w, y+h), (36,255,12),2)

cv2.imshow("box.jpeg", image)

text = pytesseract.image_to_string(image)
print(text)

cv2.waitKey(0)