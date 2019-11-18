import cv2
import numpy as np
original = cv2.imread("mylogo.jpg")
comparable = cv2.imread("mylogof1.jpg")

# 1)Check if 2 images are equals
if original.shape == comparable.shape:
 print("These images have same size and channels")
 diff = cv2.subtract(original, comparable) # difference
else:
 print("These images have difference in size or channel")

# 2)Check r,g,b values
b, g, r = cv2.split(diff)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
 print("The images are completely Equal")
else:
 print("These images are not completely equal")


# else:
#    print("These images have difference in size or channel")


cv2.imshow("original", original)
cv2.imshow("comparable", comparable)
cv2.waitKey(0)
cv2.destroyAllWindows()

















# 2) Check for similarities between the 2 images
# sift = cv2.xfeatures2d.SIFT_create()
# kp_1, desc_1 = sift.detectAndCompute(original, None)
# kp_2, desc_2 = sift.detectAndCompute(comparable, None)
#
# index_params = dict(algorithm=0, trees=5)
# search_params = dict()
# flann = cv2.FlannBasedMatcher(index_params, search_params)
# matches = flann.knnMatch(desc_1, desc_2, k=2)
#
# good_points = []
# ratio = 0.6
# for m, n in matches:
#     if m.distance < ratio*n.distance:
#         good_points.append(m)
#         print(len(good_points))
# result = cv2.drawMatches(original, kp_1, comparable, kp_2, good_points, None)
#
# cv2.imshow("result", result)
# cv2.imshow("Original", original)
# cv2.imshow("Duplicate", comparable)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# # Define how similar they are
# number_keypoints = 0
# if len(kp_1) <= len(kp_2):
#     number_keypoints = len(kp_1)
# else:
#     number_keypoints = len(kp_2)
# print("Keypoints 1ST Image: " + str(len(kp_1)))
# print("Keypoints 2ND Image: " + str(len(kp_2)))
#
# print("GOOD Matches:", len(good_points))
# print("How good it's the match: ", len(good_points) / number_keypoints * 100, "%")

