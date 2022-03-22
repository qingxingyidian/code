import tkinter as tk
import tkinter.messagebox as tk_mbx
import achievement_analysis as ats

top = tk.Tk()  # 创建窗口实例
top.geometry("330x30")  # 设置窗体宽为400，高为50

l1 = tk.Label(top, text="请输入学生姓名:")
l1.place(relx=0, rely=0.1)
e1 = tk.Entry(top)  # 创建单行文本框
e1.place(relx=0.3, rely=0.15)


def get():  # get函数将返回输入框的内容
    name = e1.get()
    if ats.student_name(name):       #判断是否存在输入的名称
        ats.show_student_score(name)
    else:
        tk_mbx.showerror(message="没有这个同学，请重新输入")


b1 = tk.Button(top, text="提交", height="1", command=get)  # 创建按钮实例
b1.place(relx=0.8, rely=0)

top.mainloop()  # 进入消息循环
