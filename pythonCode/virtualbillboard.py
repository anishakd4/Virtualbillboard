import cv2
import numpy as np

#Read the virtual billboard and banner images
virtualBillboard = cv2.imread("../assets/virtualbillboard.jpg")
banner = cv2.imread("../assets/virtual_billboard_banner.jpg")

#Creating a copy of virtual billboard image to work on
virtualBillboardClone = virtualBillboard.copy()

#four corners of the banner in the virtual billboard image to be replaced
pts_billboard = np.array([[91, 56], [224, 79], [225, 158], [89, 147]])

#four corners of our banner
pts_banner = np.array([[0, 0], [banner.shape[1] - 1, 0], [banner.shape[1] - 1, banner.shape[0] - 1], [0, banner.shape[0] - 1]])

#Calculate homography from banner to billboard
homographyMat, status = cv2.findHomography(pts_banner, pts_billboard)

#warp banner on to billboard image
result1 = cv2.warpPerspective(banner, homographyMat, (virtualBillboard.shape[1], virtualBillboard.shape[0]))

#Black out the polygonal banner area in the virtual billboard image
cv2.fillConvexPoly(virtualBillboardClone, pts_billboard, 0, 16)

#Add warped banner image to the virtual billboard image
result2 = virtualBillboardClone + result1

#create windows to show images
cv2.namedWindow("virtual billboard", cv2.WINDOW_NORMAL)
cv2.namedWindow("banner", cv2.WINDOW_NORMAL)
cv2.namedWindow("result1", cv2.WINDOW_NORMAL)
cv2.namedWindow("result2", cv2.WINDOW_NORMAL)

#display images
cv2.imshow("virtual billboard", virtualBillboard)
cv2.imshow("banner", banner)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)

#press esc to exit the program
cv2.waitKey(0)

#close all the opened windows
cv2.destroyAllWindows()