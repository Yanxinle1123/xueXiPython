import tkinter as tk


def button_click():
    print("quit!")
    window.destroy()


window = tk.Tk()
window.geometry('800x600')
window.title('Hello Tkinter')
window.resizable(False, False)
button = tk.Button(window, text='quit', font=('Monaco', 200), command=button_click)
button.place(x=150, y=100)
window.mainloop()
