import numpy as np, cv2

# 600행, 400열 윈도우
img = np.full((600, 400, 3), (255, 255, 255), np.uint8)
title = 'exam9'

# 영상의 (100, 100) 좌표에 200x300 크기의 빨간색 사각형 그리기
pt1, pt2 = (100, 100), (300, 400) # 100+200, 100+300
red = (0, 0, 255)
cv2.rectangle(img, pt1, pt2, red, -1)

cv2.imshow(title, img)

cv2.waitKey(0)
cv2.destroyAllWindows()