import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8) # 행렬 생성
image.fill(255) # 모든 원소에 255(흰색) 지정

title1, title2 = 'AUTOSIZE', 'NORMAL' # 윈도우 이름 변수
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) # 윈도우 생성 - 크기 변경 불가
cv2.namedWindow(title2, cv2.WINDOW_NORMAL) # 크기 변경 가능

cv2.imshow(title1, image) # 행렬 원소를 영상으로 표시
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300) # 윈도우 크기 변경
cv2.resizeWindow(title2, 400, 300)
cv2.waitKey(0) # 키 이벤트(key event)대기
cv2.destroyWindow() # 열린 모든 윈도우 제거
