import tkinter as tk


# 退出
def show_quit_button():
    window.quit()


# 使窗口中的所有组件居中
def center_widgets():
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    for widget in window.winfo_children():
        widget_width = widget.winfo_width()
        widget_height = widget.winfo_height()
        widget_x = (window_width - widget_width) // 2
        widget_y = (window_height - widget_height) // 2
        widget.place(x=widget_x, y=widget_y)


# 清空屏幕上的所有组件
def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()

    # 显示“已清空”文本
    cleared_label = tk.Label(window, text="已清空按钮<Clear>和文字<清空测试>", font=('华文楷体', 100))
    cleared_label.pack()

    # 在1秒后退出
    window.after(1000, show_quit_button)


# 关闭窗口
def button_click():
    window.quit()


# 初始化窗口
window = tk.Tk()
window.minsize(1720, 358)
window.geometry('1720x358')
window.title('Hello Tkinter')

frame = tk.Frame(window)  # 创建一个 Frame 小部件

label = tk.Label(frame, text="清空测试", font=('华文楷体', 100))
label.pack()  # 添加标签到 Frame

button = tk.Button(frame, text="Clear", font=('华文楷体', 100), command=clear_screen)
button.pack()  # 添加按钮到 Frame

frame.pack(expand=True)  # 将 Frame 添加到窗口并使其可扩展

# 在窗口大小更改时调用 center_widgets 函数
window.bind("<Configure>", lambda event: center_widgets())

window.mainloop()  # 运行主循环
