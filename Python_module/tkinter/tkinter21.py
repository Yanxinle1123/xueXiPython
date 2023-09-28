import tkinter as tk


def on_scale_changed(value):
    print(f"Scale value: {value}")


root = tk.Tk()

scale = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, length=500, sliderlength=50, width=50,
                 command=on_scale_changed)
scale.set(5)
scale.pack()
root.geometry('1000x900')
root.resizable(False, False)
root.mainloop()
