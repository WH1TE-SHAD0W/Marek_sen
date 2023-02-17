def check_oddnumber(n):
    for i in range(2, n):
        if (n % i) != 0:
            print(n%i, i)
            return True
    else:
        return False

print(5%3)
print(check_oddnumber(5))
