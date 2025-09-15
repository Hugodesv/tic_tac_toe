
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
        if size >= 3 and size <= 10:
            return size


def board(size):
    cells = []
    count = 1
    for row in range(size):
        row = []
        for col in range(size):
            row.append(count)
            count += 1
    return cells



#### Main part
size = ask_board_size()
startboard = board(size)
print(startboard)
mark = {"Player 1":"","Player 2":""}
p1,p2 = ask_mark()
mark["Player 1"] = p1
mark["Player 2"] = p2
print(mark)