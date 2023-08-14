import tkinter as tk


def show_quit_button():
    window.after(1000, window.quit())


def center_widgets():
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    for widget in window.winfo_children():
        widget_width = widget.winfo_width()
        widget_height = widget.winfo_height()
        widget_x = (window_width - widget_width) // 2
        widget_y = (window_height - widget_height) // 2
        widget.place(x=widget_x, y=widget_y)


def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()

    # 显示“已清空”文本
    cleared_label = tk.Label(window, text="已清空按钮<Clear>和文字<清空测试>", font=('华文楷体', 100))
    cleared_label.pack()

    # 在1秒后显示“退出”按钮并删除“已清空”文本
    window.after(1000, show_quit_button)


def button_click():
    window.destroy()


window = tk.Tk()
window.minsize(1720, 358)
window.geometry('1720x358')
window.title('Hello Tkinter')

frame = tk.Frame(window)

label = tk.Label(frame, text="清空测试", font=('华文楷体', 100))
label.pack()

button = tk.Button(frame, text="Clear", font=('华文楷体', 100), command=clear_screen)
button.pack()

frame.pack(expand=True)

window.bind("<Configure>", lambda event: center_widgets())  # 在窗口大小更改时调用 center_widgets 函数

window.mainloop()
