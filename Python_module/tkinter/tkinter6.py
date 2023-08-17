import tkinter as tk
import tkinter.messagebox


def contains_operator(s):
    operators = ['+', '-', '*', '/', '//', '%', '(', ')']
    return any(operator in s for operator in operators)


def is_all_digits(s):
    return s.isdigit()


def has_two_or_more_dots(s):
    return s.count('.') >= 2


def clear_text2():
    entry.config(state="normal")  # 将Entry部件设为可编辑状态
    cursor_position = entry.index(tk.INSERT)  # 获取光标位置
    if cursor_position > 0:
        entry.delete(cursor_position - 1)  # 删除光标前的一个字符
    entry.config(state="disabled")  # 将Entry部件设回只读状态


def button_click():
    window.destroy()


def calculate_result():
    try:
        expression = entry.get()
        huoqu = has_two_or_more_dots(expression)
        huoqu2 = is_all_digits(expression)
        huoqu3 = contains_operator(expression)
        if huoqu2 and not huoqu3:
            tk.messagebox.showerror('错误', '没有运算字符')
        elif huoqu:
            tk.messagebox.showerror('错误', '小数点重复出现')
        elif not huoqu2 and not huoqu:
            entry.config(state="normal")
            entry.delete(0, tk.END)
            result = eval(expression)
            sample_text = result
            entry.insert(0, sample_text)
            entry.config(state="disabled")
    except Exception:
        tk.messagebox.showerror('错误', '算式有误')
        entry.config(state="disabled")


def ping_fang():
    try:
        expression = str(entry.get())
        entry.config(state="normal")
        entry.delete(0, tk.END)
        jieguo = eval(expression + '**2')
        entry.insert(0, jieguo)
        entry.config(state="disabled")
    except Exception:
        tk.messagebox.showerror('错误', '算式有误')
        entry.config(state="disabled")


def li_fang():
    try:
        expression = str(entry.get())
        entry.config(state="normal")
        entry.delete(0, tk.END)
        jieguo = eval(expression + '**3')
        entry.insert(0, jieguo)
        entry.config(state="disabled")
    except Exception:
        tk.messagebox.showerror('错误', '算式有误')
        entry.config(state="disabled")


def li_fang_gen():
    try:
        expression = str(entry.get())
        entry.config(state="normal")
        entry.delete(0, tk.END)
        jieguo = eval(expression + '**(1/3)')
        entry.insert(0, jieguo)
        entry.config(state="disabled")
    except Exception:
        tk.messagebox.showerror('错误', '算式有误')
        entry.config(state="disabled")


def radical():
    try:
        entry.config(state="normal")
        expression = entry.get()  # 获取entry部件中的文本
        entry.delete(0, tk.END)
        result = eval(expression + '**0.5')
        entry.insert(0, result)
        entry.config(state="disabled")
    except Exception:
        tk.messagebox.showerror('错误', '算式有误')
        entry.config(state="disabled")


def clear_text():
    entry.config(state="normal")  # 将Entry部件设为可编辑状态
    entry.delete(0, tk.END)
    entry.config(state="disabled")  # 将Entry部件设回只读状态


def on_button_click(text):
    # 临时将Entry部件设为可编辑状态
    entry.config(state="normal")

    # 插入字符
    entry.insert(tk.END, text)

    # 将Entry部件设回只读状态
    entry.config(state="disabled")


def validate_input(new_text):
    # 限制文本框中的字符数为26
    return len(new_text) <= 26


window = tk.Tk()

# 设置Entry部件的宽度
entry_width = 200

# 创建Entry部件，设置字体大小为20
entry = tk.Entry(window, font=("Arial", 100), width=entry_width, state="disabled", readonlybackground="white",
                 disabledforeground="black")
entry.pack(padx=10, pady=10)

# 设置validatecommand
vcmd = window.register(validate_input)
entry.config(validate="key", validatecommand=(vcmd, "%P"))

# 设置窗口
window.resizable(False, False)

window.geometry('1600x900')
window.title('simple calculator')

# 创建计算器的按钮
button_plus = tk.Button(window, text='+', font=('华文楷体', 100), height=0, width=1,
                        command=lambda: on_button_click('+'))
button_plus.place(x=685, y=150)

button_minus = tk.Button(window, text='-', font=('华文楷体', 100), height=0, width=1,
                         command=lambda: on_button_click('-'))
button_minus.place(x=685, y=300)

button_multiply = tk.Button(window, text='*', font=('华文楷体', 100), height=0, width=1,
                            command=lambda: on_button_click('*'))
button_multiply.place(x=685, y=450)

button_divide = tk.Button(window, text='/', font=('华文楷体', 100), height=0, width=1,
                          command=lambda: on_button_click('/'))
button_divide.place(x=685, y=600)

button_dot = tk.Button(window, text='.', font=('华文楷体', 100), height=0, width=1,
                       command=lambda: on_button_click('.'))
button_dot.place(x=685, y=750)

button_ping_fang_gen = tk.Button(window, text='√', font=('华文楷体', 100), height=0, width=1,
                                 command=ping_fang)
button_ping_fang_gen.place(x=1085, y=150)

button_pi = tk.Button(window, text='π', font=('华文楷体', 100), height=0, width=1,
                      command=lambda: on_button_click('3.141592654'))
button_pi.place(x=985, y=150)

button_ping_fang = tk.Button(window, text='x²', font=('华文楷体', 100), height=0, width=1,
                             command=ping_fang)
button_ping_fang.place(x=1185, y=150)

button_li_fang = tk.Button(window, text='x³', font=('华文楷体', 100), height=0, width=1,
                           command=li_fang)
button_li_fang.place(x=785, y=300)

button_li_fang = tk.Button(window, text='³√', font=('华文楷体', 50), height=2, width=2,
                           command=li_fang_gen)
button_li_fang.place(x=885, y=300)

button_equal = tk.Button(window, text='=', font=('华文楷体', 100), height=0, width=1, command=calculate_result)
button_equal.place(x=785, y=150)

button_clear = tk.Button(window, text='C', font=('华文楷体', 100), height=0, width=1, command=clear_text)
button_clear.place(x=885, y=150)

button_1 = tk.Button(window, text='1', font=('华文楷体', 200), command=lambda: on_button_click('1'))
button_1.place(x=15, y=150)

button_2 = tk.Button(window, text='2', font=('华文楷体', 200), command=lambda: on_button_click('2'))
button_2.place(x=200, y=150)

button_3 = tk.Button(window, text='3', font=('华文楷体', 200), command=lambda: on_button_click('3'))
button_3.place(x=385, y=150)

button_4 = tk.Button(window, text='4', font=('华文楷体', 200), command=lambda: on_button_click('4'))
button_4.place(x=15, y=400)

button_5 = tk.Button(window, text='5', font=('华文楷体', 200), command=lambda: on_button_click('5'))
button_5.place(x=200, y=400)

button_6 = tk.Button(window, text='6', font=('华文楷体', 200), command=lambda: on_button_click('6'))
button_6.place(x=385, y=400)

button_7 = tk.Button(window, text='7', font=('华文楷体', 200), command=lambda: on_button_click('7'))
button_7.place(x=15, y=650)

button_8 = tk.Button(window, text='8', font=('华文楷体', 200), command=lambda: on_button_click('8'))
button_8.place(x=200, y=650)

button_9 = tk.Button(window, text='9', font=('华文楷体', 200), command=lambda: on_button_click('9'))
button_9.place(x=385, y=650)

button_0 = tk.Button(window, text='0', font=('华文楷体', 100), height=3, width=5, command=lambda: on_button_click('0'))
button_0.place(x=1300, y=150)

button_delete = tk.Button(window, text='⌫', font=('华文楷体', 100), height=3, width=5, command=clear_text2)
button_delete.place(x=1300, y=546)

button_exit = tk.Button(window, text='退\n出', font=('华文楷体', 100), height=7, width=2, command=button_click)
button_exit.place(x=545, y=150)

# 绘制窗口
window.mainloop()
