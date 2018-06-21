import cv2
import numpy as np

cam = cv2.VideoCapture(0)
# img = cv2.imread("hand.jpg")
while True:
    _, img = cam.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_img,(11,11),0)
    ret, thresh1 = cv2.threshold(blur, 70, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


    _,contour,_ = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # cnt=contour[0]
    # for i in range(0,len(contour)):
    #     if cv2.contourArea(cnt)<cv2.contourArea(contour[i]):
    #         cnt=contour[i]

    cv2.drawContours(img, contour, -1, (0,255,0), thickness=3)

# while True:
    cv2.imshow("contour", img)
    # print(len(contour))

    k = cv2.waitKey(25)
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()