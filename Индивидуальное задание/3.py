print("После увелечения нормы на 10 % суммарно за 7 дней пробежит:")
d = 7
summa = 0
yesterday = 10
for i in range(d):
    summa += yesterday
    yesterday += yesterday / 10
print(summa)
