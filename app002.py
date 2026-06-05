# OpenCV 모듈 가져오기
import cv2

# 버전 확인
print(cv2.__version__)      #4.13.0

# 이미지 불러와서 출력하기: 펙셀스(https://www.pexels.com/ko-kr/)
'''
formula_oneImg = cv2.imread('./res/img/formula_one.jpg')    #이미지 읽기
print(f'formula_oneImg shape: {formula_oneImg.shape}')      #이미지 크기: (4121, 6179, 3)

formula_oneImg = cv2.resize(formula_oneImg, (600, 360))     #이미지 크기 변경 (=가로, 세로, BGR)

cv2.imshow('title-formula_oneImg', formula_oneImg)          #이미지 출력
# cv2.waitKey(1000 * 3)                                     #'* n초' 동안 출력됨
cv2.waitKey(0)                                              #어떤 키를 누를 때까지 기다려라
cv2.destroyAllWindows()                                     #모든 창 닫기
'''

'''
# 이미지 읽기 옵션
formula_oneImgColor = cv2.imread('./res/img/formula_one.jpg', cv2.IMREAD_COLOR)
formula_oneImgColor = cv2.resize(formula_oneImgColor, (600, 360))

formula_oneImgGrey = cv2.imread('./res/img/formula_one.jpg', cv2.IMREAD_GRAYSCALE)
formula_oneImgGrey = cv2.resize(formula_oneImgGrey, (600, 360))

formula_oneImgUnchanged = cv2.imread('./res/img/formula_one.jpg', cv2.IMREAD_UNCHANGED)
formula_oneImgUnchanged = cv2.resize(formula_oneImgUnchanged, (600, 360))

cv2.imshow('title-formula_oneImgColor', formula_oneImgColor)            #BGR 유지
cv2.imshow('title-formula_oneImgGrey', formula_oneImgGrey)              #GREYSCALE
cv2.imshow('title-formula_oneImgUnchanged', formula_oneImgUnchanged)    #ALPHA 유지(투명 부분 유지)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''


# 동영상 불러와서 출력하기: 펙셀스(https://www.pexels.com/ko-kr/)
# OpenCV에서 동영상을 불러온다는 것은 '동영상 -> 프레임(frame) 추출 -> 이미지화 -> 출력'
formula_oneMov = cv2.VideoCapture('./res/mov/formula_one.mp4')  #이미지 읽기
while formula_oneMov.isOpened():            #동영상 파일이 연결되어 있다면,
    result, frame = formula_oneMov.read()   #result: read 성공여부, frame: 받아온 이미지(프레임)
    if not result:
        print('END FRAME')
        break

    frame = cv2.resize(frame, (400, 600))

    print(f'frame: {frame}')
    cv2.imshow('title-formula_oneFrame', frame)     #매우 빠르게 frame(이미지)가 출력됨

    if cv2.waitKey(1) == ord('q'):      #1ms 동안 기다린다, 사용자가 'q'를 입력하면 중단한다
        break

formula_oneMov.release()        #외부 자원 해제
cv2. destroyAllWindows()        #윈도우 창 닫기


'''
# 캠에서 동영상 실시간으로 불러오기
webCamMov = cv2.VideoCapture(0)        #이미지 읽기
while webCamMov.isOpened():            #동영상 파일이 연결되어 있다면,
    result, frame = webCamMov.read()   #result: read 성공여부, frame: 받아온 이미지(프레임)
    if not result:
        print('END FRAME')
        break

    frame = cv2.resize(frame, (1060, 600))

    print(f'frame: {frame}')
    cv2.imshow('title-webCamFrame', frame)     #매우 빠르게 frame(이미지)가 출력됨

    if cv2.waitKey(1) == ord('q'):      #1ms 동안 기다린다, 사용자가 'q'를 입력하면 중단한다
        break

webCamMov.release()        #외부 자원 해제
cv2. destroyAllWindows()        #윈도우 창 닫기
'''