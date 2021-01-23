def binary_serach(arr, item):
    low = 0
    maxi = len(arr) - 1

    while low <= maxi:
        mid = low + maxi // 2
        guess = arr[mid]
        if guess == item:
            return f"index: {mid}"
        if guess > item:
            maxi = mid - 1
        else:
            low = mid + 1
    return


print(binary_serach([1, 3, 5, 8, 9], 3))
