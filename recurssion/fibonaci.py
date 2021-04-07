def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2)+bad_fibonacci(n-1)


# print(bad_fibonacci(10))


# example of linear recurssion as it make one call at the end of the function
def good_fibonacci(n):
    if n <= 1:
        print('in for ', n)
        return (n, 0)
    else:
        print('in else with ', n)
        a, b = good_fibonacci(n-1)
        print(a, b, 'for', n)
        return (a+b, a)


print(good_fibonacci(10))
