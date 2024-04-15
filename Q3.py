def min_sum_of_products(array_one, array_two):
    n = len(array_one)
    
    array_one.sort()
    array_two.sort(reverse=True)
    
    sum_of_products = sum(array_one[i] * array_two[i] for i in range(n))
    
    return sum_of_products

array_one = [7, 5, 1, 4]
array_two = [6, 17, 9, 3]
min_sum = min_sum_of_products(array_one, array_two)
print("Minimum sum of products:", min_sum)
