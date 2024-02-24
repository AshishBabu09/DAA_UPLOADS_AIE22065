import time
import numpy as np

def insertion_sort(arr):
    n = len(arr)
    swaps = 0
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
        arr[j + 1] = key
    
    return swaps

arr = np.random.randint(1, 100, size=50)  

start_time = time.time()

swaps = insertion_sort(arr)
print("Sorted array:", arr)
print("Number of swaps:", swaps)

end_time = time.time()

time_taken = end_time - start_time

print("Time taken:", time_taken, "seconds")
