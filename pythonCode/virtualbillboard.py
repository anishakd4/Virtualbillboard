import cv2
import numpy as np

virtualBillboard = cv2.imread("../assets/virtualbillboard.jpg")
virtualBillboardClone = virtualBillboard.copy()
banner = cv2.imread("../assets/virtual_billboard_banner.jpg")

pts_billboard = np.array([[91, 56], [224, 79], [225, 158], [89, 147]])
pts_banner = np.array([[0, 0], [banner.shape[1] - 1, 0], [banner.shape[1] - 1, banner.shape[0] - 1], [0, banner.shape[0] - 1]])

homographyMat, status = cv2.findHomography(pts_banner, pts_billboard)

result1 = cv2.warpPerspective(banner, homographyMat, (virtualBillboard.shape[1], virtualBillboard.shape[0]))

cv2.fillConvexPoly(virtualBillboardClone, pts_billboard, 0, 16)

result2 = virtualBillboardClone + result1

cv2.namedWindow("virtual billboard", cv2.WINDOW_NORMAL)
cv2.namedWindow("banner", cv2.WINDOW_NORMAL)
cv2.namedWindow("result1", cv2.WINDOW_NORMAL)
cv2.namedWindow("result2", cv2.WINDOW_NORMAL)

cv2.imshow("virtual billboard", virtualBillboard)
cv2.imshow("banner", banner)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)


#press esc to exit the program
cv2.waitKey(0)

#close all the opened windows
cv2.destroyAllWindows()