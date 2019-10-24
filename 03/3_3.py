import numpy as np
import matplotlib.pyplot as plt
# Напишите код, который будет переводить полярные координаты в декартовы.
def polarToDecart(a,R):
    # x = r*cosa
    # y = r*sina
    return (R*np.cos(a), R*np.sin(a))

aa = np.pi/4
rr = 1
print ("Полярные координаты:", "угол", aa,"радиус",rr)
print("Перевод в декартовы координаты:",polarToDecart(aa,rr))

# Напишите код, который будет рисовать график окружности в полярных координатах.
R=3
x = np.linspace(-R, R, 512, endpoint=True)
y = np.sqrt(-(x * x) + R * R)
# plt.plot(x, y, marker="o")
# plt.plot(x, -y, marker="o")
# plt.gca().set_aspect('equal')
plt.polar(x,y)
plt.show()

# Напишите код, который будет рисовать график отрезка прямой линии в полярных координатах.
x = np.linspace(0,5,100)
y = 2*x+2
# plt.plot(x,y)
plt.polar(x,y)
plt.gca().set_aspect('equal')
plt.show()