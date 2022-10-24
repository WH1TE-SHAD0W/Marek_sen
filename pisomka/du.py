import math
n = int(input())
fib = [0, 1]



for i in range(n):
    fib.append(fib[i] + fib[i + 1])
# print(fib[n-1], fib)

num = fib[n-1]
# print(fib[n-1])
rounded = round(num/10)*10

print(rounded)
