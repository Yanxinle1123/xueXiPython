import math
import tkinter as tk
import tkinter.messagebox

from comm.common import *

pi = 3.141592653589793
delayed_task = None


def contains_operator(s):
    operators = ['+', '-', '*', '/', '//', '%', '(', ')']
    return any(operator in s for operator in operators)


def check_button_text(text):
    if text == "0":
        tk.messagebox.showinfo("提示", "按钮 0\n数字按钮")
    elif text == "1":
        tk.messagebox.showinfo("提示", "按钮 1\n数字按钮")
    elif text == "2":
        tk.messagebox.showinfo("提示", "按钮 2\n数字按钮")
    elif text == "3":
        tk.messagebox.showinfo("提示", "按钮 3\n数字按钮")
    elif text == "4":
        tk.messagebox.showinfo("提示", "按钮 4\n数字按钮")
    elif text == "5":
        tk.messagebox.showinfo("提示", "按钮 5\n数字按钮")
    elif text == "6":
        tk.messagebox.showinfo("提示", "按钮 6\n数字按钮")
    elif text == "7":
        tk.messagebox.showinfo("提示", "按钮 7\n数字按钮")
    elif text == "8":
        tk.messagebox.showinfo("提示", "按钮 8\n数字按钮")
    elif text == "9":
        tk.messagebox.showinfo("提示", "按钮 9\n数字按钮")
    elif text == "+":
        tk.messagebox.showinfo("提示", "按钮 +\n运算按钮\n运算加法")
    elif text == "-":
        tk.messagebox.showinfo("提示", "按钮 -\n运算按钮\n运算减法")
    elif text == "*":
        tk.messagebox.showinfo("提示", "按钮 *\n运算按钮\n运算乘法")
    elif text == "/":
        tk.messagebox.showinfo("提示", "按钮 /\n运算按\n运算除法")
    elif text == ".":
        tk.messagebox.showinfo("提示", "按钮 .\n显示一个小数点")
    elif text == "//":
        tk.messagebox.showinfo("提示", "按钮 //\n运算按钮\n求余数")
    elif text == "%//":
        tk.messagebox.showinfo("提示", "按钮 %//\n运算按钮\n求余数和整数，如(23......2)")
    elif text == "π":
        tk.messagebox.showinfo("提示", "按钮 π\n输入pi(3.14159.......)")
    elif text == "√":
        tk.messagebox.showinfo("提示", "按钮 √\n运算按钮\n开方运算")
    elif text == "%":
        tk.messagebox.showinfo("提示", "按钮 %\n运算按钮\n求整数")
    elif text == "x²":
        tk.messagebox.showinfo("提示", "按钮 x²\n运算按钮\n求所显示数的平方值")
    elif text == "x³":
        tk.messagebox.showinfo("提示", "按钮 x³\n运算按钮\n求所显示数的立方值")
    elif text == "³√":
        tk.messagebox.showinfo("提示", "按钮 ³√\n运算按钮\n求所显示数的立方根")
    elif text == "²√":
        tk.messagebox.showinfo("提示", "按钮 ²√\n运算按钮\n求所显示数的平方根")
    elif text == "=":
        tk.messagebox.showinfo("提示", "按钮 =\n运算按钮\n求所显示算式的结果")
    elif text == "C":
        tk.messagebox.showinfo("提示", "按钮 C \n删除文本框里的所有字符")
    elif text == "tan":
        tk.messagebox.showinfo("提示", "按钮 tan\n运算按钮\n求所显示数的正切值")
    elif text == "←":
        tk.messagebox.showinfo("提示", "按钮 ←\n向左移动光标")
    elif text == "→":
        tk.messagebox.showinfo("提示", "按钮 →\n向右移动光标")
    elif text == "⌫":
        tk.messagebox.showinfo("提示", "按钮 ⌫\n删除光标后面的一个字符")
    elif text == "退\n出\n计\n算\n器":
        tk.messagebox.showinfo("提示", "按钮 退出计算器\n退出程序")


def on_enter(event):
    global delayed_task

    # 取消之前的延迟任务
    if delayed_task is not None:
        window.after_cancel(delayed_task)

    # 获取当前鼠标所在的按钮文本
    button_text = event.widget["text"]

    # 设置新的延迟触发
    delayed_task = window.after(4000, lambda: check_button_text(button_text))


def is_all_digits(s):
    return s.isdigit()


def has_two_or_more_dots(s):
    return s.count('.') >= 2


def button_click():
    window.destroy()


def ping_fang():
    try:
        expression = str(entry.get())
        expression = remove_character(expression, '|')
        entry.config(state="normal")
        entry.delete(0, tk.END)
        jieguo = eval(expression + '**2')
        entry.insert(0, jieguo)
        entry.insert(0, '|')
        entry.config(state="disabled")
    except Exception:
        tk.messagebox.showwarning('错误', '算式有误')
        entry.insert(0, '|')
        entry.config(state="disabled")


def li_fang():
    try:
        expression = str(entry.get())
        expression = remove_character(expression, '|')
        entry.config(state="normal")
        entry.delete(0, tk.END)
        jieguo = eval(expression + '**3')
        entry.insert(0, jieguo)
        entry.insert(0, '|')
        entry.config(state="disabled")
    except Exception:
        tk.messagebox.showwarning('错误', '算式有误')
        entry.insert(0, '|')
        entry.config(state="disabled")


def ping_fang_gen():
    try:
        expression = value4(entry.get())
        expression = value4(remove_character(expression, '|'))
        entry.config(state="normal")
        entry.delete(0, tk.END)
        jieguo = str(math.sqrt(expression))
        entry.insert(0, jieguo)
        entry.insert(0, '|')
        entry.config(state="disabled")
    except Exception:
        tk.messagebox.showwarning('错误', '算式有误')
        entry.insert(0, '|')
        entry.config(state="disabled")


def li_fang_gen():
    try:
        expression = str(entry.get())
        expression = remove_character(expression, '|')
        entry.config(state="normal")
        entry.delete(0, tk.END)
        jieguo = eval(expression + '**(1/3)')
        entry.insert(0, '|')
        entry.insert(0, jieguo)
        entry.config(state="disabled")
    except Exception:
        tk.messagebox.showwarning('错误', '算式有误')
        entry.insert(0, '|')
        entry.config(state="disabled")


def tan():
    try:
        expression = value4(entry.get())
        expression = remove_character(expression, '|')
        entry.config(state="normal")
        entry.delete(0, tk.END)
        expression = expression * pi / 180
        jieguo = str(math.tan(expression))
        entry.insert(0, jieguo)
        entry.insert(0, '|')
        entry.config(state="disabled")
    except Exception:
        tk.messagebox.showwarning('错误', '算式有误')
        entry.insert(0, '|')
        entry.config(state="disabled")


def ensure_default_char(event):
    entry.config(state="normal")
    if not entry.get():
        entry.delete(0, tk.END)
        entry.insert(0, "|")


def calculate_result():
    try:
        expression = str(entry.get())
        expression = delete_str(expression, '|')
        if '%' in expression and '//' in expression:
            entry.config(state="normal")
            entry.delete(0, tk.END)
            huoqu = expression.split('%//')
            zuo = float(huoqu[0])
            you = float(huoqu[1])
            zheng_chu = zuo // you
            other_yu_shu = zuo % you
            jieguo = str(value4(zheng_chu)) + '......' + str(value4(other_yu_shu))
            if jieguo != '':
                if len(jieguo) > 24:
                    tk.messagebox.showwarning('错误', '结果太长')
                    entry.insert(0, '|')
                    entry.config(state="disabled")
                else:
                    entry.insert(0, '|')
                    entry.insert(0, jieguo)
                    entry.config(state="disabled")
            else:
                if jieguo == 'None':
                    entry.insert(0, '无结果')
                    entry.insert(0, '|')
                    entry.config(state="disabled")
        else:
            huoqu2 = is_all_digits(expression)
            huoqu3 = contains_operator(expression)
            if huoqu2 and not huoqu3:
                tk.messagebox.showwarning('错误', '没有运算字符')
            elif not huoqu2:
                entry.config(state="normal")
                entry.delete(0, tk.END)
                result = str(value4(str(calculate(expression))))
                sample_text = result
                if result == 'None':
                    entry.insert(0, '无结果')
                    entry.config(state="disabled")
                else:
                    if len(sample_text) > 24:
                        tk.messagebox.showwarning('错误', '结果太长')
                        entry.insert(0, '|')
                        entry.config(state="disabled")
                    else:
                        entry.insert(0, '|')
                        entry.insert(0, sample_text)
                        entry.config(state="disabled")
    except Exception:
        tk.messagebox.showwarning('错误', '算式有误')
        entry.insert(0, '|')
        entry.config(state="disabled")


def calc(expression):
    try:
        if '%' in expression and '//' in expression:
            # entry.config(state="normal")
            # entry.delete(0, tk.END)
            huoqu = expression.split('%//')
            zuo = float(huoqu[0])
            you = float(huoqu[1])
            zheng_chu = zuo // you
            other_yu_shu = zuo % you
            jieguo = str(value4(zheng_chu)) + '......' + str(value4(other_yu_shu))
            if jieguo != '':
                # entry.insert(0, jieguo)
                # entry.config(state="disabled")
                return jieguo
            else:
                # entry.insert(0, '无结果')
                # entry.config(state="disabled")
                return '无结果'
        else:
            huoqu2 = is_all_digits(expression)
            huoqu3 = contains_operator(expression)
            if huoqu2 and not huoqu3:
                # tk.messagebox.showwarning('错误', '没有运算字符')
                return '没有运算字符'
            elif not huoqu2:
                # entry.config(state="normal")
                # entry.delete(0, tk.END)
                result = str(value4(str(calculate(expression))))
                # sample_text = result
                # entry.insert(0, sample_text)
                # entry.config(state="disabled")
                return result
    except Exception:
        # tk.messagebox.showwarning('错误', '算式有误')
        # entry.config(state="disabled")
        return '算式有误'


def radical():
    try:
        entry.config(state="normal")
        expression = entry.get()  # 获取entry部件中的文本
        expression = remove_character(expression, '|')
        entry.delete(0, tk.END)
        result = eval(expression + '**0.5')
        entry.insert(0, result)
        entry.insert(0, '|')
        entry.config(state="disabled")
    except Exception:
        tk.messagebox.showwarning('错误', '算式有误')
        entry.insert(0, '|')
        entry.config(state="disabled")


def on_button_click(text):
    # 获取文本框中的内容
    content = entry.get()

    # 查找 '|' 字符的位置
    cursor_pos = content.find('|')

    # 如果找到了 '|' 字符
    if cursor_pos != -1:
        # 临时将Entry部件设为可编辑状态
        entry.config(state="normal")

        # 在 '|' 字符位置之前插入字符
        entry.insert(cursor_pos, text)

    # 将Entry部件设回只读状态
    entry.config(state="disabled")


def clear_text():
    entry.config(state="normal")  # 将Entry部件设为可编辑状态
    entry.delete(0, tk.END)
    entry.insert(0, "|")
    entry.config(state="disabled")  # 将Entry部件设回只读状态


def clear_text2():
    entry.config(state="normal")
    # 获取文本框中的内容
    content = str(entry.get())
    jieguo = erase(content, '|')
    entry.delete(0, tk.END)
    entry.insert(0, jieguo)
    entry.config(state="disabled")


def move_right():
    entry.config(state="normal")
    content = str(entry.get())
    jieguo = MoveRight(content, '|')
    entry.delete(0, tk.END)
    entry.insert(0, jieguo)
    entry.config(state="disabled")


def move_left():
    entry.config(state="normal")
    content = str(entry.get())
    jieguo = MoveLeft(content, '|')
    entry.delete(0, tk.END)
    entry.insert(0, jieguo)
    entry.config(state="disabled")


def validate_input(new_text):
    # 限制文本框中的字符数为26
    return len(new_text) <= 26


window = tk.Tk()
entry_width = 200

# 创建Entry部件，设置字体大小为20
entry = tk.Entry(window, font=("Arial", 100), width=entry_width, state="disabled", readonlybackground="white",
                 disabledforeground="black", insertofftime=1)
entry.pack(padx=10, pady=10)
vcmd = window.register(validate_input)

# 设置validatecommand
entry.config(validate="key", validatecommand=(vcmd, "%P"))
entry.config(state="normal")

# 插入默认字符
entry.insert(0, "|")
entry.config(state="disabled")

# 绑定键盘事件
entry.bind("<KeyRelease>", ensure_default_char)
# 设置窗口
window.resizable(False, False)
window.geometry('1600x900')
window.title('计算器')
window.overrideredirect(False)

# 创建计算器的按钮
button_plus = tk.Button(window, text='+', font=('华文楷体', 100), height=0, width=1,
                        fg='purple', command=lambda: on_button_click('+'))
button_plus.place(x=685, y=150)
button_plus.bind("<Enter>", on_enter)

button_minus = tk.Button(window, text='-', font=('华文楷体', 100), height=0, width=1,
                         fg='purple', command=lambda: on_button_click('-'))
button_minus.place(x=685, y=300)
button_minus.bind("<Enter>", on_enter)

button_multiply = tk.Button(window, text='*', font=('华文楷体', 100), height=0, width=1,
                            fg='purple', command=lambda: on_button_click('*'))
button_multiply.place(x=685, y=450)
button_multiply.bind("<Enter>", on_enter)

button_divide = tk.Button(window, text='/', font=('华文楷体', 100), height=0, width=1,
                          fg='purple', command=lambda: on_button_click('/'))
button_divide.place(x=685, y=600)
button_divide.bind("<Enter>", on_enter)

button_dot = tk.Button(window, text='.', font=('华文楷体', 100), height=0, width=1,
                       fg='purple', command=lambda: on_button_click('.'))
button_dot.place(x=685, y=750)
button_dot.bind("<Enter>", on_enter)

button_gen = tk.Button(window, text='√', font=('华文楷体', 50), height=2, width=2,
                       fg='#3715a1', command=ping_fang)
button_gen.place(x=1085, y=150)
button_gen.bind("<Enter>", on_enter)

button_pi = tk.Button(window, text='π', font=('华文楷体', 100), height=0, width=1,
                      fg='#3715a1', command=lambda: on_button_click('3.14159265358......'))
button_pi.place(x=985, y=150)
button_pi.bind("<Enter>", on_enter)

button_ping_fang = tk.Button(window, text='x²', font=('华文楷体', 50), height=2, width=2,
                             fg='#3715a1', command=ping_fang)
button_ping_fang.place(x=1185, y=150)
button_ping_fang.bind("<Enter>", on_enter)

button_li_fang = tk.Button(window, text='x³', font=('华文楷体', 50), height=2, width=2,
                           fg='#3715a1', command=li_fang)
button_li_fang.place(x=785, y=300)
button_li_fang.bind("<Enter>", on_enter)

button_li_fang_gen = tk.Button(window, text='³√', font=('华文楷体', 50), height=2, width=2,
                               fg='#3715a1', command=li_fang_gen)
button_li_fang_gen.place(x=885, y=300)
button_li_fang_gen.bind("<Enter>", on_enter)

button_zheng_chu = tk.Button(window, text='//', font=('华文楷体', 50), height=2, width=2,
                             fg='#3715a1', command=lambda: on_button_click('//'))
button_zheng_chu.place(x=985, y=300)
button_zheng_chu.bind("<Enter>", on_enter)

button_kuo_hao = tk.Button(window, text='(', font=('华文楷体', 50), height=2, width=2,
                           fg='#3715a1', command=lambda: on_button_click('('))
button_kuo_hao.place(x=1085, y=300)
button_kuo_hao.bind("<Enter>", on_enter)

button_kuo_hao2 = tk.Button(window, text=')', font=('华文楷体', 50), height=2, width=2,
                            fg='#3715a1', command=lambda: on_button_click(')'))
button_kuo_hao2.place(x=1185, y=300)
button_kuo_hao2.bind("<Enter>", on_enter)

button_z_y = tk.Button(window, text='%\n//', font=('华文楷体', 50), height=2, width=2,
                       fg='#3715a1', command=lambda: on_button_click('%//'))
button_z_y.place(x=785, y=450)
button_z_y.bind("<Enter>", on_enter)

button_yu_shu = tk.Button(window, text='%', font=('华文楷体', 100), height=0, width=1,
                          fg='#3715a1', command=lambda: on_button_click('%'))
button_yu_shu.place(x=885, y=450)
button_yu_shu.bind("<Enter>", on_enter)

button_ping_fang_gen = tk.Button(window, text='²√', font=('华文楷体', 50), height=2, width=2,
                                 fg='#3715a1', command=ping_fang_gen)
button_ping_fang_gen.place(x=885, y=450)
button_ping_fang_gen.bind("<Enter>", on_enter)

button_tan = tk.Button(window, text='tan', font=('华文楷体', 100), height=0, width=5,
                       fg='#3715a1', command=tan)
button_tan.place(x=985, y=450)
button_tan.bind("<Enter>", on_enter)

button_equal = tk.Button(window, text='=', font=('华文楷体', 100), height=0, width=1, fg='blue',
                         command=calculate_result)
button_equal.place(x=785, y=150)
button_equal.bind("<Enter>", on_enter)

button_clear = tk.Button(window, text='C', font=('华文楷体', 100), height=0, width=1, fg='red', command=clear_text)
button_clear.place(x=885, y=150)
button_clear.bind("<Enter>", on_enter)

button_zuo = tk.Button(window, text='←', font=('华文楷体', 100), height=2, width=3, fg='#3B3AB7',
                       command=move_left)
button_zuo.place(x=785, y=600)
button_zuo.bind("<Enter>", on_enter)

button_you = tk.Button(window, text='→', font=('华文楷体', 100), height=2, width=3, fg='#3B3AB7',
                       command=move_right)
button_you.place(x=1080, y=600)
button_you.bind("<Enter>", on_enter)

button_1 = tk.Button(window, text='1', font=('华文楷体', 200), command=lambda: on_button_click('1'), fg='#ef742d')
button_1.place(x=15, y=150)
button_1.bind("<Enter>", on_enter)

button_2 = tk.Button(window, text='2', font=('华文楷体', 200), command=lambda: on_button_click('2'), fg='#ef742d')
button_2.place(x=200, y=150)
button_2.bind("<Enter>", on_enter)

button_3 = tk.Button(window, text='3', font=('华文楷体', 200), command=lambda: on_button_click('3'), fg='#ef742d')
button_3.place(x=385, y=150)
button_3.bind("<Enter>", on_enter)

button_4 = tk.Button(window, text='4', font=('华文楷体', 200), command=lambda: on_button_click('4'), fg='#ef742d')
button_4.place(x=15, y=400)
button_4.bind("<Enter>", on_enter)

button_5 = tk.Button(window, text='5', font=('华文楷体', 200), command=lambda: on_button_click('5'), fg='#ef742d')
button_5.place(x=200, y=400)
button_5.bind("<Enter>", on_enter)

button_6 = tk.Button(window, text='6', font=('华文楷体', 200), command=lambda: on_button_click('6'), fg='#ef742d')
button_6.place(x=385, y=400)
button_6.bind("<Enter>", on_enter)

button_7 = tk.Button(window, text='7', font=('华文楷体', 200), command=lambda: on_button_click('7'), fg='#ef742d')
button_7.place(x=15, y=650)
button_7.bind("<Enter>", on_enter)

button_8 = tk.Button(window, text='8', font=('华文楷体', 200), command=lambda: on_button_click('8'), fg='#ef742d')
button_8.place(x=200, y=650)
button_clear.bind("<Enter>", on_enter)

button_9 = tk.Button(window, text='9', font=('华文楷体', 200), command=lambda: on_button_click('9'), fg='#ef742d')
button_9.place(x=385, y=650)
button_9.bind("<Enter>", on_enter)

button_0 = tk.Button(window, text='0', font=('华文楷体', 250), height=1, width=2, fg='#ef742d',
                     command=lambda: on_button_click('0'))
button_0.place(x=1300, y=150)
button_0.bind("<Enter>", on_enter)

button_delete = tk.Button(window, text='⌫', font=('华文楷体', 100), height=3, width=5, fg='#ff0032',
                          command=clear_text2)
button_delete.place(x=1300, y=546)
button_delete.bind("<Enter>", on_enter)

button_exit = tk.Button(window, text='退\n出\n计\n算\n器', font=('华文楷体', 100), height=7, width=2,
                        command=button_click)
button_exit.place(x=545, y=150)
button_exit.bind("<Enter>", on_enter)

# 绘制窗口
window.mainloop()
