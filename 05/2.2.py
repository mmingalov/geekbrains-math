# Сгенерируйте десять выборок случайных чисел х0, …, х9.
# и постройте гистограмму распределения случайной суммы х0+х1+ …+ х9.
import numpy as np
import matplotlib.pyplot as plt

x = []      #список выборок
sum = []    #список сумм элементов каждой выборки
for i in range (0,10):
    sum.append(0)
    x.append(np.random.rand(32))  #np.random.rand(0,9,100) для целых
    # x.append(np.random.randint(0, 9, 10))
    # sum_i = x[i].sum()
    # sum[i] = sum[i] + sum_i
print(x)
sum = x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8]+x[9]
print (sum)

num_bins = 7
n, bins, patches = plt.hist(sum, num_bins)
plt.xlabel('sum')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()