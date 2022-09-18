a = float(input("Введите действительное число a:"))
b = float(input("Введите действительное число b:"))
c = float(input("Введите действительное число c:"))
for i in (a,b,c):
    if abs(i) >= 4:
        print(i)
