def win_condition(board,mark,size):
    
    for r in range(size):
        win = True
        for c in range(size):
            if board[r][c] != mark:
                win = False
                break
        if win:
            return True
        
        for c in range(size):
            win = True

def ask_mark():
    while True:
        p1 = input("Player 1, Choose your mark: ").strip()
        if len(p1) == 1:
            break

    while True:
        p2 = input(f"Player 2, Choose your mark, different from {p1}: ")
        if len(p2) != 1:
            continue
        if p1 == p2:
            continue
        return p1, p2

def ask_board_size():
    while True:
        size = int(input("Enter board size n for n x n board (3-10): "))
        if 3 <= size <= 10:
            return size


def create_board(size):
    board = []
    num = 1
    for r in range(size):
        row = []
        for c in range(size):
            row.append(str(num))
            num+=1
        board.append(row)
    return board

def print_board(board):
    size = len(board)
    cell_width = len(str(size * size))

    for r in range(size):
        line = ""
        for c in range(size):
            cell = board[r][c]
            cell = cell.rjust(cell_width)
            line += cell
            if c < size - 1:
                line += " | "
        print(line)
        if r < size - 1:
            sep = ("-" * cell_width)
            sep_line = sep
            for c in range(size - 1):
                sep_line += "-+-" + sep
            print(sep_line)

def board_is_full(board):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c].isdigit():
                return False
    return True

def read_move(player_name, size):
    while True:
        move = input(f"{player_name}, enter your move (1-{size*size}): ").strip()
        if move.isdigit():
            n = int(move)
            if 1 <= n <= size*size:
                return move
        print("Invalid input, try again.")
            
def make_move(board, move, mark):
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == str(move):   
                board[r][c] = mark        
                return True               
    return False           

def take_turn(player_name, mark, board):
    size = len(board)
    while True:
        move = read_move(player_name, size)     
        ok = make_move(board, move, mark)       
        if ok:
            return
        else:
            print("Cell already taken. Choose another number.")

def tic_tac_toe():
    size = ask_board_size()
    board = create_board(size)
    p1, p2 = ask_mark()
    mark = {"Player 1": p1,"Player 2":p2}
    current = "Player 1"
    print_board(board)
    while True:
        print(f"\n{current} plays ({mark[current]})")
        take_turn(current, mark[current], board)  
        print_board(board)

        if board_is_full(board):
            print("\nBoard full. Game over!")
            break
        if current == "Player 1":
            current = "Player 2"
        else:
            current = "Player 1"

# Main part

tic_tac_toe()