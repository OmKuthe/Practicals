"""
Experiment 4: A* Algorithm for 8-Puzzle using Manhattan Distance Heuristic
"""

import heapq
import copy

# Goal state as a tuple (immutable for hashing)
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)


def manhattan_distance(state):
    """
    Manhattan Distance heuristic (admissible)
    Sum of absolute distances each tile must move to reach goal
    """
    distance = 0
    for i in range(9):
        if state[i] != 0:
            # Find where this tile should be in goal
            goal_index = GOAL_STATE.index(state[i])
            # Convert linear indices to (row, col)
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_index, 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance


def misplaced_tiles(state):
    """Alternative heuristic: count misplaced tiles (also admissible but less informed)"""
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL_STATE[i]:
            count += 1
    return count


def get_neighbors(state):
    """Generate all valid neighbor states by moving the blank tile"""
    neighbors = []
    blank_index = state.index(0)
    row, col = divmod(blank_index, 3)
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            # Swap blank with adjacent tile
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
            neighbors.append(tuple(new_state))
    
    return neighbors


def is_solvable(state):
    """
    Check if 8-puzzle is solvable using inversion parity
    For 8-puzzle (3x3), solvable if number of inversions is EVEN
    """
    flat = [tile for tile in state if tile != 0]
    inversions = 0
    
    for i in range(len(flat)):
        for j in range(i + 1, len(flat)):
            if flat[i] > flat[j]:
                inversions += 1
    
    return inversions % 2 == 0


def a_star(start_state, heuristic_func=manhattan_distance):
    """
    A* search algorithm
    Returns: (path, nodes_expanded, cost)
    """
    if not is_solvable(start_state):
        print("Warning: This puzzle state is UNSOLVABLE!")
        return None, 0, 0
    
    # Priority queue: (f(n), g(n), state, path)
    open_list = []
    start_h = heuristic_func(start_state)
    heapq.heappush(open_list, (start_h, 0, start_state, [start_state]))
    
    # Closed set to avoid revisiting states
    closed_set = set()
    nodes_expanded = 0
    
    print("Searching for optimal solution using A*...")
    
    while open_list:
        f, g, current_state, path = heapq.heappop(open_list)
        nodes_expanded += 1
        
        # Goal test
        if current_state == GOAL_STATE:
            return path, nodes_expanded, g
        
        # Mark as explored
        closed_set.add(current_state)
        
        # Expand current node
        for neighbor in get_neighbors(current_state):
            if neighbor not in closed_set:
                new_g = g + 1
                new_h = heuristic_func(neighbor)
                new_f = new_g + new_h
                
                # Check if neighbor already in open_list with better f
                heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))
    
    return None, nodes_expanded, 0


def print_solution(solution):
    """Print the solution path in a readable format"""
    if not solution:
        print("No solution found!")
        return
    
    print("\n" + "=" * 50)
    print(f"SOLUTION FOUND! ({len(solution) - 1} moves)")
    print("=" * 50)
    
    for step, state in enumerate(solution):
        print(f"\nStep {step}:")
        for i in range(0, 9, 3):
            row = state[i:i+3]
            print(" ".join(str(tile) if tile != 0 else '_' for tile in row))
    print()


# ============================================
# TEST CASES
# ============================================

def run_test_cases():
    test_cases = [
        {
            "name": "Easy - Almost solved",
            "state": (1, 2, 3,
                      4, 5, 6,
                      7, 0, 8)
        },
        {
            "name": "Medium - Needs several moves",
            "state": (1, 2, 3,
                      4, 0, 6,
                      7, 5, 8)
        },
        {
            "name": "Hard - Requires many moves",
            "state": (2, 4, 3,
                      1, 0, 6,
                      7, 5, 8)
        },
        {
            "name": "Unsolvable (should be detected)",
            "state": (1, 2, 3,
                      4, 5, 6,
                      8, 7, 0)  # Two adjacent tiles swapped → odd inversions
        }
    ]
    
    for test in test_cases:
        print("\n" + "#" * 50)
        print(f"TEST CASE: {test['name']}")
        print("#" * 50)
        
        print(f"\nSolvable: {is_solvable(test['state'])}")
        
        solution, nodes, cost = a_star(test['state'])
        print_solution(solution)
        
        if solution:
            print(f"Nodes expanded: {nodes}")
            print(f"Solution cost: {cost} moves")


# ============================================
# COMPARE HEURISTICS
# ============================================

def compare_heuristics():
    """Compare Manhattan Distance vs Misplaced Tiles"""
    test_state = (2, 4, 3,
                  1, 0, 6,
                  7, 5, 8)
    
    print("\n" + "=" * 50)
    print("HEURISTIC COMPARISON")
    print("=" * 50)
    
    print(f"\nTest state: {test_state}")
    print(f"Manhattan Distance: {manhattan_distance(test_state)}")
    print(f"Misplaced Tiles: {misplaced_tiles(test_state)}")
    
    # Run A* with both heuristics
    print("\n--- Running A* with Manhattan Distance ---")
    solution1, nodes1, cost1 = a_star(test_state, manhattan_distance)
    print(f"Nodes expanded: {nodes1}, Cost: {cost1}")
    
    print("\n--- Running A* with Misplaced Tiles ---")
    solution2, nodes2, cost2 = a_star(test_state, misplaced_tiles)
    print(f"Nodes expanded: {nodes2}, Cost: {cost2}")
    
    print("\nCONCLUSION: Manhattan Distance is more informed,")
    print("so it expands fewer nodes to find the optimal solution.")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    run_test_cases()
    compare_heuristics()
    
    print("\n" + "=" * 50)
    print("CONCLUSION:")
    print("A* with an admissible heuristic (Manhattan Distance) finds")
    print("the optimal solution efficiently. It is complete and optimal.")
    print("=" * 50)