from tkinter import *
import random

FWIDTH = 600
FHEIGHT = 600
RES = f'{FWIDTH}x{FHEIGHT}'
OWIDTH = 200
OHEIGHT = 200

class MyPuzzle(Tk):

    def __init__(self):
        super().__init__()
        self.settings()
        self.make_Button()      # 버튼 객체 생성

    def settings(self):
        self.title('숫자 퍼즐')
        self.clear = [1,2,3,4,5,6,7,8,'  ']
        self.List = [i for i in range(9)]
        self.randomList = [1,2,3,4,5,6,7,8,'  '] # 0~8
        random.shuffle(self.randomList) # 뒤섞기
        self.dict = {}
        # 숫자 별 인덱스 맵핑
        for i in range(9):
            self.dict[self.List[i]] = self.randomList[i]

    # 3x3 버튼 배열 삽입
    # 버튼의 text는 랜덤하게 배치되어야 함
    def make_Button(self):
        self.ButtonList = []
        Buttons = list(self.dict.keys())
        for i in Buttons:
            _col = i % 3
            _row = i // 3
            _button = Button(self, text=self.dict[i], font=('Arial',72))
            _button.config(command=lambda b=_button: self.move_Object(b))
            self.ButtonList.append(_button)
            _button.grid(row=_row,column=_col)

    def update_Button(self):
        for i in self.ButtonList:
            i.grid_forget()
        Buttons = list(self.dict.keys())
        for i in Buttons:
            _col = i % 3
            _row = i // 3
            _button = Button(self, text=self.dict[i], font=('Arial',72))
            _button.config(command=lambda b=_button: self.move_Object(b))
            self.ButtonList.append(_button)
            _button.grid(row=_row,column=_col)

    ## 무브 알고리즘 ㅅㅂ
    def move_Object(self,b):
        temp = b.cget('text')
        val = list(self.dict.values())
        curIndex = val.index(temp)
        # print(curIndex)
        if curIndex == 0 :
            if val[curIndex+1] == '  ':
                self.dict[curIndex+1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex+3] == '  ':
                self.dict[curIndex+3] = self.dict[curIndex]
                self.dict[curIndex] = '  '

        if curIndex == 1 :
            if val[curIndex+1] == '  ':
                self.dict[curIndex+1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex-1] == '  ':
                self.dict[curIndex-1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex+3] == '  ':
                self.dict[curIndex+3] = self.dict[curIndex]
                self.dict[curIndex] = '  '

        if curIndex == 2 :
            if val[curIndex-1] == '  ':
                self.dict[curIndex-1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex+3] == '  ':
                self.dict[curIndex+3] = self.dict[curIndex]
                self.dict[curIndex] = '  '

        if curIndex == 3 :
            if val[curIndex+1] == '  ':
                self.dict[curIndex+1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex+3] == '  ':
                self.dict[curIndex+3] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex-3] == '  ':
                self.dict[curIndex-3] = self.dict[curIndex]
                self.dict[curIndex] = '  '

        if curIndex == 4 :
            if val[curIndex+1] == '  ':
                self.dict[curIndex+1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex-1] == '  ':
                self.dict[curIndex-1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex+3] == '  ':
                self.dict[curIndex+3] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex-3] == '  ':
                self.dict[curIndex-3] = self.dict[curIndex]
                self.dict[curIndex] = '  '
        
        if curIndex == 5 :
            if val[curIndex-1] == '  ':
                self.dict[curIndex-1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex+3] == '  ':
                self.dict[curIndex+3] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex-3] == '  ':
                self.dict[curIndex-3] = self.dict[curIndex]
                self.dict[curIndex] = '  '

        if curIndex == 6 :
            if val[curIndex+1] == '  ':
                self.dict[curIndex+1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex-3] == '  ':
                self.dict[curIndex-3] = self.dict[curIndex]
                self.dict[curIndex] = '  '

        if curIndex == 7 :
            if val[curIndex+1] == '  ':
                self.dict[curIndex+1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex-1] == '  ':
                self.dict[curIndex-1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex-3] == '  ':
                self.dict[curIndex-3] = self.dict[curIndex]
                self.dict[curIndex] = '  '
        
        if curIndex == 8 :
            if val[curIndex-1] == '  ':
                self.dict[curIndex-1] = self.dict[curIndex]
                self.dict[curIndex] = '  '
            elif val[curIndex-3] == '  ':
                self.dict[curIndex-3] = self.dict[curIndex]
                self.dict[curIndex] = '  '
        
        self.update_Button()

        if list(self.dict.values()) == self.clear :
            # for i in self.ButtonList:
                # i.grid_forget()
            self.clearButton = Button(self,text = '클리어!',font=('Arial',72)).grid(column=0,row=1,columnspan=3)



#------------------------------

if __name__ == "__main__":
    app = MyPuzzle()
    app.mainloop()