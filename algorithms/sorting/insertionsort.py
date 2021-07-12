def insertion_sort(S):
    for k in range(1, len(S)):
        cur = S[k]
        print('cur', cur)
        j = k
        while j > 0 and S[j-1] > cur:
            S[j] = S[j-1] # copy the value forward
            j -= 1
            print(S)

        print('j ends at ', j)
        S[j] = cur # set the value at j to Current
        print('setting cur ', S)

if __name__ == "__main__":
    S = [85, 24, 63, 45, 17, 31, 96, 50]
    print(S)
    insertion_sort(S)
    print(S)
