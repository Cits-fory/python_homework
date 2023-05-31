'''
Cits-fory1
'''
# # 1、编写一个猜年龄的小游戏；
# import random
# def guess_game(guess):
#     guess_temp = int(float(input("猜猜多少岁：")))
#     if guess_temp == guess:
#         print("猜对了！")
#         return 0
#     if guess_temp//2 > guess:
#         print("太大了！！除个二再猜")
#     elif 2*guess_temp < guess:
#         print("太小了！！乘个二再猜")
#     elif guess_temp < guess:
#         print("小了！！")
#     elif guess_temp > guess:
#         print("大了！！")
#     return 1
# guess = random.randint(1,150) # 随机生成待猜测的年龄2
# while guess_game(guess):
#     pass



# # 2、输入直角三角形两直角边a,b，求斜边C,并输出。(from math import *)；
# import math
# try:
#     a, b = map(float, input("请输入三角形两直角边，用空格分隔:").split())
#     if a > 0 and b > 0:
#         c = math.sqrt(a ** 2 + b ** 2)
#         print("该三角形斜边长为：{}".format(c))
#     else:
#         print("请检查输入数据！")
# except ValueError:
#     print("请注意用空格分隔数据！")



# # 3、编写程序，输入球的半径，计算球的表面积和体积，半径为实数，
# #    用π，结果输出为浮点数，共10位小数，保留2位小数。
# from math import *
# r = float(input("请输入球的半径："))
# s = 4*pi*r*r
# v = 4/3*pi*r**3
# print("球的表面积为：%.2f 体积为：%.2f" %(s,v))



# 4、实用列表实现筛选法求素数。
# n=int(input("请输入所求素数上限："))
# l=[]
# for i in range(2,n):
#     for x in l:
#         if i%x==0:
#             break
#     else:
#         l.append(i)
# print(l)

# # 5、使用集合实现筛选法求素数。
# N = int(input('请输入一个大于2的自然数：'))
# primes = set(range(2,N))
#
# n = int(N**0.5)+1
# m = [p for p in range(2,n) if 0 not in [p%d for d in range(2,int(p**0.5)+1)]]
# for p in m:
#     for i in range(2,N//p+1):
#         primes.discard(i*p)
# print(primes)



# 6、检测密码安全强度。
# 请用控制台运行，getpass函数在ide内可能不起作用
from getpass import *
from string import digits, ascii_lowercase, ascii_uppercase
pwd_strength = {"0":"拜托你很弱耶","1":"有点弱，改改吧",
                "2":"正常强度，按时更改比较好","3":"比较安全",
                "4":"挺强的,这你咋记住的","5":"最强，佩服佩服",}
pwd_type = [digits,ascii_lowercase,ascii_uppercase,',.!;?<>']

password  = getpass("请输入需要检测的密码：")
# 图灵测试hhh，防止你乱打
print(password)
while password != getpass("请再输入一次需要检测的密码："):
    print(password)
    pass
pwd_level = 1 # 基本强度
if len(password)<8:
    pwd_level = pwd_level-1
n = [type for type in pwd_type for ch in password if ch in type]
# 利用集合不允许重复元素的特性
pwd_level = pwd_level+len(set(n))
print("[{}]:{}".format(pwd_level/5,pwd_strength.get(str(pwd_level))))



# # 7、文本进度条：编程通过格式化字符串输出和时间延迟实现控制台风格文本进度条。
# import time
# scale = 60
# # 获得现在的时间
# start = time.perf_counter()
# print("     " + "starting".center(scale,'-'))
# for i in range(scale+1):
#     run_already = '█'*i
#     run_after = '-'*(scale - i)
#     run_percent = (i/scale)*100
#     dur_time = time.perf_counter() - start
#     print("\r{:3.0f}%[{}{}] total：{:.2f}s".format(run_percent,run_already,run_after,dur_time),end="")
#     time.sleep(0.05) # 稍稍延时一下，
# print("\n"+"     " +"ending".center(scale,'-'))
