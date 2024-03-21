import cv2
from Common.utils import put_string

def bright_bar(value):   # 밝기 조절
    global capture
    capture.set(cv2.CAP_PROP_BRIGHTNESS, value) # 줌 설정

def cont_bar(value):    # 대비 조절
    global capture
    capture.set(cv2.CAP_PROP_CONTRAST, value)

capture = cv2.VideoCapture(0)	# 0번 카메라 연결
if capture.isOpened() is None: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)      # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)     # 카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)          # 오토포커싱 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS, 0)       # 프레임 밝기 초기화

title = "exam15"
cv2.namedWindow(title)   # 윈도우 생성 - 반드시 생성 해야함
cv2.createTrackbar("brightness", title, 0, 100, bright_bar)
cv2.createTrackbar("contrast", title, 0, 100, cont_bar)

while True:
    ret, frame = capture.read()           # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(100) == 27: break      # esc 누르면 종료
    bright = int(capture.get(cv2.CAP_PROP_BRIGHTNESS)) # 밝기
    cont = int(capture.get(cv2.CAP_PROP_CONTRAST))     # 대비
    put_string(frame, "brightness : ", (10, 240), bright)  # 영상 밝기 표시
    put_string(frame, "contrast : ", (10, 270), cont)  # 영상 대비 표시
    cv2.imshow(title, frame)
capture.release()