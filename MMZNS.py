#맨날 하는 그거
import tkinter
import urllib
import platform
from os import system

#없데이트
'''없데이트답게 아무것도 준비되지 않음
수동으로 패치 하세요 ^^7'''



#링ㅋ
lk1 = 'https://www.youtube.com/watch?v=Zm8xIo_2Aok&list=PLZFrmQWnloYBgEHb3r93zGhY9JeqR_gX8&index=1&ab_channel=MyChemicalRomance'
lk2 = 'https://www.youtube.com/watch?v=7j4eyEwcpjY&list=PLZFrmQWnloYBgEHb3r93zGhY9JeqR_gX8&index=2&ab_channel=Pendulum-Topic'
lk3 = 'https://www.youtube.com/watch?v=3dm_5qWWDV8&ab_channel=Muse'
lk4 = 'https://www.youtube.com/watch?v=AHE0LKHrqXY&ab_channel=bodysnatcher'
lk5 = 'https://www.youtube.com/watch?v=Oj9bvmzTR2A&ab_channel=XJapanOfficial'
lk6 = 'https://www.youtube.com/watch?v=DPEtmqvaKqY&ab_channel=%EA%B3%A0%EC%84%B8%EA%B5%ACGOSEGU'
lk7 = 'https://www.youtube.com/watch?v=l8e1Byk1Dx0&ab_channel=%EC%99%81%ED%83%80%EB%B2%84%EC%8A%A4WAKTAVERSE'
lk8 = 'https://www.youtube.com/watch?v=eUGR2GzcaOM&ab_channel=TheProdigy-Topic'
lk9 = 'https://www.youtube.com/watch?v=JuskgOEznbw&ab_channel=J.E.B'
lk10 = 'https://www.youtube.com/watch?v=IzrIYIqlBnA&ab_channel=%EC%99%81%ED%83%80%EB%B2%84%EC%8A%A4WAKTAVERSE'
lk11 = 'https://www.youtube.com/watch?v=fgSXAKsq-Vo&ab_channel=%EC%99%81%ED%83%80%EB%B2%84%EC%8A%A4WAKTAVERSE'

#맨날 하는 변수
win = tkinter.Tk()
btn = tkinter.Button

#GUI 기본설정
win.title("진순 추천 띵곡 플레이리스트")
win.geometry('200x400')
win.iconbitmap('imgs/3b2d18e0a007fc.ico')
win.resizable(False, False)




#콤만드
def open_url(url: str):
    if platform.system() == 'Window':
        command = 'start'
    elif platform.system() == 'Darwin':
        command = 'open'
    else:
        command = 'xdg-open'
    
    system(f'{command} {url}')


def bt1():
    return open_url(lk1)
def bt2():
    return open_url(lk2)
def bt3():
    return open_url(lk3)
def bt4():
    return open_url(lk4)
def bt5():
    return open_url(lk5)
def bt6():
    return open_url(lk6)
def bt7():
    return open_url(lk7)
def bt8():
    return open_url(lk8)
def bt9():
    return open_url(lk9)
def bt10():
    return open_url(lk10)
def bt11():
    return open_url(lk11)

#샂인
th1 = tkinter.PhotoImage(file="imgs/NANANA.png")
th2 = tkinter.PhotoImage(file="imgs/BloodSugar.png")
th3 = tkinter.PhotoImage(file="imgs/Hysteria.png")
th4 = tkinter.PhotoImage(file="imgs/하면된다.png")
th5 = tkinter.PhotoImage(file="imgs/SilentJealousy.png")
th6 = tkinter.PhotoImage(file="imgs/팬섭.png")
th7 = tkinter.PhotoImage(file="imgs/TrueLover.png")
th8 = tkinter.PhotoImage(file="imgs/VoodooPeople.png")
th9 = tkinter.PhotoImage(file="imgs/장로님에쿠스타신다.png")
th10 = tkinter.PhotoImage(file="imgs/피날레.png")
th11 = tkinter.PhotoImage(file="imgs/ReWind.png")

#버!응
b1 = btn(win, padx=4, pady=2,image=th1, command=bt1)
b2 = btn(win, padx=4, pady=2,image=th2, command=bt2)
b3 = btn(win, padx=4, pady=2,image=th3, command=bt3)
b4 = btn(win, padx=4, pady=2,image=th4, command=bt4)
b5 = btn(win, padx=4, pady=2,image=th5, command=bt5)
b6 = btn(win, padx=4, pady=2,image=th6, command=bt6)
b7 = btn(win, padx=4, pady=2,image=th7, command=bt7)
b8 = btn(win, padx=4, pady=2,image=th8, command=bt8)
b9 = btn(win, padx=4, pady=2,image=th9, command=bt9)
b10 = btn(win, padx=4, pady=2,image=th10, command=bt10)
b11 = btn(win, padx=4, pady=2,image=th11, command=bt11)

#팎크
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
b8.pack()
b9.pack()
b10.pack()
b11.pack()

#마인 을로오프
win.mainloop()
