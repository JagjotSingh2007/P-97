import os
number = 5
guess = ""
chances = 5
print("NUMBER GUESSING GAME")
print("GUESS A NUMBER (BETWEEN 1 AND 9)")
print("YOU HAVE FIVE CHANCES")
Guess = input("ENTER YOUR GUESS")
if guess !== number :
    print("CLOSE YET FAR")
    break
    while chances < 5 :
        chances = chances-1
if guess === number :
    print("CONGRATULATIONS YOU WIN")
    break

if not chances <  5 :
    print("YOU LOSE!!, THE NUMEBER IS " , number)