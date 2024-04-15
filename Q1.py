class Item:
    def __init__(self, benefit, weight):
        self.benefit = benefit
        self.weight = weight
        self.value_per_weight = benefit / weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.value_per_weight, reverse=True)

    total_value = 0
    sack = []

    for item in items:
        if capacity >= item.weight:
            total_value += item.benefit
            sack.append((item, 1.0))
            capacity -= item.weight
        else:
            fraction = capacity / item.weight
            total_value += fraction * item.benefit
            sack.append((item, fraction))
            break

    return total_value, sack

items = [Item(60, 10), Item(100, 20), Item(120, 30)]
capacity = 50

optimal_value, optimal_sack = fractional_knapsack(items, capacity)
print("Optimal value:", optimal_value)
print("Optimal sack contents:")
for item, fraction in optimal_sack:
    print("- Item with benefit {}, weight {}, and fraction {}".format(item.benefit, item.weight, fraction))
