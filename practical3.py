"""
Experiment 3: 8-Puzzle Problem using Steepest Ascent Hill Climbing
"""

import copy

# Goal state
GOAL = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]]


def heuristic(state):
    """
    Misplaced tiles heuristic (ignores blank tile 0)
    Lower value = closer to goal
    """
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL[i][j]:
                h += 1
    return h


def find_blank(state):
    """Find the position of the blank tile (0)"""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return -1, -1


def generate_neighbors(state):
    """Generate all valid neighbor states by moving the blank tile"""
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = copy.deepcopy(state)
            # Swap blank with adjacent tile
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    
    return neighbors


def print_state(state, step_num=None):
    """Pretty print a puzzle state"""
    if step_num is not None:
        print(f"\nStep {step_num} (h = {heuristic(state)}):")
    for row in state:
        print(" ".join(str(tile) if tile != 0 else '_' for tile in row))
    print()


def steepest_ascent_hill_climbing(initial_state, max_iterations=100):
    """
    Steepest Ascent Hill Climbing algorithm
    Returns: (final_state, success, steps_taken)
    """
    current = copy.deepcopy(initial_state)
    current_h = heuristic(current)
    steps = 0
    
    print("=" * 50)
    print("STEEPEST ASCENT HILL CLIMBING FOR 8-PUZZLE")
    print("=" * 50)
    print_state(current, 0)
    
    while steps < max_iterations:
        neighbors = generate_neighbors(current)
        
        if not neighbors:
            print("No neighbors available!")
            return current, False, steps
        
        # Find best neighbor (lowest heuristic)
        best_neighbor = min(neighbors, key=heuristic)
        best_h = heuristic(best_neighbor)
        
        # Stopping conditions
        if current_h == 0:
            print(f"\n✓ GOAL REACHED at step {steps}!")
            return current, True, steps
        
        if best_h > current_h:
            print(f"\n✗ LOCAL MAXIMUM encountered at step {steps}")
            print(f"  Current h = {current_h}, best neighbor h = {best_h}")
            return current, False, steps
        
        if best_h == current_h:
            print(f"\n✗ PLATEAU encountered at step {steps}")
            print(f"  All neighbors have same heuristic value h = {current_h}")
            return current, False, steps
        
        # Move to better neighbor
        current = best_neighbor
        current_h = best_h
        steps += 1
        print_state(current, steps)
    
    print(f"\n✗ MAXIMUM ITERATIONS ({max_iterations}) reached")
    return current, False, steps


# ============================================
# TEST CASES
# ============================================

def run_test_cases():
    test_cases = [
        {
            "name": "Easy - 1 move from goal",
            "state": [[1, 2, 3],
                      [4, 5, 6],
                      [7, 0, 8]]
        },
        {
            "name": "Medium - Requires 2 moves",
            "state": [[1, 2, 3],
                      [4, 0, 6],
                      [7, 5, 8]]
        },
        {
            "name": "Hard - May get stuck",
            "state": [[2, 4, 3],
                      [1, 0, 6],
                      [7, 5, 8]]
        }
    ]
    
    for test in test_cases:
        print("\n" + "#" * 50)
        print(f"TEST CASE: {test['name']}")
        print("#" * 50)
        
        final_state, success, steps = steepest_ascent_hill_climbing(test['state'])
        
        print("\n" + "-" * 30)
        print("RESULT:")
        if success:
            print(f"✓ SUCCESS! Solved in {steps} steps")
        else:
            print(f"✗ FAILED! Stuck after {steps} steps")
        print("-" * 30)


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    run_test_cases()
    
    print("\n" + "=" * 50)
    print("CONCLUSION:")
    print("Hill Climbing is simple and efficient but not complete.")
    print("It can get stuck in local maxima or plateaus.")
    print("Success depends heavily on the initial state.")
    print("=" * 50)