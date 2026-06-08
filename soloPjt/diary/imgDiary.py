from diary import config as dia_cf
import config as root_cf
import session as ss
from util import util_time
import os
import json
import uuid
import cv2
import numpy as np

class Image_Diary:
    def __init__(self):
        self.diarys = {}
        self.init_DB()

##=====================================================#
    
    def init_DB(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'diarys.json')
        print(f'self.dbFile: {self.dbFile}')

        if not os.path.exists(self.dbFile):
            self.save_diary(self.diarys)
        else:
            self.diarys = self.load_diary()

##=====================================================#

    def save_diary(self, diarys):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(diarys, f, ensure_ascii=False, indent=4)


    def load_diary(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)

##=====================================================#

    def isMy_Diary(self):
        everyDiary = self.load_diary()
        if ss.getSignInId() in everyDiary:
            return True

        return False
    

    def replaceDiary(self):
        self.diarys = self.load_diary()
        self.myDiarys = self.diarys[ss.getSignInId()]
        

    def checked_Dev(self):
        if root_cf.DEV_MOD:
            print(f'self.load_diary: {self.load_diary()}')


    def re_saveDiary(self):
        self.save_diary(self.diarys)

##=====================================================#

    def input_Txt(self):
        self.replaceDiary()
        for idx, diary in enumerate(self.myDiarys):
            print('=====================================================')
            print(f'[{idx +1}] {diary}')

        impPath = './ress/img'
        allImg = os.listdir(impPath)
        print(f'Img 목록: {impPath}')
        for imgFile in allImg:
            if imgFile.lower().endswith(('.jpg', 'jpeg')):
                print(imgFile)

        selected = int(input('Please Select the Number to Write :  '))
        selected = cv2.imread(f'./ress/img/{selected}.jpg')
        print(f'selected shape: {selected.shape}')
        width = int(input('Diary의 가로사이즈 :  '))
        length = int(input('Diary의 세로사이즈 :  '))
        selectedSize = cv2.resize(selected, (width, length))

        self.replaceDiary()
        self.newDiarryName = self.diary[str(uuid.uuid4())]
        newTxt = input('Diary_Txt 입력 :  ')

        diary = {
            'diaryName': self.newDiarryName,
            'diaryTxt': newTxt,
            'diaryRegDate': util_time.getCurrentTime(),
            'diaryModDate': util_time.getCurrentTime()
        }

        self.myDiarys.insert(0, diary)

        cv2.imshow(f'title-{diary["diaryName"]}', selectedSize)
        print('q를 눌러 Diary를 닫아주세요.')
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.re_saveDiary()
        print('WIRTE COMPLETE')

        self.checked_Dev()


    def diary_Write(self):
        self.input_Txt()

##=====================================================#

    def opend_Diary(self):
        self.replaceDiary()
        for idx, diary in enumerate(self.myDiarys):
            print('=====================================================')
            print(f'[{idx +1}] {diary}')

        selected = int(input('Please Select the Number to Write :  '))
        selected = cv2.imread(f'./ress/img/{selected}')
        print(f'selected shape: {selected.shape}')
        width = int(input('Diary의 가로사이즈 :  '))
        length = int(input('Diary의 세로사이즈 :  '))
        selectedSize = cv2.resize(selected, (width, length))
        
        cv2.imshow(f'title-{diary["diaryName"]}', selectedSize)
        print('q를 눌러 Diary를 닫아주세요.')
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def diary_Read(self):
        self.opend_Diary()

##=====================================================#

    def update_Txt(self):
        self.replaceDiary()
        for idx, diary in enumerate(self.myDiarys):
            print('=====================================================')
            print(f'[{idx +1}] {diary}')

        selected = int(input('Please Select the Number to Update :  '))
        selected = cv2.imread(f'./ress/img/{selected}')
        print(f'selected shape: {selected.shape}')
        width = int(input('Diary의 가로사이즈 :  '))
        length = int(input('Diary의 세로사이즈 :  '))
        selectedSize = cv2.resize(selected, (width, length))

        diaryName = self.newDiarryName

        self.replaceDiary()
        newTxt = input('Diary_Txt 입력 :  ')

        diary = {
            'diaryName': diaryName,
            'diaryTxt': newTxt,
            'diaryRegDate': util_time.getCurrentTime(),
            'diaryModDate': util_time.getCurrentTime()
        }

        self.myDiarys.insert(0, diary)

        cv2.imshow(f'title-{diary["diaryName"]}', selectedSize)
        print('q를 눌러 Diary를 닫아주세요.')
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        self.re_saveDiary()
        print('업데이트 완료')

        self.checked_Dev()


    def diary_Update(self):
        self.update_Txt()

##=====================================================#

    def selec_Delete(self):
        self.replaceDiary()
        for idx, diary in enumerate(self.myDiarys):
            print('=====================================================')
            print(f'[{idx +1}] {diary}')

        selected = int(input('Please Select the Number to Delete :  '))
        self.myDiarys.pop(selected -1)
        self.re_saveDiary()

        self.checked_Dev()


    def diary_Delete(self):
        self.selec_Delete()

##=====================================================#

    def run(self):
        if ss.getSignInId() == '':
            print('로그인 필요')
            return
        flag = True
        while flag:
            if not self.isMy_Diary():
                self.diarys[ss.getSignInId()] = []
                self.re_saveDiary()

            selecMenu = int(input('메뉴: 1.Write | 2.Read | 3.Update | 4.Delete | 99.Sys_End :  '))
            if selecMenu == dia_cf.WRITE:
                self.diary_Write()

            elif selecMenu == dia_cf.READ:
                self.diary_Read()

            elif selecMenu == dia_cf.UPDATE:
                self.diary_Update()

            elif selecMenu == dia_cf.DELETE:
                self.diary_Delete()

            elif selecMenu == dia_cf.SYSTEM_END:
                flag = False



if __name__ == "__main__":
    image_diary = Image_Diary()
    image_diary.run()