num = int(input())
if num <= 1:
    trfa = False
else:
    trfa = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            trfa = False
if trfa:
    print("Число: ", num,"- простое")
else:
    print("Число", num, " - составное число")