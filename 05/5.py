import numpy as np
import matplotlib.pyplot as plt

# ​ Дополните код расчетом коэффициента корреляции ​ x ​ и ​ y ​ по формуле

n = 100
r = 0.77
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x,y,'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print("a, b через МНК для линейной регрессии:",a,b)
print("a, b через встроенную библиотеку:",a1, b1)
c = np.corrcoef(x, y)
print("Коэф корреляции через встроенную библиотеку:", c)

# ​ Дополните код расчетом коэффициента корреляции ​ x ​ и ​ y ​ по формуле
# найдем средние значения
x_avg = np.average(x)
y_avg = np.average(y)
print("x, y средние:",x_avg, y_avg)
R = np.sum((x - x_avg)*(y - y_avg)) / (np.sum((x-x_avg)**2)*(np.sum((y-y_avg)**2)))**0.5
print("Коэф корреляции по формуле:", R)
plt.plot([0, 1], [b, a + b])
plt.show()