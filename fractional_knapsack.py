def fractional_knapsack(capacity, values, weights):
    n = len(values)
    items = []

    for i in range(n):
        items.append((values[i], weights[i], values[i] / weights[i]))

    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0.0

    for value, weight, ratio in items:
        if capacity == 0:
            break
        if weight <= capacity:
            capacity -= weight
            total_value += value
        else:
            total_value += ratio * capacity
            capacity = 0

    return total_value


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(fractional_knapsack(capacity, values, weights))
