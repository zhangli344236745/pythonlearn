# -*- coding=utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

mass = [50*i for i in range(1,12)]
length = [1.000,1.875,2.750,3.250,4.375,4.875,5.675,6.500,7.250,8.000,8.750]

F = np.polyfit(mass,length,1)
print(F)
P = np.poly1d(F)
print(P)

y = np.polyval(F,mass)

plt.title('mass length')#创建标题
plt.xlabel('mass')#X轴标签
plt.ylabel('length')#Y轴标签
plt.plot(mass,length)#画图
plt.plot(mass,y,color = 'r')#根据函数值画图并设定颜色
plt.show()#显示