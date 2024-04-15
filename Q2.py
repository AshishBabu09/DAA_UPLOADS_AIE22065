def max_sum(arr):
    n = len(arr)
    max_sum = 0

    for i in range(n):
        for j in range(i, n):
            max_sum = max(max_sum, arr[i] * j)

    return max_sum

arr = [2, 5, 3, 4, 0]
print("Maximum sum:", max_sum(arr))
