import re
import tkinter
import tkinter.messagebox

Control = tkinter.Tk()
Control.geometry('300x270+400+100')
Control.resizable(False, False)
Control.title("计算器")


def Key(btn):
    Get_content = contentVar.get()
    if Get_content.startswith('.'):
        Get_content = '0' + Get_content
        if btn in '0123456789':
            Get_content += btn
        elif btn == '.':
            lastPart = re.split(r'\+ | - | \* | /', Get_content)[-1]
            if '.' in lastPart:
                tkinter.messagebox.showerror('错误', '小数点重复出现')
                return
            else:
                Get_content += btn
        elif btn == 'C':
            Get_content = ''
        elif btn == '=':
            try:
                Get_content = str(eval(Get_content))

            except:
                tkinter.messagebox.showerror('错误', '算式有误')

                return
        elif btn in operators:
            if Get_content.endswith(operators):
                tkinter.cessagebox.showerror('错误', '不允许存在连续的运算符')
                return
            Get_content += btn
        elif btn == 'Sqrt':
            n = Get_content.split('.')
            if all(map(lambda x: x.isdigit(), n)):
                Get_content = eval(Get_content) ** 0.5

            else:
                tkinter.messagebox.showerror('错误', '无法开平方')

                return
        contentVar.set(Get_content)


contentVar = tkinter.StringVar(Control, '')
contentEntry = tkinter.Entry(Control, textvariable=contentVar)
contentEntry['state'] = 'readonly'
contentEntry.place(x=10, y=10, width=280, height=20)

btnClear = tkinter.Button(Control, text='C', bg='orange', command=lambda: Key('C'))
btnClear.place(x=40, y=40, width=80, height=20)

btnComputer = tkinter.Button(Control, text='=', bg='purple', command=lambda: Key('='))
btnComputer.place(x=170, y=40, width=80, height=20)

digits = list('0123456789.') + ['Sqrt']
index = 0
for row in range(4):
    for col in range(3):
        d = digits[index]
        index += 1
        btnDigit = tkinter.Button(Control, text=d, bg='blue', command=lambda x=d: Key(x))

        btnDigit.place(x=20 + col * 70, y=80 + row * 50, width=50, height=20)

operators = ('+', '-', '*', '/', '**', '//')
for index, operator in enumerate(operators):
    btnOperator = tkinter.Button(Control, text=operator, bg='green', command=lambda x=operator: Key(x))
    btnOperator.place(x=230, y=80 + index * 30, width=50, height=20)
Control.mainloop()
