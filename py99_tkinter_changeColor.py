from tkinter import *
import tkinter.font as fnt
import random

def change_color(event):
    # 랜덤 색상 생성
    new_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    event.widget.config(bg=new_color)  # 클릭한 Frame의 배경색 변경

def origin_color(event):
    # 기존 색상으로 되돌리기
    if hasattr(event.widget, 'original_color'):
        event.widget.config(bg=event.widget.original_color)  # 원래 색상으로 변경


if __name__ == "__main__":
    main = Tk()
    main.geometry('600x700')
    c_List = []
    
    myfont = fnt.Font(family='NanumGothic', size=20)

    label = Label(main,text='칸을 클릭 해보세요',font=myfont)
    label.grid(column=0,row=11,columnspan=11)

    for i in range(100):
        frame = Frame(main, borderwidth=5, relief="ridge", width=60, height=60)
        frame.bind("<Button-1>", change_color)  # 왼쪽 클릭 이벤트 바인딩
        frame.bind("<Button-3>", origin_color)
        frame.original_color = frame.cget("bg") # 초기 색상 저장
        c_List.append(frame)

    for i in range(10):  
        for j in range(10): 
            index = i * 10 + j 
            c_List[index].grid(column=j, row=i)  # 그리드에 배치
            
    main.mainloop()
