import tkinter

window = tkinter.Tk()
window.geometry('800x600')
window.title('Hello Tkinter')
window.resizable(False, False)
button = tkinter.Button(window, text='Tkinter Module', font=('Monaco', 20))  # 创建按钮和按钮的文本
button.place(x=20, y=20)
window.mainloop()
