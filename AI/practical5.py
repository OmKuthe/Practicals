"""
Experiment 5: N-Queens Problem using CSP
Backtracking with MRV Heuristic and Forward Checking
"""

import copy


def solve_n_queens(N):
    """Main function to solve N-Queens problem"""
    domains = {row: set(range(N)) for row in range(N)}
    assignment = {}
    nodes_expanded = [0]  # Use list for mutable counter
    
    result = backtracking_search(assignment, domains, N, nodes_expanded)
    return result, nodes_expanded[0]


def is_consistent(row, col, assignment):
    """Check if placing a queen at (row, col) conflicts with existing queens"""
    for r, c in assignment.items():
        # Same column or same diagonal
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def forward_checking(row, col, assignment, domains, N):
    """
    Remove values from future variables' domains that conflict with current assignment
    Returns False if any domain becomes empty (dead end)
    """
    for next_row in range(N):
        if next_row not in assignment:
            # Calculate conflicting columns
            conflicts = {col}
            conflicts.add(col + (next_row - row))   # Diagonal down-right
            conflicts.add(col - (next_row - row))   # Diagonal down-left
            
            # Remove conflicts from domain
            original_size = len(domains[next_row])
            domains[next_row] = {v for v in domains[next_row] 
                                 if 0 <= v < N and v not in conflicts}
            
            # If domain becomes empty, forward checking fails
            if len(domains[next_row]) == 0 and original_size > 0:
                return False
    
    return True


def backtracking_search(assignment, domains, N, nodes_expanded):
    """Recursive backtracking with MRV and forward checking"""
    nodes_expanded[0] += 1
    
    # Goal test: all rows assigned
    if len(assignment) == N:
        return copy.deepcopy(assignment)
    
    # MRV Heuristic: choose row with smallest domain
    unassigned = [r for r in range(N) if r not in assignment]
    row = min(unassigned, key=lambda r: len(domains[r]))
    
    # Try each column in domain (ordered for determinism)
    for col in sorted(domains[row]):
        if is_consistent(row, col, assignment):
            # Make assignment
            assignment[row] = col
            
            # Save domains for backtracking
            original_domains = copy.deepcopy(domains)
            
            # Apply forward checking
            if forward_checking(row, col, assignment, domains, N):
                result = backtracking_search(assignment, domains, N, nodes_expanded)
                if result:
                    return result
            
            # Backtrack
            del assignment[row]
            domains.update(original_domains)
    
    return None


def print_board(solution, N):
    """Print chessboard representation of solution"""
    if not solution:
        print("No solution found!")
        return
    
    print("\n" + "─" * (N * 4 + 1))
    for i in range(N):
        row_str = "│"
        for j in range(N):
            if solution.get(i) == j:
                row_str += " Q │"
            else:
                row_str += "   │"
        print(row_str)
        print("─" * (N * 4 + 1))


def print_statistics(solution, N, nodes_expanded):
    """Print solution statistics"""
    if solution:
        print(f"\n✓ Solution found for {N}-Queens!")
        print(f"  Assignment (row → column): {solution}")
        print(f"  Nodes expanded: {nodes_expanded}")
        print_board(solution, N)
        
        # Verify solution
        valid = verify_solution(solution, N)
        print(f"  Solution valid: {valid}")
    else:
        print(f"\n✗ No solution found for {N}-Queens!")
        print(f"  Nodes expanded: {nodes_expanded}")


def verify_solution(solution, N):
    """Verify that a solution satisfies all constraints"""
    if len(solution) != N:
        return False
    
    for r1, c1 in solution.items():
        for r2, c2 in solution.items():
            if r1 != r2:
                if c1 == c2 or abs(r1 - r2) == abs(c1 - c2):
                    return False
    return True


def min_conflicts_heuristic(N, max_steps=1000):
    """
    Alternative: Min-Conflicts Hill Climbing for N-Queens
    Much faster for large N (can solve 1000+ queens)
    """
    import random
    
    # Initialize: place one queen per row in random columns
    queens = [random.randint(0, N-1) for _ in range(N)]
    
    def count_conflicts(queens, row, col):
        """Count conflicts for a queen at (row, col)"""
        conflicts = 0
        for r in range(N):
            if r != row:
                if queens[r] == col or abs(r - row) == abs(queens[r] - col):
                    conflicts += 1
        return conflicts
    
    for step in range(max_steps):
        # Find rows with conflicts
        conflicted_rows = [r for r in range(N) 
                          if count_conflicts(queens, r, queens[r]) > 0]
        
        if not conflicted_rows:
            # Convert to dictionary format
            solution = {r: queens[r] for r in range(N)}
            return solution, step
        
        # Pick random conflicted row
        row = random.choice(conflicted_rows)
        
        # Find column with minimum conflicts
        current_conflicts = count_conflicts(queens, row, queens[row])
        best_col = queens[row]
        best_conflicts = current_conflicts
        
        for col in range(N):
            if col != queens[row]:
                conflicts = count_conflicts(queens, row, col)
                if conflicts < best_conflicts:
                    best_conflicts = conflicts
                    best_col = col
        
        queens[row] = best_col
    
    return None, max_steps


# ============================================
# TEST CASES
# ============================================

def run_test_cases():
    """Run N-Queens for multiple values of N"""
    test_cases = [4, 5, 6, 8, 10]
    
    for N in test_cases:
        print("\n" + "=" * 50)
        print(f"Solving {N}-Queens Problem")
        print("=" * 50)
        
        solution, nodes = solve_n_queens(N)
        print_statistics(solution, N, nodes)


def compare_algorithms():
    """Compare backtracking vs min-conflicts"""
    N = 20
    
    print("\n" + "=" * 50)
    print(f"ALGORITHM COMPARISON for {N}-Queens")
    print("=" * 50)
    
    # Backtracking
    print("\n--- Backtracking with MRV + FC ---")
    import time
    start = time.time()
    solution, nodes = solve_n_queens(N)
    backtracking_time = time.time() - start
    
    if solution:
        print(f"  Time: {backtracking_time:.3f} seconds")
        print(f"  Nodes expanded: {nodes}")
    else:
        print(f"  No solution found within reasonable time")
    
    # Min-Conflicts
    print("\n--- Min-Conflicts Hill Climbing ---")
    start = time.time()
    solution, steps = min_conflicts_heuristic(N)
    mc_time = time.time() - start
    
    if solution:
        print(f"  Time: {mc_time:.3f} seconds")
        print(f"  Steps taken: {steps}")
    else:
        print(f"  No solution within max steps")
    
    print("\nCONCLUSION: For large N, Min-Conflicts is much faster,")
    print("but backtracking guarantees solution (though slower).")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    run_test_cases()
    compare_algorithms()
    
    print("\n" + "=" * 50)
    print("CONCLUSION:")
    print("Backtracking with MRV and Forward Checking efficiently solves")
    print("N-Queens for N up to ~30. For larger N, use Min-Conflicts.")
    print("=" * 50)