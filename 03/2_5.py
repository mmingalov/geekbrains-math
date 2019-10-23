# 5. Задание (в программе)
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

# Нарисуйте трехмерный график двух параллельных плоскостей.
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X,Y)
Z = 2+Y
Z2 = 8+Y
ax.plot_wireframe(X,Y,Z)
ax.plot_wireframe(X,Y,Z2)
ax.scatter(0, 0, 0, 'z', 50, 'red')
show()


# Нарисуйте трехмерный график двух любых поверхностей второго порядка.
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.5)
Y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(X,Y)
Z = np.sqrt(X*X + Y*Y)
Z2 = (X*X - Y*Y)
ax.plot_surface(X,Y,Z)
ax.plot_surface(X,Y,Z2,color='green')
ax.scatter(0, 0, 0, 'z', 50, 'red')
show()

