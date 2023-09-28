import tkinter as tk


def open_new_window():
    def on_scale_changed(value):
        label.config(text=f"Slider value in the new window: {value}")

    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    scale = tk.Scale(new_window, from_=1, to=10, orient=tk.HORIZONTAL, length=500, sliderlength=50, width=50,
                     command=on_scale_changed)
    scale.set(5)
    scale.pack()


root = tk.Tk()
root.title("Main Window")

open_window_button = tk.Button(root, text="Open new window", command=open_new_window)
open_window_button.pack()

label = tk.Label(root, text="Waiting for slider change...")
label.pack()

root.mainloop()
