def selectionsort(S):
    for i in range(len(S)):
        min_idx = i
        for j in range(i+1, len(S)):
            if S[min_idx] > S[j]:
                min_idx = j

        S[i], S[min_idx] = S[min_idx], S[i]


if __name__ == "__main__":
    S = [85, 24, 63, 45, 17, 31, 96, 50]
    selectionsort(S)
    print(S)
