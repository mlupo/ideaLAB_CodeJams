import random

PlayerName = input("Hello friend, what is your name? ") # take in the Player's name

print("Hi there " + PlayerName + ", guess a number from 1 to 10")

number = random.randint(1, 10) # random number generated here

tries = 3
PlayerAttempt = 1

win = False

while PlayerAttempt <= tries: 
    PlayerGuess = int(input("Guess a number: "))
    if PlayerGuess == number:
        print("You win!!!!")
        print("Woo!")
        win = True
        break
    elif PlayerGuess < number: # fancy way to say else if
        PlayerAttempt += 1
        print("Oh, sorry... that was too low")
    elif PlayerGuess > number: # fancy way to say else if
        PlayerAttempt += 1
        print("Oh, sorry... that was too high")

if win:
    print("congrats, " + PlayerName + " you are totally right!")
else:
    print("Ouch, " + PlayerName + " you lost :(")
    print("The number was: " + str(number))
