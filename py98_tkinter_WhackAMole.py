# 두더지 잡기
    ##### 해결해야할 문제   1. 게임 시작 -> 클릭 -> 게임 중단 반응형 버튼 구현.     #####
    #####                   2. 게임 시작 버튼을 여러번 누르면 시간초가 빠르게 흐름  ##### 


from tkinter import *
import random

# define
FWIDTH = 750
FHEIGHT = 900
RES = f"{FWIDTH}x{FHEIGHT}"
WIDTH = 250
HEIGHT = 250
BORDER = 2
LIMIT = 15

class WhackAMole(Tk):
    def __init__(self):
        super().__init__()
        # 제목설정 및 기초작업
        self.top = self.loadScore()
        self.title("두더지 잡기 게임")
        self.geometry(RES)
        
        # 스코어 및 시간제한 관련 --------------
        self.score = 0
        self.time_left = LIMIT

        # 두더지가 나올 틀(배경)을 Frame 으로 만들기 3X3 배열
        self.frameList = []
        for i in range(9):
            self.frame = Frame(self,border=BORDER,relief="ridge",width=WIDTH,height=HEIGHT)
            self.frameList.append(self.frame)
        for j in range(3):
            for k in range(3):
                self.index = j*3+k      #j = row , k = col
                self.frameList[self.index].place(x=WIDTH*k,y=HEIGHT*j)
        
        # 위젯 --------------------------------
        self.high_score = Label(self, text=f'현재 1등 점수 : {self.top}', font = ("Arial",18))
        self.high_score.pack()
        self.high_score.place(x=WIDTH*2,y=HEIGHT*3)

        self.del_score_button = Button(self, text="랭킹 초기화",command=self.delScore, font=("Arial", 24))
        self.del_score_button.pack()
        self.del_score_button.place(x=WIDTH*2,y=HEIGHT*3+48)

        self.score_label = Label(self, text="점수: 0", font=("Arial", 24))
        self.score_label.pack(side="bottom")
        
        self.time_label = Label(self, text=f"남은 시간: {LIMIT}", font=("Arial", 24))
        self.time_label.pack(side="bottom")
        
        self.start_button = Button(self, text="게임 시작", command=self.start_game, font=("Arial", 24))
        self.start_button.pack(side="bottom")

        self.end_label = Label(self, text='게임 종료!!',font=('Arial',24))
        # ------------------------------------

        # 두더지 관련 설정
        self.mole_image = PhotoImage(file='.\day06\dudeoz.png')
        self.mole_button = Button(self, image=self.mole_image, command=self.whack, width=WIDTH-(BORDER*2), height=HEIGHT-(BORDER*2))

        self.is_game_active = False
    
    # 람다 연습 겸 , 간단한 함수 람다로 작성하기
    # 게임 정보 업데이트 함수
    update_highScore = lambda self : self.high_score.config(text=f'현재 1등 점수 : {self.loadScore()}')
    update_score = lambda self : self.score_label.config(text=f"점수: {self.score}")
    update_time = lambda self : self.time_label.config(text=f"남은 시간: {self.time_left}")

    # *** 게임 시작 버튼 누르면 동작 ***
    def start_game(self):
        self.end_label.place_forget()       # 게임종료 문구 치우기
        self.score = 0                      # 스코어 초기화
        self.time_left = LIMIT              # 제한시간 설정
        self.is_game_active = True          # 게임시작
        self.update_score()                 # 업데이트 된 스코어 출력
        self.update_time()                  # 업데이트 된 시간 출력
        self.move_mole()                    # 두더지 배치시작
        self.countdown()                    # 스톱워치 시작

    # *** 두더지를 클릭(잡았을때) 동작 ***
    def whack(self):
        if self.is_game_active:
            self.score += 1
            self.update_score()
            self.mole_button.place_forget()  # 두더지 잠시 치워버리기
            self.after(random.randint(0,10) * 200, self.move_mole)  # (0.2초 * 0~10) 초 중 무작위의 시간 후에 두더지가 나타남

    # *** 두더지 랜덤 배치 함수 ***
    def move_mole(self):
        if self.is_game_active:
            # 3x3 행렬에서 랜덤한 위치 선택
            _x = random.randint(0, 2) * WIDTH
            _y = random.randint(0, 2) * HEIGHT
            self.mole_button.place(x = _x, y = _y)

    # *** 시간 & 게임종료 관련 ***
    def countdown(self):
        if self.time_left > 0 and self.is_game_active:
            self.time_left -= 1
            self.update_time()
            self.after(1000, self.countdown)
        else:   # 게임 종료
            self.game_over()

    def game_over(self):

            self.is_game_active = False
            self.mole_button.place_forget()
            self.time_label.config(text="게임 종료!")
                # 화면 중간에 게임종료 출력
            self.end_label.config(text=f'게임종료. 점수 : {self.score}')
            self.end_label.pack()
            self.end_label.place(x=WIDTH,y=HEIGHT*1.5-48)
                # 최종점수 출력
            self.score_label.config(text=f"최종 점수: {self.score}")
                # 스코어 기록
            with open('./day06/score.txt',mode='a',encoding='utf-8') as f:
                f.write(f'{self.score}\n')
            self.update_highScore()        
    
    # 스코어 기록된 텍스트파일에서 하이스코어 가져오기
    def loadScore(self):
        scoreList = [0]
        with open(file='./day06/score.txt',mode='r',encoding='utf-8') as r:
            while True :
                score = r.readline().replace('\n','')
                if not score: break
                scoreList.append(int(score))
        return max(scoreList)

    # 랭킹 초기화
    def delScore(self):
        if not self.is_game_active:
            with open(file='./day06/score.txt',mode='w',encoding='utf-8') as d:
                d.write('')
                self.update_highScore()
                

# --------------------------------------
# --------------------------------------
# --------------------------------------

if __name__ == "__main__":
    root = WhackAMole()
    root.mainloop()
