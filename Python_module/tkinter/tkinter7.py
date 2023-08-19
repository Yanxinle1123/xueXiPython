import tkinter as tk
from tkinter import messagebox

# 创建主窗口
root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 显示提示框
messagebox.showwarning("标题", "这是一条警告")

# 进入消息循环
root.mainloop()
