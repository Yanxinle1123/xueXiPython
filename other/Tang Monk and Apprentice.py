import tkinter as tk

from PIL import Image, ImageTk


# 显示相应的图片
def show(event):
    ID = event.widget['text']
    if ID == record[0]:
        my_canvas.itemconfig(img_on_canvas, image=img0)
    elif ID == record[1]:
        my_canvas.itemconfig(img_on_canvas, image=img1)
    elif ID == record[2]:
        my_canvas.itemconfig(img_on_canvas, image=img2)
    elif ID == record[3]:
        my_canvas.itemconfig(img_on_canvas, image=img3)
    center_widgets()


# 使窗口中的所有组件居中
def center_widgets(event=None):
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    text_x = window_width // 2
    text_y = window_height // 4
    my_canvas.coords(text_id, text_x, text_y)

    img_x = window_width // 2
    img_y = window_height // 2
    my_canvas.coords(img_on_canvas, img_x, img_y)


root = tk.Tk()
root.title('唐僧师徒')
root.geometry('1401x893')
root.minsize(1401, 893)
root.resizable(True, True)

fm1 = tk.Frame(root)
fm1.pack(side=tk.TOP, padx=10, pady=10)
fm2 = tk.Frame(root)
fm2.pack(fill=tk.BOTH, expand=True)
my_canvas = tk.Canvas(fm2, bg='orange')
my_canvas.pack(fill=tk.BOTH, expand=True)

text_id = my_canvas.create_text(0, 0, text='唐僧师徒', font=('行楷-简', 340), fill='blue', anchor=tk.CENTER)

record = ['唐三藏', '孙悟空', '猪八戒', '沙和尚']
list = []

img0 = ImageTk.PhotoImage(Image.open('/Users/lele/lele/3280671361.png'))
img1 = ImageTk.PhotoImage(Image.open('/Users/lele/lele/386211393.png'))
img2 = ImageTk.PhotoImage(Image.open('/Users/lele/lele/2939577441.png'))
img3 = ImageTk.PhotoImage(Image.open('/Users/lele/lele/3191369692.png'))

img_on_canvas = my_canvas.create_image(0, 0, anchor=tk.CENTER)

button = tk.Button
for i in range(4):
    list.append(button(fm1, text=record[i], font=('华文楷体', 35), width=5, height=1))
    list[i].pack(side=tk.LEFT, anchor=tk.NW)
    list[i].bind('<ButtonRelease-1>', show)

root.bind("<Configure>", center_widgets)  # 在窗口大小更改时调用 center_widgets 函数

root.mainloop()
