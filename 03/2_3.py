import numpy as np
import matplotlib.pyplot as plt
import math
# Напишите код на Python, реализующий построение графиков:
#   окружности,
#   эллипса,
#   гиперболы.

def plot_ellipsoid(a,b):
    # plot эллипс
    # x**2/a**2 + y**2/b**2 = 1
    x=[]
    y=[]
    # a=3
    # b=1
    x = np.linspace(-a, a, 512, endpoint=True)
    y = np.sqrt((1-x**2/a**2)*b**2)
    plt.plot(x, y, marker = "o")
    plt.plot(x, -y, marker = "o")
    plt.gca().set_aspect('equal')
    plt.show()

def plot_circle(R):
    # plot окружность
    # x**2 + y**2 = R**2
    x=[]
    y=[]
    # R=3
    x = np.linspace(-R, R, 512, endpoint=True)
    y = np.sqrt(-(x*x) + R*R)
    plt.plot(x, y, marker = "o")
    plt.plot(x, -y, marker = "o")
    plt.gca().set_aspect('equal')
    plt.show()

def plot_hyperboloid(a,b):
    # plot гипербола
    # x**2/a**2 - y**2/b**2 = 1
    x=[]
    y=[]
    # a=3
    # b=1
    x = np.linspace(-a*3, a*3, 512, endpoint=True)
    y = np.sqrt((x**2/a**2 - 1)*b**2)
    plt.plot(x, y, marker = "o")
    plt.plot(x, -y, marker = "o")
    # plt.gca().set_aspect('equal')
    plt.show()

# построим Окружность
plot_circle(1)
# построим Эллипсоид
plot_ellipsoid(3,2)
# построим Гиперболу
plot_hyperboloid(2,2)