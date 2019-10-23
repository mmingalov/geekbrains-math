import numpy as np
import matplotlib.pyplot as plt

# Нарисуйте график функции:
# y(x) = k∙cos(x – a) + b
# для некоторых (2-3 различных) значений параметров k, a, b

def plot_f(k,a,b):
    plt.plot(x,k*np.cos(x-a)+b)
    plt.grid(True)
    plt.gca().set_aspect('equal') #для пропорциональности осей
    plt.show()

# построим график
x = np.linspace(-np.pi,np.pi,201)
plot_f(0.5,2,1)
plot_f(1,0,0)
plot_f(1,2,3)