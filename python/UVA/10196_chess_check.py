
import fileinput

SPACE = '.'

WHITE = 'white'

BLACK = 'black'

EMPTY = '.' * 8

file_input = fileinput.input()


def read_board(file_input):
    board = [next(file_input).strip() for i in range(8)]
    if all(map(lambda x: x == EMPTY, board)):
        return None
    else:
        next(file_input) #ignore empty line
        return board


def get_kings_position(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'k':
                black = (i, j)
            elif board[i][j] == 'K':
                white = (i, j)
    return (black, white)


def check_row(board, position, king_position):
    r = position[1]
    k = king_position[1]
    row = position[0]
    if r > k:
        k, r = (r, k)

    if r < k:
        for i in range(r + 1, k):
            if board[row][i] != SPACE:
                return False
        return True
    else:
        raise Exception("Impossible!")


def check_col(board, position, king_position):
    r = position[0]
    k = king_position[0]
    col = position[1]
    if r > k:
        k, r = (r, k)

    if r < k:
        for i in range(r + 1, k):
            if board[i][col] != SPACE:
                return False
        return True
    else:
        raise Exception("Impossible!")


def check_rook_check(board, position, king_position, result):
    if position[0] == king_position[0]:
        if check_row(board, position, king_position):
            return result

    if position[1] == king_position[1]:
        if check_col(board, position, king_position):
            return result

    return False


def diag(position):
    return position[1] - position[0]


def rev_diag(position):
    return position[1] + position[0]


def check_diag(board, position, king_position):
    r = position[0]
    k = king_position[0]
    col = position[1]
    if r > k:
        k, r = (r, k)
        col = king_position[1]

    if r < k:
        for i in range(1, k - r):
            if (r + i) >= 8 or (col + i) >= 8:
                return True

            if board[r + i][col + i] != SPACE:
                return False
        return True
    else:
        raise Exception("Impossible!")


def check_rev_diag(board, position, king_position):
    r = position[0]
    k = king_position[0]
    col = position[1]
    if r > k:
        k, r = (r, k)
        col = king_position[1]

    if r < k:
        for i in range(1, k - r):
            if (col + i) < 0:
                return True
            if board[r + i][col - i] != SPACE:
                return False
        return True
    else:
        raise Exception("Impossible!")


def check_bishop_check(board, position, king_position, result):
    if diag(position) == diag(king_position):
        if check_diag(board, position, king_position):
            return result

    if rev_diag(position) == rev_diag(king_position):
        if check_rev_diag(board, position, king_position):
            return result

    return False


def check_queen_check(board, position, king_position, result):
    return check_bishop_check(board, position, king_position, result) or \
           check_rook_check(board, position, king_position, result)


def check_knight_check(board, position, king_position, result):
    x = abs(king_position[0] - position[0])
    y = abs(king_position[1] - position[1])

    if (x == 1 and y == 2) or (x == 2 and y == 1):
        return result

    return False


def check_black_pawn(board, position, white_king, result):
    if white_king[0] == position[0] + 1:
        if abs(white_king[1] - position[1]) == 1:
            return result

    return False


def check_white_pawn(board, position, black_king, result):
    if black_king[0] == position[0] - 1:
        if abs(black_king[1] - position[1]) == 1:
            return result

    return False


def handle_piece(board, piece, position, black, white):
    if piece == 'r':
        return check_rook_check(board, position, white, WHITE)
    elif piece == 'R':
        return check_rook_check(board, position, black, BLACK)
    elif piece == 'b':
        return check_bishop_check(board, position, white, WHITE)
    elif piece == 'B':
        return check_bishop_check(board, position, black, BLACK)
    elif piece == 'q':
        return check_queen_check(board, position, white, WHITE)
    elif piece == 'Q':
        return check_queen_check(board, position, black, BLACK)
    elif piece == 'n':
        return check_knight_check(board, position, white, WHITE)
    elif piece == 'N':
        return check_knight_check(board, position, black, BLACK)
    elif piece == 'p':
        return check_black_pawn(board, position, white, WHITE)
    elif piece == 'P':
        return check_white_pawn(board, position, black, BLACK)


def check_the_check(board, black, white):
    for i in range(8):
        for j in range(8):
            if board[i][j] != SPACE:
                is_checked = handle_piece(board, board[i][j], (i, j), black, white)
                if is_checked:
                    return is_checked

    return None



def check_board(board):
    # print(board)

    black, white = get_kings_position(board)
    # print(black)
    # print(white)

    return check_the_check(board, black, white)

count = 0
board = read_board(file_input)
while (board):
    count += 1
    result = check_board(board)
    if (result):
        print("Game #{}: {} king is in check.".format(count, result))
    else:
        print("Game #{}: no king is in check.".format(count))
    # print(board)

    board = read_board(file_input)

