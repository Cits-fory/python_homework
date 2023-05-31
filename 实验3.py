# coding=gbk
'''
Cits-fory
'''

# # 1���Զ�����ģ����ά�����������㡣
# class Array:
#     def __init__(self,x,y,z):
#         self.__x = x
#         self.__y = y
#         self.__z = z
#     def add(self,b):
#         self.__x+=b.__x
#         self.__y+=b.__y
#         self.__z+=b.__z
#     def sub(self,b):
#         self.__x-=b.__x
#         self.__y-=b.__y
#         self.__z-=b.__z
#     def mul(self,b:int):
#         self.__x *= b
#         self.__y *= b
#         self.__z *= b
#     def div(self,b:int):
#         if b == 0:
#             print("��������Ϊ0��")
#             return
#         self.__x /= b
#         self.__y /= b
#         self.__z /= b
#     def print(self):
#         print("Array = {},{}.{}".format(self.__x,self.__y,self.__z))
#
# a1 = Array(1,2,3)
# a2 = Array(1,3,2)
# a1.add(a2)
# a1.print()
# a1.sub(a2)
# a1.print()
# a1.div(2)
# a1.print()
# a1.mul(3)
# a1.print()



# # 2����дһ��ѧ���ͽ�ʦ�����������ʾ�������У�ѧ�������б�š��������༶�ͳɼ���
# #    ��ʦ�����б�š�������ְ�ƺͲ��š�Ҫ��
# # ��1������š������������ʾ��Ƴ�һ����person��
# # ��2�������person�������ࣺѧ����student�ͽ�ʦ��teacher��
# class person:
#     def __init__(self):
#         self.num  = int(input("���������ı�ţ�"))
#         self.name = input("�������������֣�")
#     def show(self):
#         print(f"    ���      ����")
#         print(f"{self.num:>10}{self.name:>5}")
#
# class student(person):
#     def __init__(self,Class,score):
#         super(student, self).__init__()
#         self.__Class = Class
#         self.__score = score
#     def show(self):
#         print(f"    ���      ����      �༶       �ɼ�")
#         print(f"{self.num:>10}{self.name:>5}{self.__Class:>12}{self.__score:>6}")
#
# class teacher(person):
#     def __init__(self,professor,department ):
#         super(teacher, self).__init__()
#         self.__professor = professor
#         self.__department = department
#     def show(self):
#         print(f"    ���      ����      ְ��     ����")
#         print(f"{self.num:>10}{self.name:>5}{self.__professor:>8}{self.__department:>8}")
# # 2020212748 ���ٶ�
# a = student("08052001",100)
# a.show()
#
# # 2020212748 �ϳ�
# b = teacher("��ʦ","�Զ���")
# b.show()

# # 3������һ��Ա����Employee�������ݳ�Ա��������š�
# # ����һ������Ա�̳���Ա����Sales������Ϊ���۶�����10%��
# # ����һ��������Manager���̶�����8000��
# # ����һ�����۾����࣬�̳�������Ա��;����࣬����Ϊ�̶�����5000�����۶�����5%��
# # ÿ�������display���������Ϣ����д���������ԡ�
# class Employee:
#     def __init__(self,name,num):
#         self.name = name
#         self.num = num
#     def display(self):
#         print("��Ա������{}����ţ�{}".format(self.name,self.num))
# class Sales(Employee):
#     def __init__(self,name,num,salary):
#         super(Sales, self).__init__(name,num)
#         self.salary = salary
#         self.__pay = self.salary*0.1
#     def display(self):
#         print("��Ա������{}����ţ�{},���ʣ�{}".format(self.name,self.num,self.__pay))
# class Manager(Employee):
#     def __init__(self,name,num):
#         super(Manager, self).__init__(name,num)
#         self.__pay = 8000
#     def display(self):
#         print("��Ա������{}����ţ�{},���ʣ�{}".format(self.name,self.num,self.__pay))
# class Sale_Manager(Sales,Manager):
#     def __init__(self,name,num,salary):
#         super(Sale_Manager, self).__init__(name,num,salary)
#         self.__pay = 5000 + self.salary*0.05
#     def display(self):
#         print("��Ա������{}����ţ�{},���ʣ�{}".format(self.name,self.num,self.__pay))
#
# a = Sales("��","1",10000)
# a.display()
# b = Manager("��","2")
# b.display()
# c = Sale_Manager("��","3",10000)
# c.display()

# # 4����дһ������������Բ����Բ׶�ı�����������Ҫ��
# # 1������һ�����࣬���ٺ���һ�����ݳ�Ա�뾶������Ϊ˽�г�Ա��
# # 2������������������Բ����Բ׶��������������������ĳ�Ա�����ʹ�ӡ������
# # 3����д������������Բ����Բ׶�ı�����������
# from math import *
# class base:
#     def __init__(self,r):
#         self.__r = r
#     def get_r(self):
#         return self.__r
# class ball(base):
#     def __init__(self, r):
#         super(ball, self).__init__(r)
#     def display(self):
#         print("���r="+ str(self.get_r()))
#     def cal_S(self):
#         r = self.get_r()
#         print("��ı����Ϊ��" + str(4*pi*r*r))
#     def cal_V(self):
#         r = self.get_r()
#         print("������Ϊ��" + str(4*pi*r*r*r/3.0))
#
# class cone(base):
#     def __init__(self, r,h):
#         super(cone, self).__init__(r)
#         self.h = h
#     def display(self):
#         print("Բ����r={},h={}".format(self.get_r(),self.h))
#     def cal_S(self):
#         r = self.get_r()
#         print("Բ���ı����Ϊ��" + str(2*pi*r*(r+self.h)))
#     def cal_V(self):
#         r = self.get_r()
#         print("Բ�������Ϊ��" + str(pi*r*r*self.h))
# class cylinder(base):
#     def __init__(self, r,h):
#         super(cylinder, self).__init__(r)
#         self.h = h
#         self.l = sqrt(r*r + self.h*self.h)
#     def display(self):
#         print("Բ׶��r={},h={},l={:.3}".format(self.get_r(),self.h,self.l))
#     def cal_S(self):
#         r = self.get_r()
#         l = self.l
#         print("Բ׶�ı����Ϊ��" + str(pi*r*r+pi*r*l))
#     def cal_V(self):
#         print("Բ׶�����Ϊ��" + str(pi*self.get_r()*self.get_r()*self.h/3.0))
# list = [ball(10),cone(5,10),cylinder(5,10)]
# for i in list:
#     i.display()
#     i.cal_S()
#     i.cal_V()


# # 5������������������ͥסַ����������������Ϣ�����Զ����ƽ����ļ���д��
# import random,string,struct
#
# def random_data():
#     def random_sex():
#         sex = '��Ů'
#         return random.choice(sex)
#     def random_address():
#         address = ['������������', '������������', '�����д�ɿ���', '�������山��', '�����а�����', '������ƽ����', '��������ƽ��', '��������ɽ��', '�����е潭��']
#         return random.choice(address)
#     def random_mail():
#         last_l = ['@qq.com','@gmail.com','@163.com','@126.com','@stu.cqupt.edu.cn']
#         num = ''.join([random.choice(string.digits) for i in string.digits])
#         last = str(random.choice(last_l))
#         return  num + last
#     sex = random_sex()
#     mail = random_mail()
#     firstname = list('��Ǯ��������֣���������������������������ʩ�ſײ��ϻ���κ�ս���л������ˮ��������˸��ɷ�����')
#     boy_name = "���� ��Ԫ Ң�� ���� �⿬ ���� � ���� ��Ң �ڻ� ��Ԫ ���� ʥ� ���� �ȿ� ���� ���� ���� ���� ���� ־ǿ ���� ��ƽ ���� ���� ����".split()
#     girl_name = '�� �껪 �� ���� �Ⱦ� �� ϼ�� �� ݺ �� ���� �� �Ѽ� �� ���� ���� ��� Ҷ �� � ���� ���� ɺɯ �� ϣ�� �� Ʈ�� �� �'.split()
#     if sex == '��':
#         name = random.choice(firstname) + random.choice(boy_name)
#     else:
#         name = random.choice(firstname) + random.choice(girl_name)
#     address = random_address()
#     return sex,name,address,mail
# n = int(input("��������Ҫ������ɵ���Ϣ������"))
# headline = "�Ա�   ����      ��ַ             ����"
# print(headline)
# data_list = [headline]
# for i in range(n):
#     sex,name,address,mail = random_data()
#     data = "{:>2}  {:>4} {:>8} {}".format(sex,name,address,mail)
#     data_list.append(data)
#     print(data)
#
# with open("data.bin","wb") as file:
#     file.write(str(data_list).encode())
# with open("data.bin","rb") as file:
#     data = file.read().decode().split(",")
#     print(data)

# # 6����д�ı��ļ��������кš�
# path = input("�������ı��ļ�������·��(��C:\\Users\\1.txt):")
# data_after = ''
# try:
#     with open(path,"r",encoding="utf-8") as f:
#         i = 1
#         for data in f.readlines():
#             data_after += "{:>2}:  {}".format(i,data)
#             i += 1
#     print(data_after)
#     with open(path,"w") as f:
#         f.write(data_after)
# except FileNotFoundError:
#     print("ע������������·����")

# # # 7��ʵ���ļ����������������ȱ�������ɸѡ��ĳ�����ڵ�����.txt�ļ���
# # # ��ӡȫ·���ļ������������ļ������̽������򣬲��������ַ�������ͬ�㡣
# from os import *
# from os.path import isfile,isdir
# import time
#
# # ����ȡ·�������ļ���[-1],Ȼ��ȥ��׺.txt��[0],֮�����������ؾ���
# def sort_txt(txt_list):
#     list = [item.split("\\")[-1].split(".")[0] for item in txt_list]
#     id1 = sorted(range(len(list)), key=lambda x: len(list[x]))
#     return [txt_list[i] for i in id1]
#
# # �����������������Ŀ¼����
# def listDirDepthFirs(path):
#     txt_path = []
#     try:
#         for subPath in listdir(path):
#             path_new = path + "\\" + subPath
#             if isfile(path_new):
#                 if path_new[-4:] == '.txt':
#                     txt_path.append(path_new)
#             elif isdir(path_new):
#                 list = listDirDepthFirs(path_new)
#                 if list != []:
#                     for item in list:
#                         txt_path.append(item)
#     except:
#         pass
#     return txt_path
#
# # ������������������ļ��б��ȴ������е�ǰĿ¼���ļ��У�һ����ȥ������������ѹջ
# def listDirWidthFirst(path):
#     dirs = [path]
#     txt_path = []
#     while dirs:
#         current = dirs.pop(0)
#         try:
#             for subPath in listdir(current):
#                 path_new = current + "\\" + subPath
#                 if isfile(path_new):
#                     if path_new[-4:] == '.txt':
#                         txt_path.append(path_new)
#                 elif isdir(path_new):
#                     dirs.append(path_new)
#         except:
#             pass
#     return txt_path
#
# path = input("��������Ҫ��������(����C:\):")
# print("��ʼ��������Ŀ¼��~")
# print("-----------�����������---------------")
# start1 = time.perf_counter()
# for item in sort_txt(listDirDepthFirs(path)):
#     print(item)
# end1 = time.perf_counter()
# start2 = time.perf_counter()
# print("-----------�����������---------------")
# for item in sort_txt(listDirWidthFirst(path)):
#     print(item)
# end2 = time.perf_counter()
# print("------------������ʱ---------------")
# print("�������������{}".format(end1 - start1))
# print("�������������{}".format(end2 - start2))

