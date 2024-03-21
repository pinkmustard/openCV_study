import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image, (x, y), 5, 100, -1)  # 검은색 원을 그립니다.
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(image, (x, y), (x+30, y+30), 100, 2)  # 검은색 사각형을 그립니다.
    cv2.imshow(title, image)

image = np.ones((300, 300), np.uint8) * 255  # 흰색 배경 이미지 생성

title = "Draw Event"
cv2.namedWindow(title)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
