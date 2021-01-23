def binary_search_recursive(arr, low, maxi, x):

    if maxi >= low:
        mid = maxi + low // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, maxi, x)

    else:
        return -1


data = [2, 3, 4, 8, 11]

print(binary_search(data, 0, len(data) - 1, 2))

