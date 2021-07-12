def quick_sort(S):
    n = len(S)
    if n < 2:
        return
    p = S[-1] # remember to peek for the pivot and not remove it
    L = []
    G = []
    E = []
    while(len(S) > 0):
        n = S.pop(0)
        if n < p:
            L.append(n)
        elif n > p:
            G.append(n)
        else:
            E.append(n)

    quick_sort(L)
    quick_sort(G)

    for n in L:
        S.append(n)
    for n in E:
        S.append(n)
    for n in G:
        S.append(n)


if __name__ == "__main__":
    S = [85, 24, 63, 45, 17, 31, 96,45,17, 50]
    quick_sort(S)
    print(S)
