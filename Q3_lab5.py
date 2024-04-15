def pylons(distribution, positions):
    total_plants = 0
    last_plant_pos = -1
    i = 0
    
    while i < len(positions):
        plant_location = min(i + distribution - 1, len(positions) - 1)
        
        while plant_location > last_plant_pos:
            if positions[plant_location] == 1:
                break
            plant_location -= 1
        
        if plant_location == last_plant_pos:
            return -1
        
        total_plants += 1
        last_plant_pos = plant_location + distribution - 1
        i = last_plant_pos + 1
    
    return total_plants

def main():
    n, k = map(int, input().split())
    positions = list(map(int, input().split()))

    print(pylons(k, positions))

if __name__ == "__main__":
    main()
