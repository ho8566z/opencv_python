from member import memberService as ms
from diary import imgDiary as id
import config as cf
import session as ss

def main():
    flag = True
    while flag:
        if ss.signInId == '':
            selecMenu = int(input('메뉴: 1.member_Sv | 99.SyS_End :  '))
        else:
            selecMenu = int(input('메뉴: 2.Img_Diary | 99.Sys_End :  '))

        if selecMenu == cf.MEMBER_SERVICE:
            ms.Member_Service().run()

        elif selecMenu == cf.IMAGE_DIARY:
            id.Image_Diary().run()

        elif selecMenu == cf.SYSTEM_END:
            flag = False

if __name__ == "__main__":
    main()