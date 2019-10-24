import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
# Решите систему уравнений:
# y = x**2 – 1
# exp(x) + x∙(1 – y) = 1
def equations(p):
    x, y = p
    return (y - x**2 + 1, np.exp(x) - x*y +x -1)

# построим графики
x = np.linspace(-2,3,201)
plt.plot(x,(np.exp(x) +x - 1)/x) #синий
plt.plot(x, x**2 - 1)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-1.5)
plt.grid(True)
plt.show()

# решим с-му численным методом
#1
xx = -1.5
yy = 1.5
print("Решение с точкой приближения: (",xx,";",yy,")")
x1, y1 = fsolve(equations,(xx,yy))
print ("x1=",x1,"; y1=",y1)
#2
xx = 2.5
yy = 5.5
print("Решение с точкой приближения: (",xx,";",yy,")")
x2, y2 = fsolve(equations,(xx,yy))
print ("x2=",x2,"; y2=",y2)

print()
# Решите систему уравнений и неравенств:
# y = x**2 – 1
# exp(x) + x∙(1 – y) > 1

def ner(x,y):
    return np.exp(x)+x*(1-y)-1
print ("Выше мы нашли корни системы уравнений. Проверим найденные корни, подставив их в систему с уравнением и неравенством.")
print("y = x**2 – 1")
print ("exp(x) + x∙(1 – y) -1 > 0")
print("Решением системы будут корни, при котором выполняется неравенство (>0 ). Подставим и посчитаем:")
print("x1,y1:",ner(x1,y1))
print("x2,y2:",ner(x2,y2))