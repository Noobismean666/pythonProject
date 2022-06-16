#综合训练-血压苹果
high = input("请输入您测量的高压值")
low = input("请输入您测量的低压值")
high = int(high)
low = int(low)
'''
if (low>60 and low <90) and (high > 90 and high <140):
    print("您的血压正常，请继续保持健康的生活习惯")
else:
    print("您的血压出现异常，请尽快就医")
'''
if not ((low <= 60 or low >=90) or (high >= 140 or high <=90)):
    print("您的血压正常，请继续保持健康的生活习惯")
else:
    print("的血压出现异常，请尽快就医")

#判断水仙花数
num = int(input("请输入一个三位数:"))
# 分别求出三位数的个位，十位，百位
gw = num // 100
sw = (num // 10)%10
bw = num % 10
# 定义变量total，保存各位数字立方和
total = (gw*gw*gw) + (sw*sw*sw) + (bw*bw*bw)
# 用if语句判断条件是否成立，并做出相应的输出
if (total==num):

    print("是水仙花数")

else:

    print("不是水仙花数")

