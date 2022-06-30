#查找1000以内的质数
# 1.判断某个数字是否是质数
# 2.连续判断多个数字是否是质数
num = 17
i = 2
is_prime = True#标识当前数字是否为质数 True-是 False 不是
while i < num :
    if num % i == 0:
        is_prime = False
        break
    i = i +1
if is_prime == False:
    print("{}不是质数".format(num))
else:
    print("{}是质数".format(num))

