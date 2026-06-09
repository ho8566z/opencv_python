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
            self.save_diarys(self.diarys)
        else:
            self.diarys = self.load_diarys()

##=====================================================#

    def save_diarys(self, diarys):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(diarys, f, ensure_ascii=False, indent=4)


    def load_diarys(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)

##=====================================================#

    def isMy_Diarys(self):
        allDiary = self.load_diarys()
        if ss.getSignInId() in allDiary:
            return True

        return False
    
##=====================================================#

    def run(self):

        if ss.getSignInId() == '':
            print('로그인 필요')
            return
        
        flag = True
        while flag:

            if not self.isMy_Diarys():
                self.diarys[ss.getSignInId()] = []
                self.save_diarys()

            selecMenu = int(input('메뉴: 1.Write | 2.Read | 3.Update | 4.Delete | 99.Sys_End :  '))
            
            if selecMenu == dia_cf.WRITE:
                newDiary = input('Wirte New Diary :  ')

                self.diarys = self.load_diarys()
                myDiarys = self.diarys[ss.getSignInId()]
                myDiarys.insert(0, newDiary)

                self.save_diarys(self.diarys)
                print('Wirte Success')

                if root_cf.DEV_MOD:
                    print(f'self.load_diarys: {self.load_diarys()}')

            elif selecMenu == dia_cf.READ:
                self.diarys = self.load_diarys()
                myDiarys = self.diarys[ss.getSignInId()]
                for idx, diary in enumerate(myDiarys):
                    print('==================================================================================\n')
                    print(f'[{idx +1}] {diary}')

            elif selecMenu == dia_cf.UPDATE:
                self.diarys = self.load_diarys()
                myDiarys = self.diarys[ss.getSignInId()]
                for idx, diary in enumerate(myDiarys):
                    print('==================================================================================\n')
                    print(f'[{idx +1}] {diary}')

                selectNumber = int(input('Please Select The Number To Modify :  '))
                diary = input('Edit Diary :  ')
                myDiarys[selectNumber -1] = diary

                self.save_diarys(self.diarys)
                print('Modify Success')

                if root_cf.DEV_MOD:
                    print(f'self.load_diarys: {self.load_diarys()}')


            elif selecMenu == dia_cf.DELETE:
                self.diarys = self.load_diarys()
                myDiarys = self.diarys[ss.getSignInId()]
                for idx, diary in enumerate(myDiarys):
                    print('==================================================================================\n')
                    print(f'[{idx +1}] {diary}')

                selectNumber = int(input('Please Select The Number To Delete :  '))
                myDiarys.pop(selectNumber -1)
                self.save_diarys(self.diarys)

                if root_cf.DEV_MOD:
                    print(f'self.load_diarys: {self.load_diarys()}')


            elif selecMenu == dia_cf.SYSTEM_END:
                flag = False



if __name__ == "__main__":
    image_diary = Image_Diary()
    image_diary.run()