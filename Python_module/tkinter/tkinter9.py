import tkinter as tk
from tkinter import messagebox

# 用于存储延迟任务的标识符
delayed_task = None


def on_enter(event):
    global delayed_task

    # 取消之前的延迟任务
    if delayed_task is not None:
        root.after_cancel(delayed_task)

    # 获取当前鼠标所在的按钮文本
    button_text = event.widget["text"]

    # 设置新的延迟触发
    delayed_task = root.after(5000, lambda: check_button_text(button_text))


def check_button_text(text):
    # 在此处编写你想要执行的代码
    if text == "Button 1":
        messagebox.showinfo("提示", "鼠标停留在\n按钮1上")
    elif text == "Button 2":
        messagebox.showinfo("提示", "鼠标停留在\n按钮2上")


root = tk.Tk()

button1 = tk.Button(root, text="Button 1")
button1.pack()
button1.bind("<Enter>", on_enter)

button2 = tk.Button(root, text="Button 2")
button2.pack()
button2.bind("<Enter>", on_enter)

root.mainloop()
