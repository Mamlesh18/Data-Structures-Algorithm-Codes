def maxProductSubarray(arr):
    n = len(arr)

    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]

    for i in range(1, n):
        current = arr[i]

        temp_max = max(current, max_product * current, min_product * current)
        min_product = min(current, max_product * current, min_product * current)
        max_product = temp_max

        result = max(result, max_product)

    return result

arr1 = [-2, 6, -3, -10, 0, 2]

print(maxProductSubarray(arr1))