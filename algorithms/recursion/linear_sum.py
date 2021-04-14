# here we are working down to the bottom and then coming back up to sum everything up
def linear_sum(S, n):
    if n == 0:
        return 0
    else:
        return linear_sum(S, n - 1) + S[n-1]


S = [4, 3, 6, 2, 8]
print(linear_sum(S, len(S)))
