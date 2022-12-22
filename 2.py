# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input())
i=2
result = list()
for i in range(2, n + 1): 
    while (n % i == 0): 
        result.append(i)
        n=n/i
print(result)
            