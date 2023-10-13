n = int(input("Введите номер числа Фибоначчи: "))
result = 0
if n > 3:
    a, b = 0, 1
    for i in range(3, n):
        a, b = b, a + b
        if i+1 == n:
            result = a + b
            print(result)
elif n == 1:
    result = 0
    print(result)
elif n == 2:
    result = 1
    print(result)
elif n == 3:
    result = 1
    print(result)
else:
    print("Введите число больше 0.")