# Сгенерируйте десять выборок случайных чисел х0, …, х9.
# и постройте гистограмму распределения случайной суммы х0+х1+ …+ х9.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

x = []      #список выборок
sum = []    #список сумм элементов каждой выборки
for i in range (0,10):
    sum.append(0)
    x.append(np.random.rand(100))  #np.random.rand(0,9,100) для целых
    # x.append(np.random.randint(0, 9, 100))
    sum_i = x[i].sum()
    sum[i] = sum[i] + sum_i
    print(sum[i],x[i])

print (sum)
num_bins = 7
n, bins, patches = plt.hist(sum, num_bins)
plt.xlabel('sum')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()