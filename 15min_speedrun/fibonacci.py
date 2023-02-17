def fibonacci(n):
    m = [1,1]
    for i in range(n):
        m.append(m[i]+m[i+1])
    print(m[n-1])

print(fibonacci(7))