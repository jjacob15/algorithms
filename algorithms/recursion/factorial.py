def factorial(n):
    if n == 0:
        return 1
    else:
        val = n * factorial(n - 1)
        print(val)
        return val


factorial(50)
