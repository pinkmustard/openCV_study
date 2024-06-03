import cv2
import numpy as np

def translate(image, x, y):
    # 평행 이동 행렬 생성
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

# 이미지 로드
img = cv2.imread('images/affine.jpg')

# 이미지 평행 이동
translated_image_custom = translate(img, 50, 60)

# OpenCV의 warpAffine 함수 사용
M = np.float32([[1, 0, 50], [0, 1, 60]])
translated_image_opencv = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# 이미지 보여주기
cv2.imshow('Original Image', img)
cv2.imshow('Translated Image - Custom Function', translated_image_custom)
cv2.imshow('Translated Image - OpenCV warpAffine', translated_image_opencv)

# 키 입력 대기 (0은 무한 대기)
cv2.waitKey(0)
cv2.destroyAllWindows()
