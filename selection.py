import time
start_time = time.time()

import numpy as np

def selection_sort(arr):
    n = len(arr)
    swaps = 0
    
    for i in range(n):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    return swaps  


arr = np.random.randint(1, 100, size=50)  
print("Original array:", arr)
swaps = selection_sort(arr)
print("Sorted array:", arr)
print("Number of swaps:", swaps)

end_time = time.time()


time_taken = end_time - start_time
print("Time taken:", time_taken,"seconds")