import math

# Даны два вектора в трехмерном пространстве: (10,10,10) и (0,0,-10)
# Найдите их сумму. (на листочке)
# Напишите код на Python, реализующий расчет длины вектора, заданного его координатами

# РЕШЕНИЕ
# Сумма векторов -- это результирующий вектор, который вычисляется как:
# [0-10,0-10,-10-10] -> [-10,-10,-20]

vec1 = [10,10,10]
vec2 = [0,0,-10]

def VectorGet(v1, v2):
    result = []
    for i in range(v1.__len__()):
        result.append(v2[i]-v1[i]);
    return result;

def LengthGet(v):
    sum = 0
    for i in v:
        sum = sum + i*i;
    return (math.sqrt(sum))

vec3 = VectorGet(vec1,vec2);
print("Искомый вектор:",vec3)
len3 = LengthGet(vec3);

print ("Длина искомого вектора =",len3);
