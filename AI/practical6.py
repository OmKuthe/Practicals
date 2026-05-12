"""
Experiment 6: Tic-Tac-Toe using Minimax Algorithm
Perfect AI that never loses
"""

import copy

# Global constants
PLAYER = 'X'      # Maximizing player (AI)
OPPONENT = 'O'    # Minimizing player (Human)


def print_board(board):
    """Pretty print the current board"""
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
    print("-" * 9)
    print()


def is_moves_left(board):
    """Check if there are any empty cells on the board"""
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
    return False


def evaluate(board):
    """
    Evaluate the board.
    Returns:
        +10 if PLAYER (X) wins
        -10 if OPPONENT (O) wins
         0 if draw or no winner yet
    """
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == PLAYER:
                return 10
            elif board[row][0] == OPPONENT:
                return -10
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == PLAYER:
                return 10
            elif board[0][col] == OPPONENT:
                return -10
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == PLAYER:
            return 10
        elif board[0][0] == OPPONENT:
            return -10
    
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == PLAYER:
            return 10
        elif board[0][2] == OPPONENT:
            return -10
    
    return 0


def minimax(board, depth, is_max, alpha=-1000, beta=1000, use_pruning=False):
    """
    Minimax algorithm with optional alpha-beta pruning
    Returns: best score for the current board
    """
    score = evaluate(board)
    
    # Terminal conditions
    if score == 10:
        return score - depth  # Prefer faster wins
    if score == -10:
        return score + depth  # Prefer slower losses (force opponent to win slower)
    if not is_moves_left(board):
        return 0
    
    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = PLAYER
                    best = max(best, minimax(board, depth + 1, False, alpha, beta, use_pruning))
                    board[i][j] = '_'
                    
                    if use_pruning:
                        alpha = max(alpha, best)
                        if beta <= alpha:
                            return best  # Beta cut-off
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = OPPONENT
                    best = min(best, minimax(board, depth + 1, True, alpha, beta, use_pruning))
                    board[i][j] = '_'
                    
                    if use_pruning:
                        beta = min(beta, best)
                        if beta <= alpha:
                            return best  # Alpha cut-off
        return best


def find_best_move(board, use_pruning=False):
    """
    Find the best move for the AI using minimax
    Returns: (row, col, best_score)
    """
    best_val = -1000
    best_move = (-1, -1)
    
    print("AI is evaluating moves...")
    print("-" * 30)
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                # Try the move
                board[i][j] = PLAYER
                move_val = minimax(board, 0, False, -1000, 1000, use_pruning)
                board[i][j] = '_'
                
                print(f"  Move ({i}, {j}) → Score: {move_val}")
                
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    
    print("-" * 30)
    print(f"Best Move: {best_move} with score {best_val}")
    
    return best_move[0], best_move[1], best_val


def is_winner(board, player):
    """Check if the given player has won"""
    # Rows
    for row in range(3):
        if all(board[row][col] == player for col in range(3)):
            return True
    # Columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    """Check if the board is completely filled"""
    return all(board[i][j] != '_' for i in range(3) for j in range(3))


def play_game():
    """Interactive game where player plays against AI"""
    board = [['_' for _ in range(3)] for _ in range(3)]
    ai_starts = input("Should AI start first? (y/n): ").lower() == 'y'
    
    print("\n" + "=" * 40)
    print("TIC-TAC-TOE - You are 'O', AI is 'X'")
    print("Enter moves as row and column numbers (0, 1, or 2)")
    print("=" * 40)
    
    current_player = PLAYER if ai_starts else OPPONENT
    
    while True:
        print_board(board)
        
        if current_player == PLAYER:
            # AI's turn
            print("AI is thinking...")
            row, col, _ = find_best_move(board, use_pruning=True)
            board[row][col] = PLAYER
            print(f"AI plays: ({row}, {col})")
            
            if is_winner(board, PLAYER):
                print_board(board)
                print("🤖 AI WINS! 🤖")
                break
        else:
            # Player's turn
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter col (0-2): "))
                
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input! Enter numbers between 0 and 2.")
                    continue
                
                if board[row][col] != '_':
                    print("That cell is already taken!")
                    continue
                
                board[row][col] = OPPONENT
                
                if is_winner(board, OPPONENT):
                    print_board(board)
                    print("🎉 YOU WIN! 🎉")
                    break
            except ValueError:
                print("Please enter valid numbers!")
                continue
        
        if is_board_full(board):
            print_board(board)
            print("🤝 IT'S A DRAW! 🤝")
            break
        
        # Switch player
        current_player = PLAYER if current_player == OPPONENT else OPPONENT


# ============================================
# TEST CASES
# ============================================

def run_test_cases():
    """Test minimax on predefined board states"""
    test_boards = [
        {
            "name": "AI can win immediately",
            "board": [
                ['x', 'o', 'x'],
                ['o', 'o', 'x'],
                ['_', '_', '_']
            ]
        },
        {
            "name": "Multiple winning moves",
            "board": [
                ['x', '_', '_'],
                ['_', 'o', '_'],
                ['_', '_', 'x']
            ]
        },
        {
            "name": "Block opponent's winning move",
            "board": [
                ['o', 'x', 'o'],
                ['x', 'x', '_'],
                ['_', '_', 'o']
            ]
        }
    ]
    
    print("\n" + "=" * 50)
    print("TESTING MINIMAX ON PRE-DEFINED BOARDS")
    print("=" * 50)
    
    for test in test_boards:
        print(f"\n--- {test['name']} ---")
        board = test['board']
        print_board(board)
        
        row, col, score = find_best_move(board)
        print(f"\nRecommended move: ({row}, {col})")
        print(f"Score: {score}\n")


def compare_without_pruning():
    """Compare minimax with and without alpha-beta pruning"""
    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]
    
    print("\n" + "=" * 50)
    print("COMPARING MINIMAX WITH AND WITHOUT ALPHA-BETA PRUNING")
    print("=" * 50)
    print_board(board)
    
    import time
    
    # Without pruning
    start = time.time()
    _, _, score1 = find_best_move(board, use_pruning=False)
    time1 = time.time() - start
    
    # With pruning
    start = time.time()
    _, _, score2 = find_best_move(board, use_pruning=True)
    time2 = time.time() - start
    
    print(f"\nWithout pruning: {time1:.4f} seconds")
    print(f"With pruning:    {time2:.4f} seconds")
    print(f"Speedup: {time1/time2:.2f}x faster")


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    # Run test cases
    run_test_cases()
    compare_without_pruning()
    
    # Ask if user wants to play
    print("\n" + "=" * 50)
    play = input("Do you want to play against the AI? (y/n): ").lower()
    if play == 'y':
        play_game()
    
    print("\n" + "=" * 50)
    print("CONCLUSION:")
    print("Minimax with alpha-beta pruning finds the optimal move")
    print("and guarantees that the AI will never lose in Tic-Tac-Toe.")
    print("=" * 50)