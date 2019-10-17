%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,16,128)
k1 = 1
k2 = 1.9
plt.plot(x, np.cos(x*k1), marker = "o")
plt.plot(x, np.cos(x*k2), marker = "x")