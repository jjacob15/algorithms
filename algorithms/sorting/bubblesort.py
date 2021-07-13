""" bubble sort only compares its ajacent value during one iteration and need 
multiple iterations to complete the sort.
When it completes an iteration with no swap, it exits.
Average 0(n^2)
Worst 0(n^2)
"""
def bubblesort(S):
    n = len(S)
    swapped = None
    while swapped == True or swapped == None:
        swapped = False
        for i in range(n-1):
            if S[i] > S[i+1]:
                S[i+1], S[i] = S[i], S[i+1]
                swapped = True


if __name__ == "__main__":
    S = [17, 1, 2, 3, 85, 24, 63, 45,  31, 96, 50, 3, 2, 1]
    bubblesort(S)
    print(S)
