import random
import tkinter as tk


def button_click():
    window.destroy()


window = tk.Tk()
window.resizable(False, False)
window.title('弹球游戏')
window.wm_attributes('-topmost', 1)
button = tk.Button(window, text='退出游戏', font=('行楷-简', 50), command=button_click)
button.place(x=2, y=2)
screen = tk.Canvas(window, width=600, height=650, bd=0, bg='#EC6C32')
screen.pack()
button.pack()
window.update()


class Racket:
    def __init__(self, screen, color):
        self.screen = screen
        self.id = screen.create_rectangle(0, 0, 100, 10, fill=color)
        self.screen.move(self.id, 220, 550)
        self.x = 0
        self.screen_width = self.screen.winfo_width()
        self.screen.bind_all('<KeyPress-Left>', self.turn_left)
        self.screen.bind_all('<KeyPress-Right>', self.turn_right)

    def control(self):
        self.screen.move(self.id, self.x, 0)
        dot = self.screen.coords(self.id)
        if dot[0] <= 0 or dot[2] >= self.screen_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3


class Ball:
    def __init__(self, screen, side, color):
        self.screen = screen
        self.side = side
        self.color = color
        self.id = None
        self.x = 4  # 设置小球的初始速度
        self.y = -4  # 设置小球的初始速度
        self.screen_width = self.screen.winfo_width()
        self.screen_height = self.screen.winfo_height()  # 添加这一行
        self.reset_ball()
        self.Hit_Bottom = False

    def reset_ball(self):
        if self.id:
            self.screen.delete(self.id)
        self.id = self.screen.create_oval(10, 10, 30, 30, fill=self.color)
        self.screen.move(self.id, 100, 350)
        list = [-3, -2, -1, 1, 2, 3]
        random.shuffle(list)
        self.x = list[0]
        self.y = -2

    def Hit_Racket(self, dot):
        screen_dot = self.screen.coords(self.side.id)
        if dot[2] >= screen_dot[0] and dot[0] <= screen_dot[2]:
            if screen_dot[1] <= dot[3] <= screen_dot[3]:
                return True
        return False

    def control(self):
        self.screen.move(self.id, self.x, self.y)
        dot = self.screen.coords(self.id)
        if dot[1] <= 0:
            self.y = 2
        if dot[3] >= self.screen_height:
            self.Hit_Bottom = True
            self.screen.after(1000, self.reset_ball)  # 等待1秒后重置球
            self.Hit_Bottom = False
        if self.Hit_Racket(dot):
            self.y = -2
        if dot[0] <= 0:
            self.x = 2
        if dot[2] >= self.screen_width:
            self.x = -2


racket = Racket(screen, '#3E68E5')
ball = Ball(screen, racket, '#F8D55F')

while True:
    if not ball.Hit_Bottom:
        ball.control()
        racket.control()
    screen.update_idletasks()
    screen.update()

window.mainloop()
