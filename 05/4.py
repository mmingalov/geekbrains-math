# Из урока по комбинаторике повторите расчеты, сгенерировав возможные варианты
# перестановок для других значений n и k
import itertools
#1
count = 0
for p in itertools.product("0123",repeat=4):
    print(''.join(p))
    count = count + 1
print("total", count)
print()

#2 Перестановки
count = 0
for p in itertools.permutations("0123",4):
    print(''.join(str(x) for x in p))
    count = count + 1
print("total permutations:", count)
print()

#3 Комбинации
count = 0
for p in itertools.combinations("0123",3):
    print(''.join(str(x) for x in p))
    count = count + 1
print("total combinations:", count)