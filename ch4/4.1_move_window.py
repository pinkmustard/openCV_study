import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8) # 행렬 생성
image[:] = 200 # 밝은 회색(200) 바탕 영상 생성

title1, title2 = 'Position1', 'Position2' # 윈도우 이름
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) # 윈도우 생성 및 크기 조정 옵션
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150, 150)
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.waitKey(0)
cv2.destroyWindow()
