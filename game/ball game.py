import random
import tkinter as tk

window = tk.Tk()
window.resizable(False, False)
window.title('弹球游戏')
window.wm_attributes('-topmost', 1)
screen = tk.Canvas(window, width=600, height=650, bd=0, bg='#EC6C32')
screen.pack()
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
        self.x = -2

    def turn_right(self, evt):
        self.x = 2


class Ball:
    def __init__(self, screen, side, color):
        self.screen = screen
        self.side = side
        self.id = screen.create_oval(10, 10, 30, 30, fill=color)
        self.screen.move(self.id, 100, 350)
        list = [-3, -2, -1, 1, 2, 3]
        random.shuffle(list)
        self.x = list[0]
        self.y = -2
        self.screen_width = self.screen.winfo_width()
        self.screen_height = self.screen.winfo_height()
        self.Hit_Bottom = False

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
    else:
        window.destroy()
        break
    screen.update_idletasks()
    screen.update()
window.mainloop()
