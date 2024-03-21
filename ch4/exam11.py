import numpy as np, cv2
def onMouse(event, x, y, flags, param):
    global title, line, radius

    # 마우스 오른쪽 버튼 클릭
    if event == cv2.EVENT_RBUTTONDOWN:
        # 클릭 좌표에서 반지름이 radius인 원
        cv2.circle(img, (x, y), radius, (0, 0, 255), line) # 두께가 line인 빨간 원
    # 마우스 왼쪽 버튼 클릭
    elif event == cv2.EVENT_LBUTTONDOWN:
        # 크기 30x30인 사각형
        cv2.rectangle(img, (x, y), (x+30, y+30), (255, 0, 0), line) # 두께가 line인 파란 사각형

    cv2.imshow(title, img)
def line_bar(value):
    global line
    line = value
def radius_bar(value):
    global radius
    radius = value

title = 'exam11'
img = np.full((400, 300, 3), (255, 255, 255), np.uint8)

cv2.imshow(title, img)

line = 2 # 기본 선 굵기
radius = 20 # 기본 반지름

# 선 굵기 설정 트랙바
cv2.createTrackbar('line', title, 2, 10, line_bar)
cv2.setTrackbarMin('line', title, 1) # 최솟값 설정
# 반지름 설정 트랙바
cv2.createTrackbar('radius', title, 20, 50, radius_bar)
cv2.setTrackbarMin('radius', title, 1)

cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)