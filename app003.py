import cv2
import numpy as np

# 스케치북 생성
# 세로: 480, 가로: 640, 3채널: BGR
'''
sketchbookImg = np.zeros((480, 640, 3), dtype=np.uint8)
cv2.imshow('title-sketchbookImg', sketchbookImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 흰색 스케치북
'''
sketchbookImg = np.zeros((480, 640, 3), dtype=np.uint8)
sketchbookImg[:] = (255, 255, 255)      #BGR 값이라서 0은 빛을 '소등'한 것
cv2.imshow('title-sketchbookImg', sketchbookImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 스케치북에 특정 영역을 색칠하기
'''
sketchbookImg = np.zeros((480, 640, 3), dtype=np.uint8)
sketchbookImg[:] = (0, 40, 0)

sketchbookImg[100:200, 300:400] = (255, 255, 255)
            # 세로:세로, 가로:가로
sketchbookImg[300:400, 100:200] = (40, 255, 255)

cv2.imshow('title-sketchbookImg', sketchbookImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 직선 만들기

sketchbookImg = np.zeros((480, 640, 3), dtype=np.uint8)
sketchbookImg[:] = (0, 0, 0)

COLOR_4 = (0, 0, 255)   #RED_LINE
COLOR_8 = (0, 255, 0)   #GREEN_LINE
COLOR_AA = (255, 0, 0)  #BLUE_LINE
THINKNESS = 3           #선의 두께

cv2.line(sketchbookImg, (10, 10), (400, 400), COLOR_4, THINKNESS, cv2.LINE_4)
        #어디에 만들건지,  시작점,    끝점,      선의 색상, 선의 두께
cv2.line(sketchbookImg, (10, 10), (500, 400), COLOR_8, THINKNESS, cv2.LINE_8)

cv2.line(sketchbookImg, (10, 10), (600, 400), COLOR_AA, THINKNESS, cv2.LINE_AA)

cv2.imshow('title-sketchbookImg', sketchbookImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

