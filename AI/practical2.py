"""
Experiment 2: Problem Formulation and Uninformed Search
Missionaries and Cannibals Problem solved using BFS
"""

from collections import deque

# Possible boat moves (missionaries, cannibals)
MOVES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]


def is_valid(m, c):
    """
    Check if a state satisfies constraints.
    On each bank, if there is at least one missionary,
    cannibals cannot outnumber missionaries.
    """
    # Bounds check
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    
    # Bank A constraint
    if m > 0 and m < c:
        return False
    
    # Bank B constraint
    bm, bc = 3 - m, 3 - c
    if bm > 0 and bm < bc:
        return False
    
    return True


def successors(state):
    """Generate all valid next states"""
    m, c, boat = state
    next_states = []
    
    for dm, dc in MOVES:
        if boat == 'A':
            # Moving from A to B: subtract from A
            new_state = (m - dm, c - dc, 'B')
        else:
            # Moving from B to A: add to A
            new_state = (m + dm, c + dc, 'A')
        
        if is_valid(new_state[0], new_state[1]):
            next_states.append(new_state)
    
    return next_states


def goal_test(state):
    """Check if we've reached the goal (all on Bank B)"""
    return state[0] == 0 and state[1] == 0


def bfs():
    """Breadth-First Search to find shortest solution"""
    start = (3, 3, 'A')
    queue = deque([(start, [])])
    visited = set()
    nodes_expanded = 0
    
    print("Searching for solution...\n")
    
    while queue:
        state, path = queue.popleft()
        nodes_expanded += 1
        
        if goal_test(state):
            print(f"Nodes expanded: {nodes_expanded}")
            return path + [state]
        
        if state in visited:
            continue
        
        visited.add(state)
        
        for s in successors(state):
            if s not in visited:
                queue.append((s, path + [state]))
    
    return None


def print_solution(solution):
    """Print the solution path in readable format"""
    print("\n" + "=" * 50)
    print("SOLUTION FOUND!")
    print("=" * 50)
    
    for i, state in enumerate(solution):
        m, c, boat = state
        bm, bc = 3 - m, 3 - c
        print(f"\nStep {i}:")
        print(f"  Bank A: {m} missionaries, {c} cannibals")
        print(f"  Bank B: {bm} missionaries, {bc} cannibals")
        print(f"  Boat is on Bank {boat}")
        
        # Visual representation
        print(f"  {'M'*m}{'C'*c:<8} |{'~~' if boat=='A' else '  '}~~{'~~' if boat=='B' else '  '}| {'M'*bm}{'C'*bc}")
    
    print(f"\nTotal moves: {len(solution) - 1}")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("MISSIONARIES AND CANNIBALS PROBLEM")
    print("=" * 50)
    print("\nProblem: 3 missionaries and 3 cannibals must cross a river.")
    print("Constraints: Cannibals cannot outnumber missionaries on either bank.")
    print("Boat capacity: 2 people maximum.\n")
    
    solution = bfs()
    
    if solution:
        print_solution(solution)
    else:
        print("No solution exists!")
    
    print("\n" + "=" * 50)
    print("CONCLUSION:")
    print("BFS guarantees the shortest solution (minimum number of crossings).")
    print("The solution has 11 steps including the initial state.")
    print("=" * 50)