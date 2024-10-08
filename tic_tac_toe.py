from numpy import random
import time
import sys

move = [" "," "," "," "," "," "," "," "," "]

print(f'''

      {move[0]} | {move[1]} | {move[2]}
    -------------
      {move[3]} | {move[4]} | {move[5]}
    -------------
      {move[6]} | {move[7]} | {move[8]}
    
''')

h_turn = "X"
c_turn = "O"

def human():

    while 1:
        loc_index = int(input(f"{h_turn} Turn Enter the location 0-8 : "))
    
        if  move[loc_index] != " " :
            print(f"Location is already in used by {move[loc_index]}. Please try another one !!")
            continue
        elif loc_index > 9 :
            print("location does not exist !!")
            continue
        else:
            move[loc_index] = "X"
            break

def com():

    while 1:
        com_index = random.randint(9)
        print("Computer choosen Index : ", com_index)
        if  move[com_index] != " " :
            print(f"Location is already in used by {move[com_index]}. Please try another one !!")
            time.sleep(0.5)
            continue
        elif com_index > 9 :
            print("location does not exist !!")
            time.sleep(0.5)
            continue
        else:
            move[com_index] = "O"
            break

def print_board():
    print(f'''

      {move[0]} | {move[1]} | {move[2]}
    -------------
      {move[3]} | {move[4]} | {move[5]}
    -------------
      {move[6]} | {move[7]} | {move[8]}
    
''')

def win():
    
        if ' ' not in move:
            print("TIE")
            sys.exit()

        if move[0] == move[1] == move[2] != " ":
            print(move[0], 'Win')
            sys.exit()
    
        if move[0] == move[4] == move[8] != " ":
            print(move[0], 'Win')
            sys.exit()
        
        if move[0] == move[3] == move[6] != " ":
            print(move[0], 'Win')
            sys.exit()
        
        if move[1] == move[4] == move[7] != " ":
            print(move[1], 'Win')
            sys.exit()
        
        if move[2] == move[5] == move[8] != " ":
            print(move[2], 'Win')
            sys.exit()

        if move[3] == move[4] == move[5] != " ":
            print(move[3], 'Win')
            sys.exit()

        if move[6] == move[7] == move[8] != " ":
            print(move[6], 'Win')
            sys.exit()

        if move[2] == move[4] == move[6] != " ":
            print(move[6], 'Win')
            sys.exit()
        
def run():

    while 1:
        human()
        print_board()
        win()
        time.sleep(1)
        com()
        print_board()   
        win()


run()
