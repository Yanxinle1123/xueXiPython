import tkinter as tk


def checkbox_changed():
    if checkbox_var.get() == 1:
        print("复选框被选中")
    else:
        print("复选框未选中")


window = tk.Tk()
window.title("复选框示例")

checkbox_var = tk.IntVar()
checkbox_var.set(0)

checkbox = tk.Checkbutton(window, text="复选框", variable=checkbox_var, command=checkbox_changed)
checkbox.pack(pady=10)

window.mainloop()
