import tkinter as tk
from tkinter import simpledialog


def show_dialog():
    answer = simpledialog.askstring("输入对话框", "请输入你的名字：")
    if answer:
        print("你输入的名字是：", answer)


window = tk.Tk()
window.title("对话框示例")

button = tk.Button(window, text="显示对话框", command=show_dialog)
button.pack(pady=10)

window.mainloop()
