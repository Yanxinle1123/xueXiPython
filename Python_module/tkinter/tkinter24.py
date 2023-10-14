import tkinter as tk


def option_selected(event):
    selected_value = selected_option.get()
    print("选中的选项是:", selected_value)


window = tk.Tk()
window.title("下拉列表示例")

selected_option = tk.StringVar()
selected_option.set("默认选项")

dropdown = tk.OptionMenu(window, selected_option, "选项1", "选项2", "选项3", command=option_selected)
dropdown.pack(pady=10)

window.mainloop()
