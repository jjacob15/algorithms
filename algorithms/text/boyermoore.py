def boyer_moore(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {}
    for k in range(m):
        # dictionary to hold positions of characters. It keeps the last occurance of the character
        last[P[k]] = k
    print(last)
    i = m - 1  # start index for T 
    k = m - 1  # start index for P, pattern  match ends with k ==0

    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(T[i], -1)
            # the min of k and j+1 is to ensure it only moves k distance forward and not the total length
            i += m - min(k, j+1) # this is to counter two case. If the match was before or after the character of the pattern that was aligned with the mismatch
            k = m - 1
    return -1


if __name__ == "__main__":
    print(boyer_moore('abacaabadcabacabaabb', 'abacab'))
