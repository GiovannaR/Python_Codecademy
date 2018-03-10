"""
*Author: Giovanna Avila Riqueti
*Version 1 02/23/2018
"""

from random import randint

board = []

#Initializing board with 0s
for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

#####################################################################

#Generating a random position in the board to be the chosen one 
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

#####################################################################


def start_thegame(board):

  #Generating the answer
  ship_row = random_row(board)
  ship_col = random_col(board)

  print "This is a traditional battleship game with two players and four chances for each one"

  for turn in range(8):

    print_board(board)

    if turn % 2 == 0:
      print "Player one, please choose one row and one col"
    else:
      print "Player two, please choose one row and one col"
  
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
    
      if turn % 2 == 0:
        print "Congratulations, Player one, You sunk my battleship!"
      else:
        print "Congratulations, player two! You sunk my battleship!"

      break

    elif guess_row not in range(5) or guess_col not in range(5):
      print "Oops, that's not even in the ocean."

    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."

    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"



start_thegame(board)
      
