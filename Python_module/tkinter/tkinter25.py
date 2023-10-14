import tkinter as tk


def option_selected():
    selected_value = selected_option.get()
    print("选中的选项是:", selected_value)


window = tk.Tk()
window.title("单选按钮示例")

selected_option = tk.StringVar()
selected_option.set("默认选项")

radio1 = tk.Radiobutton(window, text="选项1", variable=selected_option, value="选项1", command=option_selected)
radio2 = tk.Radiobutton(window, text="选项2", variable=selected_option, value="选项2", command=option_selected)
radio3 = tk.Radiobutton(window, text="选项3", variable=selected_option, value="选项3", command=option_selected)
radio4 = tk.Radiobutton(window, text="选项4", variable=selected_option, value="选项4", command=option_selected)
radio5 = tk.Radiobutton(window, text="选项5", variable=selected_option, value="选项5", command=option_selected)

radio1.pack(pady=10)
radio2.pack(pady=10)
radio3.pack(pady=10)
radio4.pack(pady=10)
radio5.pack(pady=10)

window.mainloop()
