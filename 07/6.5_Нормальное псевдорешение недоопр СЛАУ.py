import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

# Найдите нормальное псевдорешение недоопределенной системы
# x+2y-z=1
# 8x-5y+2z=12
# Для этого определите функцию Q(x,y,z), равную норме решения, и найдите ее минимум

# Недоопределенные СЛАУ - "вытянутые" прмоугольные, где кол-во неизвестных больше кол-ва уравнений
A = np.array([[1,2,-1],[8,-5,2]])
B = np.array([1,12])

def Q(x,y,z):
    return (x**2 + y**2 + z**2)
# найдем x, минимизирующее норму вектора Q(x,y,z)
x=np.linspace(0,5,201)
plt.plot(x,Q(x,10*x - 14,21*x - 29))

# найдем нормальное псевдорешение
print("нормальное псевдорешение")
print(np.linalg.lstsq(A,B))

# Нарисуем трехмерный график решения.
fig = figure()
ax = Axes3D(fig)
X = np.arange(0, 2, 0.1)
Y = np.arange(-1, 2, 0.1)
X, Y = np.meshgrid(X,Y)
Z = (X+2*Y-1)
Z2 = (12-8*X+5*Y)/2

ax.plot_surface(X,Y,Z,color='cyan')
ax.plot_surface(X,Y,Z2,color='green')
ax.scatter(1.38, -0.18, 0.02, 'z', 50, 'red')
show()