def max_people(pop, towns, clouds, ranges):
    num_towns = len(towns)
    num_clouds = len(clouds)
    sunny_pop = sum(pop)
    max_sunny_pop = sunny_pop
    
    for i in range(num_clouds):
        cloud_pop = 0
        left = clouds[i] - ranges[i]
        right = clouds[i] + ranges[i]
        
        for j in range(num_towns):
            if left <= towns[j] <= right:
                cloud_pop += pop[j]
        
        sunny_pop_after_removal = sunny_pop - cloud_pop
        max_sunny_pop = max(max_sunny_pop, sunny_pop_after_removal)
    
    return max_sunny_pop

num_towns = int(input())
pop = list(map(int, input().split()))
towns = list(map(int, input().split()))
num_clouds = int(input())
clouds = list(map(int, input().split()))
ranges = list(map(int, input().split()))

print(max_people(pop, towns, clouds, ranges))
