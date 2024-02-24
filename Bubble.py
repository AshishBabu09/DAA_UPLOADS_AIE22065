import time
import numpy as np

def bubblesort(arr):
    n = len(arr)
    swaps = 0
    
    for i in range(n): 
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1

    return swaps

arr = np.random.randint(1, 100, size=50)  

start_time = time.time()

swaps = bubblesort(arr)
print("Sorted array:", arr)
print("Number of swaps:", swaps)

end_time = time.time()

time_taken = end_time - start_time

print("Time taken:", time_taken, "seconds")
