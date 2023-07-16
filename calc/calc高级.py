import tkinter

Control = tkinter.Tk()
Control.geometry('300x270+400+100')
Control.resizeable(False, False)
Control.title("计算器")

contentVar = tkinter.StringVar(Control, '')


def Key(btn):
    Get_content = contentVar.get()
