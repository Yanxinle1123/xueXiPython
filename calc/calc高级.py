import re
import tkinter
import tkinter.messagebox

calc_main = tkinter.Tk()
calc_main.geometry('300x270+400+100')
# calc_main.configure(bg='gray')
calc_main.resizable(False, False)
calc_main.title("计算器")
btn_height = 30


def key_char(btn):
    get_content = content_var.get()
    if get_content.startswith('.'):
        get_content = '0' + get_content
    if btn in '0123456789':
        get_content += btn
    elif btn == '.':
        last_part = re.split(r'\+ | - | \* | /', get_content)[-1]
        if '.' in last_part:
            tkinter.messagebox.showerror('错误', '小数点重复出现')
            return
        else:
            get_content += btn

    elif btn == 'C':
        get_content = ''
    elif btn == '=':
        try:
            get_content = str(eval(get_content))
        except:
            tkinter.messagebox.showerror('错误', '算式有误')
            return

    elif btn in operators:
        if get_content.endswith(operators):
            tkinter.messagebox.showerror('错误', '不允许存在连续的运算符')
            return
        get_content += btn

    elif btn == 'Sqrt':
        n = get_content.split('.')
        if all(map(lambda x: x.isdigit(), n)):
            get_content = eval(get_content) ** 0.5
        else:
            tkinter.messagebox.showerror('错误', '无法开平方')
            return
    print('get_content', get_content)
    content_var.set(get_content)


content_var = tkinter.StringVar(calc_main, '')
content_input = tkinter.Entry(calc_main, textvariable=content_var)
content_input['state'] = 'readonly'
content_input.place(x=10, y=10, width=280, height=btn_height)

btn_clear = tkinter.Button(calc_main, text='C', bg='red', command=lambda: key_char('C'))
btn_clear.place(x=40, y=40, width=80, height=btn_height)

btn_equal = tkinter.Button(calc_main, text='=', bg='blue', command=lambda: key_char('='))
btn_equal.place(x=170, y=40, width=80, height=btn_height)

digits = list('0123456789.') + ['Sqrt']
index = 0
for row in range(4):
    for col in range(3):
        d = digits[index]
        index += 1
        btn_digit = tkinter.Button(calc_main, text=d, bg='yellow', command=lambda x=d: key_char(x))
        btn_digit.place(x=20 + col * 70, y=80 + row * 50, width=50, height=btn_height)

operators = ('+', '-', '*', '/', '**', '//')
for index, operator in enumerate(operators):
    btn_opers = tkinter.Button(calc_main, text=operator, bg='pink', command=lambda x=operator: key_char(x))
    btn_opers.place(x=230, y=80 + index * 30, width=50, height=btn_height)

calc_main.mainloop()
