# Winning Rows are

# Top
# Top Left
# Top Middle
# Top Right

# 

# Center
# Bottom

def board_dimensions():
    dimension_str = input("Input dimension of the board: ")
    

def player_turn(turn):
    if turn == "":
        selected_str = input("X position: ")
    else:
        selected_str = input("O position: ")
    return int(selected_str)

def board_selection(position):
    return ""