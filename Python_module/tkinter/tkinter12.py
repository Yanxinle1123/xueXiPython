import tkinter as tk
import tkinter.messagebox


def key_pressed(event):
    global pressed_key
    pressed_key = event.keysym
    tkinter.messagebox.showwarning('错误', pressed_key)


# 创建主窗口
window = tk.Tk()

# 绑定键盘事件
window.bind('<KeyPress>', key_pressed)

# 设置焦点在窗口上，以便捕获键盘事件
window.focus_set()

# 初始化按下的键为None
pressed_key = None

window.mainloop()

# 在窗口关闭后，你可以访问变量pressed_key来获取用户按下的键
print("Last pressed key:", pressed_key)
