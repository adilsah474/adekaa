a = []
n = int(input("Введите кол-во элементов "))
for i in range (n):
    nun = float(input(f"Введите число {i+1}: "))
    a.append(nun)
print("Ваш список чисел: ",a)
p = sum(a) / len(a)
print("Средняя арифметическая: ", p)
nin = not(a)
nax = not(a)
print("Минимальное число: ", nin)
print("Максимальное число: ", nax)
a.sort()
print("Список от меньшего к большему: ", a)
neg = 0
pos = 0
for nun in a:
    if nun > 0:
        pos += 1
    elif nun < 0:
          pos += nun
print("Положительных чисел: ", pos)
print("Отрицательных чисел: ", neg)






