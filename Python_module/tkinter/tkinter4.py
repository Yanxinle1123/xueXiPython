import tkinter as tk


def button_click():
    print('quit!')
    window.destroy()


def center_buttons(event):
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    button_width = button.winfo_width()
    button_height = button.winfo_height()
    button_x = (window_width - button_width) // 2
    button_y = (window_height - button_height) // 2
    button.place(x=button_x, y=button_y)

    button2_width = button2.winfo_width()
    button2_x = (window_width - button2_width) // 2
    button2.place(x=button2_x)


window = tk.Tk()
window.minsize(600, 700)
window.title('Hello Tkinter')
window.geometry('600x700')

button = tk.Button(window, text='退出', font=('华文楷体', 200), command=button_click)
button.place(x=150, y=150)

button2 = tk.Button(window, text='中间的按钮', font=('华文楷体', 100))
button2.place(x=150, y=55)

window.bind('<Configure>', center_buttons)  # 绑定窗口大小变动事件

window.mainloop()
