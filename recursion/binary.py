# only if data is sorted
def binary_search(data, target, low, high):
    if(low > high):
        return False
    else:
        mid = (low+high)//2
        if target == data[mid]:
            return True
        if target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]

#tail recursions can be made iterative 
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


print(binary_search(data, 22, 0, 15))
print(binary_search_iterative(data, 22))
