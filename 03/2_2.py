# Почему прямые не кажутся перпендикулярными? (см.ролик)
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-5,5,21)
y = 3*x+1
y2 = (-1/3)*x+1
plt.plot(x,y)
plt.plot(x,y2)
plt.xlabel("x")
plt.ylabel("y")

plt.gca().set_aspect('equal')
plt.show()

# ОТВЕТ: прямые не кажутся перпендикулярными потому что шкалы осей отличаются пропорциональностью, т.е. отрезок на оси абсцисс в 2 единицы соответствует отрезку на ординат в 5 единиц.
# для того чтобы исправить этот момент необходиио перед вызовом .show() применить следующий код^
# plt.gca().set_aspect('equal')