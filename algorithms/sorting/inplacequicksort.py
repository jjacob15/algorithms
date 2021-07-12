def inplace_quicksort(S, a, b):
    if a >= b:
        return
    pivot = S[b]
    left = a
    right = b-1
    while left <= right:
        # scan until reaching value equal or larger than pivot (or right marker)
        # only move right if value is lesser than pivot. The goal is to get all the values less than pivot on the left
        # and the values larger than pivot to the right.
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and S[right] > pivot:
            right -= 1
        # scans did not strictly cross
        # swap left with right.
        if left <= right:
            S[left], S[right] = S[right], S[left]  # swap values
            left, right = left+1, right - 1  # shrink range

    # put pivot into its final place (currently marked by left index)
    # now put pivot at the center and split and recurse
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quicksort(S, a, left - 1)
    inplace_quicksort(S, left + 1, b)


if __name__ == "__main__":
    S = [85, 24, 63, 45, 17, 31, 96, 50]
    print(S)
    inplace_quicksort(S, 0, len(S)-1)
    print(S)
