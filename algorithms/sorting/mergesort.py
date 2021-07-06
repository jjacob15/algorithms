def merge(S1, S2, S):
    i = j = 0
    while i+j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
    print('merge', S1, S2)


def merge_sort(S, msg):
    print(msg, S)
    n = len(S)
    if n <2:
        return
    mid = n //2
    S1 = S[0:mid]
    S2 = S[mid:n]
    merge_sort(S1,'S1')
    merge_sort(S2, 'S2')
    merge(S1, S2, S)


if __name__ == "__main__":
    S = [85,24,63,45,17,31,96,50]
    # S = [8,3,2,3,4,6,6,4,2,34,4,5,5,435,23,4,4,34,235,45,3242,425,4,54,45,8,3,2,3,4,6,6,4,2,34,4,5,5,435,23,4,4,34,235,45,3242,425,4,54,45,8,3,2,3,4,6,6,4,2,34,4,5,5,435,23,4,4,34,235,45,3242,425,4,54,45,8,3,2,3,4,6,6,4,2,34,4,5,5,435,23,4,4,34,235,45,3242,425,4,54,45]
    merge_sort(S,'')
    print(S)

