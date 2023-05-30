def pour_water(jug1_capacity, jug2_capacity, target_amount):
    visited_states = set()  # To keep track of visited states during DFS
    path = []  # To store the sequence of actions

    def dfs(jug1_amount, jug2_amount):
        if jug1_amount == target_amount or jug2_amount == target_amount:
            return True
        
        if (jug1_amount, jug2_amount) in visited_states:
            return False
        
        visited_states.add((jug1_amount, jug2_amount))

        # Action: Fill jug1 to its maximum capacity
        if jug1_amount < jug1_capacity:
            if dfs(jug1_capacity, jug2_amount):
                path.append((jug1_capacity, jug2_amount))
                return True

        # Action: Fill jug2 to its maximum capacity
        if jug2_amount < jug2_capacity:
            if dfs(jug1_amount, jug2_capacity):
                path.append((jug1_amount, jug2_capacity))
                return True

        # Action: Empty jug1
        if jug1_amount > 0:
            if dfs(0, jug2_amount):
                path.append((0, jug2_amount))
                return True

        # Action: Empty jug2
        if jug2_amount > 0:
            if dfs(jug1_amount, 0):
                path.append((jug1_amount, 0))
                return True

        # Action: Pour water from jug1 to jug2 until jug2 is full or jug1 is empty
        if jug1_amount > 0 and jug2_amount < jug2_capacity:
            pour_amount = min(jug1_amount, jug2_capacity - jug2_amount)
            if dfs(jug1_amount - pour_amount, jug2_amount + pour_amount):
                path.append((jug1_amount - pour_amount, jug2_amount + pour_amount))
                return True

        # Action: Pour water from jug2 to jug1 until jug1 is full or jug2 is empty
        if jug2_amount > 0 and jug1_amount < jug1_capacity:
            pour_amount = min(jug2_amount, jug1_capacity - jug1_amount)
            if dfs(jug1_amount + pour_amount, jug2_amount - pour_amount):
                path.append((jug1_amount + pour_amount, jug2_amount - pour_amount))
                return True

        return False

    # Perform the depth-first search
    if dfs(0, 0):
        path.append((0, 0))
        path.reverse()
        return path
    else:
        return None

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target_amount = 2

solution_path = pour_water(jug1_capacity, jug2_capacity, target_amount)
if solution_path:
    print(f"Solution found: {solution_path}")
else:
    print("No solution found.")
