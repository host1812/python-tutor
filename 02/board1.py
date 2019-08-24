def render_cell(c):
    rendered_cell = ""
    rendered_cell += "---\n"
    rendered_cell += "|"+c+"|"
    rendered_cell += "---\n"

    return rendered_cell

def render_row(row):
    rendered_row = "-" * 9 + "\n"
    # rendered_row += "|".join(row)
    # for c in row:
        # rendered_row += "|"+c+"|"
        # rendered_row += "|".join(c)

    print(rendered_row)

def render_board(board):
    # render_cell(board[0][0])
    for row in board:
        render_row(row)
    # rendered_board = ""
    # for row in board:
    #     rendered_board += "|".join(str(row))
    #     rendered_board += "\n"
    #     rendered_board += "-" * 8
    #     rendered_board += "\n"

    # print(rendered_board)

board = [["X" for y in range(3)] for x in range(3)]

render_board(board)