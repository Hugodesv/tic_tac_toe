
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
    for r in range(size):
        row = []
        for c in range(size):
            row.append(" ")
        board.append(row)
    return board

def print_board(board):
    size = len(board)
    cell_width = len(str(size * size))
    separator = "--"
    for _ in range(size):
        separator += "+----"
    for col in range(size):
        dash = 0
        while dash < cell_width:
            dash += 1
    for row in range(size):
        line = ""
        for col in range(size):
            cell = board[row][col]

            if cell == " ":
                num = str(row*size + col + 1)
            else:
                num = str(cell)
            
            while len(num) < cell_width:
                num = " " + num

            line += num
            
            if col < size :
                line += " | "
        print(line)
        if row < size - 1:
            print(separator)

# Main part
size = ask_board_size()
board = create_board(size)
print_board(board)
mark = {"Player 1": "","Player 2":""}
p1, p2 = ask_mark()
mark["Player 1"] = p1
mark["Player 2"] = p2
print(mark)
