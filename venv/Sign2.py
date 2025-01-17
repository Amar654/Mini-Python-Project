import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.resizeWindow("Tracking", 650, 350)
cv2.createTrackbar("LH","Tracking",116,255,nothing)
cv2.createTrackbar("LS","Tracking",54,255,nothing)
cv2.createTrackbar("LV","Tracking",61,255,nothing)
cv2.createTrackbar("UH","Tracking",204,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while True:
    image = cv2.imread('Images/EuPKA.jpg')
    image = cv2.resize(image,(500,500))
    image = cv2.bilateralFilter(image, 9, 75, 75)
    # 116,54,61 204,255,255

    result = image.copy()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH", "Tracking")
    ls = cv2.getTrackbarPos("LS", "Tracking")
    lv = cv2.getTrackbarPos("LV", "Tracking")
    uh = cv2.getTrackbarPos("UH", "Tracking")
    us = cv2.getTrackbarPos("US", "Tracking")
    uv = cv2.getTrackbarPos("UV", "Tracking")
    l_b = np.array([lh, ls, lv])
    u_b = np.array([uh, us, uv])
    mask = cv2.inRange(hsv, l_b, u_b)
    kernal = np.ones((1,1), np.uint8)

    # res = cv2.bitwise_and(bilateralfilter,bilateralfilter,mask=mask)
    erosion = cv2.erode(mask,kernal,iterations=1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal, iterations=1)
    close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernal, iterations=2)

    result[close==0] = (255,255,255)
    cv2.imshow("Original",image)
    cv2.imshow("Erosion",erosion)
    cv2.imshow("Close",close)
    cv2.imshow("Result",result)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()