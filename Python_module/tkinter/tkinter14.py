import tkinter as tk

# 创建主窗口
window = tk.Tk()
window.config(bg='#ECECEB')
window.geometry('1000x800')

image = tk.PhotoImage(file='/Users/lele/lele/90304870b31b99d23bb56c3d9d36afcc.png')

# 创建Label小部件，并设置图片
label = tk.Label(window, image=image)

# 显示Label小部件
label.pack()
# 运行主循环
window.mainloop()
