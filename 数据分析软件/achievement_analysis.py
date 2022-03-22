import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]        #解决中文乱码
plt.rcParams.update({'font.size': 8})      #设置字体大小

sheet_df = pd.read_excel("成绩数据/考试.xlsx", sheet_name=None)       #读取成绩数据
for i in sheet_df.keys():           #对数据进行处理，过滤掉不必要的信息
    sheet_df[i] = sheet_df[i].set_index(["姓名"])
    sheet_df[i] = sheet_df[i].loc[ : , [i for i in sheet_df[i].columns if "学号" not in i and "序号" not in i and "总分" not in i]]
    sheet_df[i].columns = [k.upper() for k in sheet_df[i].columns]
    sheet_df[i].replace({"A" : 50, "B" : 40, "C" : 30, "D" : 20}, inplace=True)
    sheet_df[i].fillna(0)       #将Nan值填充为零

student_name_set = set()       #创建存储所有学生姓名的集合
for df in sheet_df.values():
    for name in df.index:
        student_name_set.add(name)
suject_name_set = set()        #创建存储所有科目名称的集合
for df in sheet_df.values():
    for name in df.columns:
        suject_name_set.add(name)

def student_name(name):        #判断是否存在输入的姓名
    if name in student_name_set:
        return True
    else:
        return False


def suject_name(name):      #判断是否存在输入的科目名
    name = name.upper()
    if name in suject_name_set:
        return True
    else:
        return False


def show_student_score(name):     #绘制当前学生的各个科目在各个考试中的成绩趋势折线图
    df = pd.DataFrame({i : sheet_df[i].loc[name] for i in sheet_df.keys()})
    for i in df.index:
        plt.plot(df.columns, df.loc[i])
    plt.ylim(0, 100)    #设置成绩的取值范围为0-100
    plt.xlabel("考试名称")
    plt.legend(df.index, frameon=False, bbox_to_anchor=(-0.02, 1))  #绘制图例
    plt.title("%s同学的各学期各学科成绩趋势图" % (name))
    plt.show()          #显示绘制的图像
  

def show_class_suject_score(name):
    name = name.upper()
    flag = 1
    if name in ["语文", "数学", "英语"]:
        flag = 2
    score = [0 for i in range(5)]
    for i in sheet_df.values():
        if name in i.columns:
            for j in i[name]:
                if j * 2 >= 90:
                    score[0] += 1
                elif j * 2 >= 80:
                    score[1] += 1
                elif j * 2 >= 70:
                    score[2] += 1
                elif j * 2 >= 60:
                    score[3] += 1
                else:
                    score[4] += 1
    plt.pie(x=score, labels=["90-100", "80-89", "70-79", "60-69", "0-59"], autopct="%1.1f%%")
    plt.title("20网管班级%s成绩分布" % (name))
    plt.show()

if __name__ == "__main__":
    show_class_suject_score("ps")
