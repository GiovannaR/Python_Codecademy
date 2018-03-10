"""
*Author: Giovanna Avila Riqueti
*Version 1 02/24/2018
"""

print "Scrabble is a game where players get points by spelling words. Words are scored by adding together the point values of each individual letter. Each players write two words and the one with the best score wins the battle.\n"

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
def scrabble_score(word):
    word = word.lower()
    total = 0
    for letter in word:
        for leter in score:
            if letter == leter:
                total = total + score[leter]
    
    return total


def start_thegame():
    sum1 = 0
    sum2 = 0
    
    for turn in range(4):
        if turn % 2 == 0:
            word = raw_input("Write a word, player one\n")
            value = scrabble_score(word)
            sum1 = sum1 + value
        else:
            word1 = raw_input("Write a word, player two\n")
            value = scrabble_score(word1)
            sum2 = sum2 + value

    if sum1 == sum2:
        print "it is a tie"
    elif sum1 > sum2:
        print "Player one is the winner!" 
    elif sum2 > sum1:
        print "Player two is the winner!" 


start_thegame()