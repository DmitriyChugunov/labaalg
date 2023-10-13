def sort(num):
    a = len(num)
    for i in range(a):
        for j in range(a-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
num = [100, 1000, 20, 1, 2, 7, 21]
sort(num)
print(num)