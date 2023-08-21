from tkinter import messagebox

# showinfo示例
messagebox.showinfo("提示", "这是一个信息对话框")

# showwarning示例
messagebox.showwarning("警告", "这是一个警告对话框")

# showerror示例
messagebox.showerror("错误", "这是一个错误对话框")

# askquestion示例
result = messagebox.askquestion("确认", '是否继续操作？')
if result == "yes":
    messagebox.showinfo("提示", "您选择了是")
else:
    messagebox.showinfo("提示", "您选择了否")

# askyesno示例
result = messagebox.askyesno("确认", "是否继续操作？")
if result:
    messagebox.showinfo("提示", "您选择了是")
else:
    messagebox.showinfo("提示", "您选择了否")

# askokcancel示例
result = messagebox.askokcancel("确认", "是否继续操作？")
if result:
    messagebox.showinfo("提示", "您选择了确定")
else:
    messagebox.showinfo("提示", "您选择了取消")
