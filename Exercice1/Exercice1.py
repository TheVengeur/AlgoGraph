import numpy as np

def calculate_waiting_time(positions, order):
    total_distance = 0.0
    current_position = 0.0
    total_waiting_time = 0.0
    
    for house in order:
        distance = abs(current_position - house)
        total_distance += distance
        total_waiting_time += total_distance  # Accumulate total distance as waiting time
        current_position = house
    
    return total_waiting_time / len(order)

def sort_cleaning(positions):
    return sorted(positions)

def closest_first_cleaning(positions):
    current_position = 0.0
    order = []
    unvisited = set(positions)
    
    while unvisited:
        closest = min(unvisited, key=lambda x: abs(x - current_position))
        order.append(closest)
        unvisited.remove(closest)
        current_position = closest
    
    return order

def dynamic_programming_cleaning(positions):
    positions = sorted(positions)
    n = len(positions)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            cost = abs(positions[i] - positions[j])
            dp[i] = min(dp[i], dp[j] + cost * (i - j))
    order = []
    current_position = 0
    while positions:
        next_house = min(positions, key=lambda x: abs(x - current_position))
        order.append(next_house)
        positions.remove(next_house)
        current_position = next_house
    return order

def partie_1():
# Configuration where optimal order is not obtained by sorting or closest first
    house_positions = [1.0, 2.0, 3.0, 4.0, 5.0]

    # Sorting order
    sorted_order = sorted(house_positions)
    sorted_waiting_time = calculate_waiting_time(house_positions, sorted_order)

    # Closest first order (greedy approach)
    closest_order = closest_first_cleaning(house_positions)
    closest_waiting_time = calculate_waiting_time(house_positions, closest_order)

    # Dynamic programming order

    # Output results
    print("House Positions:", house_positions)
    print("Sorted Order:", sorted_order, "Waiting Time:", sorted_waiting_time)
    print("Closest First Order:", closest_order, "Waiting Time:", closest_waiting_time)

def partie_2():
    house_positions = [1.0, 2.0, 3.0, 4.0, 5.0]

    # Sorting order
    sorted_order = sorted(house_positions)
    sorted_waiting_time = calculate_waiting_time(house_positions, sorted_order)

    # Closest first order (greedy approach)
    closest_order = closest_first_cleaning(house_positions)
    closest_waiting_time = calculate_waiting_time(house_positions, closest_order)

    # Dynamic programming order
    dp_order = dynamic_programming_cleaning(house_positions)
    dp_waiting_time = calculate_waiting_time(house_positions, dp_order)

    # Output results
    print("House Positions:", house_positions)
    print("Sorted Order:", sorted_order, "Waiting Time:", sorted_waiting_time)
    print("Closest First Order:", closest_order, "Waiting Time:", closest_waiting_time)
    print("Dynamic Programming Order:", dp_order, "Waiting Time:", dp_waiting_time)

def parcours(positions):
    positions = sorted(positions)
    n = len(positions)
    dp = [float('inf')] * n
    dp[0] = 0
    for i in range(1, n):
        for j in range(i):
            cost = abs(positions[i] - positions[j])
            dp[i] = min(dp[i], dp[j] + cost * (i - j))
    order = []
    current_position = 0
    while positions:
        next_house = min(positions, key=lambda x: abs(x - current_position))
        order.append(next_house)
        positions.remove(next_house)
        current_position = next_house
    return order

def partie_3():
# Generate random initial positions with normal distribution
    house_positions = np.random.normal(0, 1000, 1000).tolist()

    # Compute the order with the dynamic programming approach
    optimal_order = parcours(house_positions)
    optimal_waiting_time = calculate_waiting_time(house_positions, optimal_order)

    print("Dynamic Programming Waiting Time:", optimal_waiting_time)

    closest_first_order = sorted(house_positions, key=lambda x: abs(x))
    closest_first_waiting_time = calculate_waiting_time(house_positions,closest_first_order)
    print("Closest First Waiting Time:", closest_first_waiting_time)

    sorted_order = sorted(house_positions)
    sorted_waiting_time = calculate_waiting_time(house_positions, sorted_order)
    print("Sorted Waiting Time:", closest_first_waiting_time)