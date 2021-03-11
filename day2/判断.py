score = input("请录入分数：")
score = int(score)
if score >=90 and score<=100:
    print("优秀")
elif score>=80 and score<90:
    print("良好")
elif score >=70 and score<80:
    print("还可以")
elif score>=60 and score<70:
    print("危！")
elif score>0 and score<60:
    print("你完了")
else:
    print("输入非法")