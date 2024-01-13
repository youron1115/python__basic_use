a=[[1,2],[3,4]]
"""
    1 2
a=
    3 4
"""
b=[[5,6],[7,8]]
"""
    5 6
b=      
    7 8
"""
c=[1,2]
d=[5,6]
#一般陣列不適用直接做加法
print("一維矩陣加法:\n",c+d)
#二維會變成將兩個矩陣組合成一個矩陣
print("二維矩陣加法:\n",a+b)

import numpy as np
a=np.array(a)
b=np.array(b)
c=np.array(c)
d=np.array(d)
print("一維矩陣加法:\n",c+d)
print("二維矩陣加法:\n",a+b)

print("矩陣乘法:\n",a*b)#即對應位置相乘
print("一維矩陣內積:\n",c@d)
print("二維矩陣內積:\n",a@b)

np1=np.array([[1,2],[3,4]],dtype=int)#用array產生矩陣，dtype可指定資料型態
print("array產生矩陣:\n",np1)
np2=np.arange(0,5,2)#用arange產生矩陣(似迴圈)，可reshape
print("arange產生矩陣:\n",np2)
np3=np.linspace(0,16,3)#用linspace產生矩陣(在範圍內產生等距元素)，可reshape
print("linspace產生矩陣:\n",np3)
np4=np.zeros((2,3))#用zeros產生矩陣，可reshape，另有ones可以使用
print("zeros產生矩陣:\n",np4)
np5=np.random.rand(2,3)#用random產生矩陣，可reshape
print("random產生矩陣:\n",np5)
np5_2=np.random.randint(0,100,2)
#np5_2=np.random.randint(0,100,size=2)#size可加可不加
#產生範圍內的整數矩陣元素(同list一樣不含上限)
#如果設定high=None則是0-low(不含low)之間的整數
np5_2=np.random.randint(0,100,(2,3))
#np5_2=np.random.randint(0,100,size=(2,3))#size可加可不加
#產生範圍內的整數矩陣元素(同list一樣不含上限)
#如果設定high=None則是0-low(不含low)之間的整數，(2,3)為矩陣維度
print("randint產生矩陣:\n",np5_2)
np6=np.empty((2,3),dtype=int)#用empty產生矩陣，為記憶體中拉出的空間因此元素為隨機值
print("empty產生矩陣:\n",np6)


x=np.array([[1,2],[3,4],[5,6]])
x**=2
print("x**=2:\n",x)

print("x.shape[0]:",x.shape[0])
print("x.shape[1]:",x.shape[1])

for i in range(x.shape[0]):
    print("透過x.shape[0]列出x[i]:",x[i])
    
x0=np.array([[1,2,3],[4,5,6]])

print("x0.sum(0):",x0.sum(0))
print("x0.sum(1):",x0.sum(1))