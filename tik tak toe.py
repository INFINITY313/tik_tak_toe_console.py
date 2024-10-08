def check_winner():
    if area_board [0][0] ==  area_board [0][1] ==  area_board [0][2] != "*":
        return area_board[0][0]
    
    if area_board [1][0] ==  area_board [1][1] ==  area_board [1][2] != "*":
        return area_board[1][0] 

    if area_board [2][0] ==  area_board [2][1] ==  area_board [2][2] != "*":
        return area_board[2][0] 

    if area_board [0][0] ==  area_board [1][0] ==  area_board [2][0] != "*":
        return area_board[0][0]

    if area_board [0][1] == area_board [1][1] ==    area_board [2][1] != "*":
        return area_board[0][1] 

    if area_board [0][2] ==  area_board [1][2] ==  area_board [2][2] != "*":
        return area_board[0][2]

    if area_board [0][0] ==  area_board [1][1] ==  area_board [2][2] != "*":
        return area_board[0][0] 

    if area_board [2][1] ==  area_board [1][1] ==  area_board [0][2] != "*":
        return area_board[2][1]
    

    # if area_board [0][0] == "0" and area_board [0][1] == "0" and area_board [0][2] == "0":
    #     return "0"
    
    # if area_board [1][0] == "0" and area_board [1][1] == "0" and area_board [1][2] == "0":
    #     return "0"

    # if area_board [2][0] == "0" and area_board [2][1] == "0" and area_board [2][2] == "0":
    #     return "0"

    # if area_board [0][0] == "0" and area_board [1][0] == "0" and area_board [2][0] == "0":
    #     return "0"

    # if area_board [0][1] == "0" and area_board [1][1] == "0" and area_board [2][1] == "0":
    #     return "0"

    # if area_board [0][2] == "0" and area_board [1][2] == "0" and area_board [2][2] == "0":
    #     return "0"

    # if area_board [0][0] == "0" and area_board [1][1] == "0" and area_board [2][2] == "0":
    #     return "0"

    # if area_board [2][1] == "0" and area_board [1][1] == "0" and area_board [0][2] == "0":
    #     return "0"

def restart():
    global turns
    turns = 1
    global area_board 
    area_board = [["*","*","*"],
                 ["*","*","*"],
                 ["*","*","*"]]
    return input("do you want to restart the game?") == "yes"

area_board = [["*","*","*"],
              ["*","*","*"],
              ["*","*","*"]]
#area_board [1][1] = "X"
#area_board [2][2] = "X"
for line in area_board:
    print(line)
turns = 1
symbol = ""
while True:
    if turns %2 == 1:
        print("move of X")
        symbol = "X"
    else:
        print("move of 0")
        symbol = "0"

    row = int(input("enter a row number. "))
    if row  >2:
        print("error please print number between 0-2")
        continue
    col = int(input("enter a column number. "))
    if col  >2:
        print("error please print number between 0-2")
        continue
    if area_board [row][col] == "*":
        area_board [row][col] = symbol
    else:
        print("error,please pick another cell")
        continue
    turns +=1
    for line in area_board:
        print(line)
    if check_winner() == "X":
        print("X winner")
        if restart():
            continue
        else:
            break
    elif check_winner() == "0":
        print("0 winner")
        break
    elif turns == 9:
        print("draw")
        break