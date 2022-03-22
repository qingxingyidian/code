import tkinter as tk
import tkinter.messagebox as tk_mbx
import achievement_analysis as ats

root = tk.Tk()     #创建窗体

l1 = tk.Label(root, text="请输入科目名称")
l1.pack()

e2 = tk.Entry(root)  #创建输入科目名的输入框
e2.pack()

#判断输入的科目是否存在
def get():
    suject_name = e2.get()
    if ats.suject_name(suject_name):
        ats.show_class_suject_score(suject_name)
    else:
       tk_mbx.showerror(message="没有这个内容，请重新输入!") 


b1 = tk.Button(root, text="提交", command=get)
b1.pack()

tk.mainloop()
