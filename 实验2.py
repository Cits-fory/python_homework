'''
Cits-fory
'''
# # 1、输入小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数
# try:
#     height, weight = map(float, input("请输入身高和体重，用空格分隔:").split())
#     bmi = weight / (height/100)**2
#     level = zip(["过轻", "正常", "过重", "肥胖"], [18.5, 25, 28, 32])
#     # 生成器表达式
#     print("BMI为：" + str(bmi))
#     print(next((lev for lev,limits in level if bmi <= limits), "严重肥胖"))
# except ValueError:
#     print("请注意用空格分隔数据！")

# # 2、输入两个整数，打印他们相除后的结果，若输入的不是整数或除数为0，进行异常处理。
# try:
#     a, b = map(str,input("请输入两整数a/b，用空格分隔:").split())
#     assert float(a) - int(float(a)) == 0,"请检查第一个数是否为整数！"
#     assert float(b) - int(float(b)) == 0,"请检查第二个数是否为整数！"
#     assert int(float(b)) != 0,"被除数不能为0！"
#     print("a/b = " + str(int(float(a))/int(float(b))))
# except ValueError:
#     print("请注意用空格分隔数据！")

# # 3、使用蒙特·卡罗方法计算圆周率近似值
# import random
# def calpi():
#     time = 10000
#     r = 1.0
#     center_x,center_y = (0.0,0.0)
#     count = 0
#     for i in range(0,time):
#         x = random.uniform(center_x-r,center_x+r)
#         y = random.uniform(center_y-r,center_y+r)
#         if x*x + y*y <= 1.0:
#             count+=1
#     return 4*float(count/time)
# print(calpi())

# 4、使用枚举法验证6174猜想。
def guess_6174(number):
    i = 0
    while int(''.join(number)) != 6174:
        if len(number)<4:
            number.append("0")
        max = sorted(number, reverse=True)
        min = sorted(number)
        number = int(''.join(max)) - int(''.join(min))
        i += 1
        number = list(str(number))
        assert i <= 7,"6174猜想不成立"
    return i
# for number in range(1000,10000):
#     number = str(number)
#     # 筛去四个数字一样的
#     if len(set(number))>1:
#         print(number + "需要" + str(guess_6174(number)) + "次")
guess_6174("1000")
print("6174猜想成立！")
# # 5、模拟报数游戏（约瑟夫环问题）
# # 有n个人围成一圈，从1开始按顺序编号，从第一个人开始从1到k报数，报到k的人退出圈子；
# # 然后圈子缩小，从下一个人继续游戏，问最后留下的是第几号（只留1人）
# def findlastone(n,k):
#     group = list(range(1,n+1))
#     count = k-1
#     while len(group) > 1:
#         count = count % len(group)
#         group.pop(count)
#         count += k
#     return group[0]
# try:
#     n, k = map(int,input("请输入n和k，用空格分隔:").split())
#     print("最后剩下的为：" + str(findlastone(n,k)) + "号")
# except ValueError:
#     print("请注意用空格分隔数据！")

# # 6、模拟轮盘抽奖游戏
# import random
# print("本程序可以运行多次来抽奖！")
# # 概率对应为0.1 0.2 0.4 0.3
# reward = lambda x:["一等奖", "二等奖", "二等奖",
#                    "三等奖", "三等奖", "三等奖", "三等奖",
#                    "未中奖", "未中奖", "未中奖"][int(x*100)//10]
# print(reward(random.uniform(0,1)))

# # 7、一年365天，如果好好学习时能力值比前一天提高1%，
# # 当放任时相比前一天下降1%，编程计算两种情况效果相差值。
# try:
#     power = float(input("请输入初始能力值："))
#     power_down  = power
#     power_up = power
#     for i in range(365):
#         power_up *= 1.01
#         power_down *= 0.99
#     print(power * (1.01**365))
#     print("一直学习能力值为："+  str (power_up) )
#     print("一直放任能力值为："+  str (power_down) )
#     print("差值为：" + str (power_up -power_down ))
# except Exception as error:
#     print(error)


# # 8、凯撒加密算法原理与实现。
# from string import ascii_lowercase, ascii_uppercase
# try:
#     key,str = map(str,input("请输入密钥和要加密的字符串（用英文逗号隔开）：").split(","))
#     str_after = []
#     for i in str:
#         if i in ascii_lowercase:
#             str_after.append(ascii_lowercase[(ascii_lowercase.index(i) +
#             int(key))%len(ascii_lowercase)])
#         elif i in ascii_uppercase:
#             str_after.append(ascii_uppercase[(ascii_uppercase.index(i) +
#             int(key))%len(ascii_uppercase)])
#         else:
#             str_after.append(i)
#     print("加密的密钥为：" + key)
#     print("加密前的数据为：" + str)
#     print("加密后的数据为：" + ''.join(str_after))
# except ValueError:
#     print("请注意数据格式输入！")




