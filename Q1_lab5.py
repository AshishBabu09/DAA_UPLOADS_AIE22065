def min_candies_needed(n, ratings):
    candy_counts = [1] * n
    
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candy_counts[i] = candy_counts[i - 1] + 1
    
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candy_counts[i] = max(candy_counts[i], candy_counts[i + 1] + 1)
    
    return sum(candy_counts)

n = int(input())
ratings = [int(input()) for _ in range(n)]

min_candies = min_candies_needed(n, ratings)
print(min_candies)
