def pour_water(jug1_capacity, jug2_capacity, target_amount):
    visited_states = set()
    path = []

    def dfs(jug1_amt, jug2_amt):
        if jug1_amt == target_amount or jug2_amt == target_amount:
            return True

        if(jug1_amt, jug2_amt) in visited_states:
                return False

        visited_states.add((jug1_amt, jug2_amt))

        if jug1_amt < jug1_capacity:
            if dfs(jug1_capacity, jug2_amt):
                path.append((jug1_capacity, jug2_amt))
                return True

        if jug2_amt < jug2_capacity:
            if dfs(jug1_amt, jug2_capacity):
                path.append((jug1_amt, jug2_capacity))
                return True

        if jug1_amt > 0:
            if dfs(0, jug2_amt):
                path.append((0, jug2_amt))
                return True

        if jug2_amt > 0:
            if dfs(jug1_amt, 0):
                path.append((jug1_amt, 0))
                return True

        if jug1_amt > 0 and jug2_amt < jug2_capacity:
            pour_amt = min(jug1_amt, jug2_capacity - jug2_amt)
            if dfs(jug1_amt - pour_amt, jug2_amt + pour_amt):
                return True

        if jug2_amt > 0 and jug1_amt < jug1_capacity:
            pour_amt = min(jug2_amt, jug1_capacity - jug1_amt)
            if dfs(jug1_amt + pour_amt, jug2_amt - pour_amt):
                return True
        return False

    if dfs(0,0):
        path.append((0,0))
        path.reverse()
        return path
    else:
        return none
jug1_capacity = 5
jug2_capacity = 4
target_amount = 3

solution_path = pour_water(jug1_capacity, jug2_capacity, target_amount)
if solution_path:
    print(f"Solution found: {solution_path}")
else:
    print("No solution found.")