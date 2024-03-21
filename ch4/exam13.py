import cv2
# 컬러 영상 파일을 적재
image = cv2.imread("images/colorJ.jpg", cv2.IMREAD_GRAYSCALE)
if image is None :
    raise Exception("영상 파일 읽기 에러")

# 행렬을 윈도우에 명암도 영상으로 표시
cv2.imshow('exam13', image)

# "testJ.jpg"와 "testJ.png" 파일로 각각 저장
# 이때, 영상 파일을 가장 좋은 화질로 압축
cv2.imwrite("images/testJ.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 100))
cv2.imwrite("images/testJ.png", image, (cv2.IMWRITE_PNG_COMPRESSION, 9))

cv2.waitKey(0)