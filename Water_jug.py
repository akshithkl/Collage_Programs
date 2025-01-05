
 
#1. Implement and Demonstrate Depth First Search Algorithm on Water Jug Problem. 


def dfs(x_capacity, y_capacity, target, visited=set(), current=(0, 0)): 
    # Current state 
    x_current, y_current = current 
     
    # Check if the current state solves the problem or has been visited 
    if (x_current == target or y_current == target): 
        return [current]   # Return path containing only the current state if it's a solution 
    if current in visited: 
        return None 
     
    # Mark the current state as visited 
    visited.add(current) 
     
    # List of possible new states 
    states = [ 
        (x_capacity, y_current),  # Fill X completely 
        (x_current, y_capacity),  # Fill Y completely 
        (0, y_current),           # Empty X 
        (x_current, 0),           # Empty Y 
        ((x_current - min(x_current, y_capacity - y_current)), (y_current + 
min(x_current, y_capacity - y_current))),  # Pour X to Y 
        ((x_current + min(y_current, x_capacity - x_current)), (y_current - 
min(y_current, x_capacity - x_current)))   # Pour Y to X 
    ] 
 
    # Try all possible moves 
    for state in states: 
        if state not in visited: 
            result = dfs(x_capacity, y_capacity, target, visited, state) 
            if result is not None: 
                return result + [current]  # Append current state to path if succeeding 
 
    # If no state is valid, backtrack by unvisiting the current state 
    visited.remove(current) 
    return None 
 
def solve_water_jug(x_capacity, y_capacity, target): 
    result = dfs(x_capacity, y_capacity, target) 
    if result is None: 
        return "No solution" 
    else: 
        return result[::-1]  # Reverse to display steps from start to finish 
 
# Example usage 
x_capacity = 4 
y_capacity = 3 
target = 2 
result = solve_water_jug(x_capacity, y_capacity, target) 
 
print("Steps to achieve target:") 
if isinstance(result, str): 
    print(result) 
else: 
    for step in result: 
        print(step) 
 
 