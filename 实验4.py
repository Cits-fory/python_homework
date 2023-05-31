# # coding=gbk
'''
Cits-fory
'''
# # 1��ʹ��matplotlib����ͼ�λ��ơ�ͼ�β�������ͼ��ʾ��
# # ÿ����ͼ��Ҫ��ע�������ǩ��ͼ�α��⣬ͬʱ��ÿ����ͼ�����ò�ͬ����ɫ���������ȡ�
# import matplotlib.gridspec as gridspec
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(-5,5,100)
# y1 = 2*x+5
# y2 = 0.5*x*x+1
# y3 = x**3+5
# plt.figure(figsize=(7, 7))
# G = gridspec.GridSpec(2, 2)
# f1 = plt.subplot(G[0, :])
# f1.set_xlabel('x1')
# f1.set_ylabel('y1')
# f1.set_title('y1 = 2*x+5')
# f1.plot(x, y1 ,color='green', linewidth=1.0)
# f2 = plt.subplot(G[1,0])
# f2.set_title('y2 = 0.5*x^2+1')
# f2.set_xlabel('x2')
# f2.set_ylabel('y2')
# f2.plot(x, y2,color='purple', linewidth=5.0)
# f3 = plt.subplot(G[1:,1])
# f3.set_title('y3 = x^3+5')
# f3.set_xlabel('x3')
# f3.set_ylabel('y3')
# f3.plot(x, y3, color='red', linewidth=10.0)
#
# plt.show()


# # 2��(1)������pandas��matplotlib�ȹ��߻������۽����ʱ�������ͼ��
# #   ��2���������۽��ֲ�ֱ��ͼ��
# #   ��3����ȡ���۽�����ֵ��ƽ��ֵ�����ƫ�ȡ���ȵ�����ֵ����ӡ�����
# import matplotlib.pyplot as plt
# import pandas as pd
# data = pd.read_excel('Question_1_data.xls',sheet_name="Sheet1")
# date = data.set_index('��������')
# date.index = pd.to_datetime(date.index)
# plt.figure(figsize = (10, 4), dpi = 100)
# plt.title("���۽����ʱ�������ͼ",fontname="SimHei")
# plt.plot(date.loc[:,'�������'])
# plt.show()
# plt.hist(data.loc[:,'�������'], bins=40, density=False, facecolor="tab:orange", edgecolor="tab:red", alpha=0.7)
# plt.title("���۽��ֲ�ֱ��ͼ",fontname="SimHei")
# plt.show()
# max_data = data['�������'].max()
# mean_data = data['�������'].mean()
# var_data =  data['�������'].var()
# skew_data = data['�������'].skew()
# kurtosis_data = data['�������'].kurtosis()
# print("���۽�����ֵ = {}��ƽ��ֵ = {}������ = {}\nƫ�� = {}����� = {}"
#       .format(max_data,mean_data,var_data,skew_data,kurtosis_data))


# # 3����sqlite3���ݿ⡰Student.db���У��½�һ����Ϊ��userinfo���ı���
# # ���������¼�¼�󣬽������Email�޸ĸ���ΪWangwu@163.com�󣬽����еļ�¼��ӡ�����
# import sqlite3
# conn = sqlite3.connect('Student.db')
# cs = conn.cursor()
# try:
#     cs.execute("CREATE TABLE userinfo(StuNumber text, Name text, ClassNumber text, Email text)")
# except sqlite3.OperationalError:
#     print("�ñ��Ѵ��ڣ������´�����")
#     pass
# cs.execute("INSERT INTO userinfo VALUES(20190001, '����', 'C01', 'Zhangsan@163.com')")
# cs.execute("INSERT INTO userinfo VALUES(20190002, '����', 'C02', 'Lisi@163.com')")
# cs.execute("INSERT INTO userinfo VALUES(20190003, '����', 'C03', 'Wangwu@qq.com')")
# cs.execute("INSERT INTO userinfo VALUES(20190004, 'С��', 'C04', 'Xiaoming@qq.com')")
# conn.commit()
# cs.execute("UPDATE  userinfo SET Email = 'Zhangsan@163.com' where Name = '����'")
# cs.execute('SELECT * FROM userinfo')
# rows = cs.fetchall()
# for row in rows:
#     print(row)

# # 4��ʹ��KNN�����㷨ʵ�ָ������ߺ����ض����ͷ��ࡣ
# import numpy as np
# import matplotlib.pyplot as plt
# from collections import Counter
#
# data = np.array([[183,92],[183,84],[183,104],[180,88],[159,52],[156,48],[177,84],[165,68],[159,60],[156,56],
#                  [171,76],[156,68],[174,72],[171,88],[165,80],[177,76],[171,68],[173,92],[165,60],[177,96]])
# result = np.array(['����','ƫ��','̫��','����','ƫ��','ƫ��','����','����','����','����','����',
#                    '̫��','ƫ��','̫��','̫��','ƫ��','ƫ��','̫��','ƫ��','̫��'])
# def data_pocess(x,y,data):
#     gp = [[x[i],y[i]] for i in range(len(data)) if data[i] == "̫��"]
#     zc = [[x[i],y[i]] for i in range(len(data)) if data[i] == "����"]
#     ps = [[x[i],y[i]] for i in range(len(data)) if data[i] == "ƫ��"]
#     return gp,zc,ps
#
# def knn_classify(X, y, test, k):
#     def bmi(X):
#         return [(x[1] / (x[0] / 100) ** 2) for x in X]
#     dists = [np.sqrt(np.sum((x - bmi([test])[0]) ** 2)) for x in bmi(X)]
#     idx_knn = np.argsort(dists)[:k]
#     y_knn = y[idx_knn]
#     return Counter(y_knn).most_common(1)[0][0]
#
# data_train = data[:15]
# result_train = result[:15]
# data_test = data[15:]
# result_test = result[15:]
#
# predictions = [knn_classify(data_train, result_train, da, 3) for da in data_test]
# correct = np.count_nonzero((predictions==result_test)==True)
# print(result_test)
# print(predictions)
# print ("��ȷ��: %.3f" %(correct/len(data_test)))
# gp,zc,ps = data_pocess(data_test,result_test,predictions)
# plt.figure(figsize = (5, 4), dpi = 100)
# plt.xlabel("����",fontname="SimHei")
# plt.ylabel("����",fontname="SimHei")
# for d in gp:
#     plt.plot(d[0][0],d[0][1],".",color="r")
# for d in zc:
#     plt.plot(d[0][0],d[0][1],".",color="y")
# for d in ps:
#     plt.plot(d[0][0],d[0][1],".",color="k")
# plt.show()

# 5��ʹ��k-means�����㷨���з��ࡣ
import random
import numpy as np
import matplotlib.pyplot as plt

def count_dist(x,y):
    result = 0
    for i in range(len(x)):
        try:
            result+=(x[i]-y[i])**2
        except:
            print(i,x,y)
    return result**0.5
def get_centerPoint(arr):
    arr = np.array(arr)
    if len(arr) != 0:
        return [(sum(arr[:, i]) / len(arr[:, i])) for i in range(len(arr[0, :]))]
    return []

def k_means(init_points,data):
    arr = [[] for i in range(k)]
    for i in range(len(data)):
        item_arr = []
        for i2 in range(k):
            if len(init_points[i2]) != 0:
                item_arr.append(count_dist(data[i], init_points[i2]))
        min_dist = min(item_arr)
        for i3 in range(k):
            if item_arr.index(min_dist) == i3:
                arr[i3].append(data[i])
    point_arr = [get_centerPoint(arr[i]) for i in range(k)]
    if point_arr != init_points:
        arr=k_means(point_arr,data)
    return arr
def random_choose_k(data):
    points = []
    for i in range(k):
        random_index = random.randint(0, len(data) - 1)
        points.append(data[(random_index)])
    return points
def div_x_y(arr):
    return [i[0] for i in arr],[i[1] for i in arr]

def random_data(t,down,up):
    return [[random.uniform(down, up),random.uniform(down, up)] for i in range(t)]


k = 5
data = random_data(10,0,10)
# data = [[1,4],[1,5],[2,4],[2,5],[2,6],[4,1],[4,2],[5,1],[5,2],[6,2]]
color = ['y.','k.','b.','g.','m.','c.','r.'] # k���Ϊ7������ɫ������

init_points = random_choose_k(data)
arr = k_means(init_points,data)

for i in range(k):
    x,y = div_x_y(arr[i])
    plt.plot(x,y, color[i])

plt.show()


