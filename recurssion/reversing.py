# here we are doing the operation and then going down to the next position unlike linear sum
#both are recurssive but they have different approches.ArithmeticError()
def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start+1, stop-1)


S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse(S, 0, len(S))
print(S)
