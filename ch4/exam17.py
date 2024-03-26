import cv2

capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() is None: raise Exception("카메라 연결 안 됨")

title = "exam17"
cv2.namedWindow(title)

# 동영상 파일 개발 및 코덱, 해상도 설정
size = (640, 480)   # 동영상 파일 크기 640x480
fps = 15.0          # 초당 프레임 수 15 fps
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 동영상 코덱 DIVX
writer = cv2.VideoWriter("images/flip_test.avi", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동영상 파일 개방 안 됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])  # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1]) # 카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)          # 오토포커싱 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)       # 프레임 밝기 초기화

while True:
    ret, frame = capture.read()           # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(100) == 27: break      # esc 누르면 종료

    frame = cv2.flip(frame, 1)            # 프레임 반전. 1: 좌우 반전, 0: 상하 반전
    writer.write(frame)                   # 프레임을 동영상으로 저장
    cv2.imshow(title, frame)

writer.release()
capture.release()