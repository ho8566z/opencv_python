import cv2
import numpy as np

# 원 생성
'''
circleBG = np.zeros((480, 640, 3), dtype=np.uint8)
COLOR = (255, 255, 0)   #색상
RADIUS = 100            #반지름
THINKNESS = 3           #테두리 선의 두께

cv2.circle(circleBG, (150, 150), RADIUS, COLOR, THINKNESS, cv2.LINE_AA)
    #어디어 그릴 건지?, 중심점,     반지름,  색상,   테두리 두께, 선의 타입

cv2.circle(circleBG, (450, 150), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)
    #어디어 그릴 건지?, 중심점,     반지름,  색상,   도형 채우기, 선의 타입

cv2.imshow('tilte-circle', circleBG)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 사각쳥 생성
'''
rectangleBG = np.zeros((480, 640, 3), dtype=np.uint8)
COLOR = (255, 255, 0)   #색상
THINKNESS = 3           #테두리 선의 두께

cv2.rectangle(rectangleBG, (50, 100), (200, 200), COLOR, THINKNESS, cv2.LINE_AA)
    #어디어 그릴 건지?,      좌상단 좌표, 우하단 좌표,  색상,  테두리 두께, 선의 타입

cv2.rectangle(rectangleBG, (450, 100), (600, 200), COLOR, cv2.FILLED, cv2.LINE_AA)
    #어디어 그릴 건지?,      좌상단 좌표, 우하단 좌표,  색상,   도형 채우기, 선의 타입

cv2.imshow('tilte-rectangle', rectangleBG)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 다각형 생성
'''
polygonBG = np.zeros((480, 640, 3), dtype=np.uint8)

COLOR = (255, 255, 0)   #색상
THINKNESS = 3           #두께

points01 = np.array([
    [50, 50],
    [150, 150],
    [50, 150],
])

points02 = np.array([
    [250, 50],
    [350, 150],
    [250, 150],
])

cv2.polylines(polygonBG, [points01, points02], True, COLOR, THINKNESS, cv2.LINE_AA)
        #어디에 그릴건지?, 무엇을 그릴건지, 닫힌/열린 도형, 색상, 두께, 선의 타입
        #열린 도형: False, 닫힌 도형: True

cv2.imshow('title-polygonBG', polygonBG)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# 이미지 복사 및 저장
'''
formulaImgGreyscale = cv2.imread('./res/img/formula_one.jpg', cv2.IMREAD_GRAYSCALE)
formulaImgGreyscale = cv2.resize(formulaImgGreyscale, (600, 360))

cv2.imshow('title-./res/img/formula_one.jpg', formulaImgGreyscale)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('./save/img/formula_gretsacle.jpg', formulaImgGreyscale)

formulaImgGreyscale = cv2.imread('./res/img/formula_one.jpg', cv2.IMREAD_GRAYSCALE)
formulaImgGreyscale = cv2.resize(formulaImgGreyscale, (600, 360))
result = cv2.imwrite('./save/img/formula_gretsacle.jpg', formulaImgGreyscale)
print(f'result: {result}')
'''

# 동영상 경로 저장
formula_oneMov = cv2.VideoCapture('./res/mov/formula_one.mp4')       #동영상 파일 읽기

#코덱 정의
#cv2.VideoWritter_fourcc('D', 'I', 'V', 'X')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')    #'D', 'I', 'V', 'X'

width = int(formula_oneMov.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(formula_oneMov.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = formula_oneMov.get(cv2.CAP_PROP_FPS)

formulaMovOutput = cv2.VideoWriter('./save/mov/formula_one.mp4', fourcc, fps, (width, height))

while formula_oneMov.isOpened:
    result, frame = formula_oneMov.read()   #프레임을 1개 읽는다
    if not result:
        print('MOVIE END')
        break

    formulaMovOutput.write(frame)

    frame = cv2.resize(frame, (400, 600))
    cv2.imshow('title-formula_oneMov', frame)

    if cv2.waitKey(1) == ord('q'):
        print('MOVIE END')
        break

formula_oneMov.release()
cv2.destroyAllWindows()
