import numpy as np, math


# 1) Дополните код Монте-Карло последовательности независимых испытаний      расчетом соответствующих вероятностей (через биномиальное распределение)  и сравните результаты.
def Monte_Karlo(kk,n):
    # k,n = 0, 5000
    k=0
    a = np.random.randint(0,2 ,n)
    b = np.random.randint(0,2 ,n)
    c = np.random.randint(0,2 ,n)
    d = np.random.randint(0,2 ,n)
    x = a + b + c + d

    for i in range(0,n):
        if x[i] == kk:   #оценивается вероятность равного выпадения орлов и решек на ЧЕТЫРЕХ испытаниях, т.е. 2 раза Орел и 2 раза Решка
            k = k + 1
    print ("Вероятность по Монте-Карло:", k, n, k/n)

def Bernulli(n,k):
    C_n_k = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    P_n_k = C_n_k * 1/2**n
    print("Вероятность по Бернулли:", P_n_k)
    return P_n_k
#1
print("Задание 1:")
Monte_Karlo(2,5000)
Bernulli(4,2)

#2 Повторите расчеты биномиальных коэффициентов и вероятностей k успехов в         последовательности из n независимых испытаний, взяв другие значения n и k.
print("Задание 2:")
Bernulli(5,3)
