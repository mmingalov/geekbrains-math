# Из урока по комбинаторике повторите расчеты, сгенерировав возможные варианты
# перестановок для других значений n и k
import itertools
count = 0
for p in itertools.product("012345678",repeat=3):
    print(''.join(p))
    count = count + 1

print("total", count)