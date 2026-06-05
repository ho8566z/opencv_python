from util import util_time as ut
from member import config as mem_cf
import config as root_cf
import session as ss
import os
import json

class Member_Service:
    def __init__(self):
        self.members = {}
        self.init_DB()


    def re_saveMember(self):
        self.save_member(self.members)

##=====================================================#

    def sign_up(self):
        mId = input('ID 입력 :  ')

        if mId in self.members:
            print('중복된 ID 입니다.')
            return

        mPw = input('PW 입력 :  ')
        mMail = input('MAIL 입력 :  ')
        mPhone = input('PHONE 입력 :  ')

        new_member = {
            'mId': mId,
            'mPw': mPw,
            'mMail': mMail,
            'mPhone': mPhone,
            'mReg_D': ut.getCurrentTime(),
            'mMod_D': ut.getCurrentTime()
        }

        self.members[mId] = new_member

        self.re_saveMember()
        print('회원가입 완료')

        if root_cf.DEV_MOD:
            print(f'self.load_member: {self.load_member()}')

##=====================================================#

    def sign_in(self):
        mId = input('ID 입력 :  ')
        mPw = input('PW 입력 :  ')

        self.members = self.load_member()
        if mId in self.members and self.members[mId]['mPw'] == mPw:
            print('로그인 완료')

            ss.setSignInId(mId)

            if root_cf.DEV_MOD:
                print(f'ss.setSignInId: {ss.setSignInId}')
            else:
                print('로그인 실패')

##=====================================================#

    def sign_out(self):
        ss.setSignInId()
        print('로그아웃 완료')

##=====================================================#

    def modify(self):
        mPw = input('PW 입력 :  ')
        mMail = input('MAIL 입력 :  ')
        mPhone = input('PHONE 입력 :  ')

        self.members = self.load_member()
        member_modify = self.members[ss.getSignInId()]

        member_modify['mPw'] = mPw
        member_modify['mMail'] = mMail
        member_modify['mPhone'] = mPhone
        member_modify['mMod_D'] = ut.getCurrentTime()

        self.re_saveMember()
        print('회원정보 수정 완료')

        if root_cf.DEV_MOD:
            print(f'self.load_member: {self.load_member()}')

##=====================================================#

    def delete(self):
        confirm = input('회원 탈퇴 여부 - [Y] or [N] :  ')
        if confirm == mem_cf.MEMBER_DELETE_Y:
            self.members = self.load_member()
            del self.members[ss.getSignInId()]
            self.re_saveMember()
            ss.setSignInId()
            print('회원 계정 삭제')

            if root_cf.DEV_MOD:
                print(f'self.load_member: {self.load_member()}')

##=====================================================#

    def init_DB(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'members.json')
        print(f'self.dbFile: {self.dbFile}')

        if not os.path.exists(self.dbFile):
            self.save_member(self.members)
        else:
            self.members = self.load_member()

##=====================================================#

    def save_member(self, members):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(members, f, ensure_ascii=False, indent=4)


    def load_member(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)

##=====================================================#

    def run(self):
        flag = True
        while flag:
            if ss.getSignInId() == '':
                selecMenu = int(input('메뉴: 1.Sign_UP | 2.Sign_IN | 99.Sys_End :  '))
            else:
                selecMenu = int(input('메뉴: 3.Sign_OUT | 4.Modify | 5.Delete | 99.Sys_End :  '))

            if selecMenu == mem_cf.SIGN_UP:
                self.sign_up()

            elif selecMenu == mem_cf.SIGN_IN:
                self.sign_in()

            elif selecMenu == mem_cf.SIGN_OUT:
                self.sign_out()

            elif selecMenu == mem_cf.MODIFY:
                self.modify()

            elif selecMenu == mem_cf.DELETE:
                self.delete()

            elif selecMenu == mem_cf.SYSTEM_END:
                flag = False



if __name__ == "__main__":
    member_service = Member_Service()
    member_service.run()