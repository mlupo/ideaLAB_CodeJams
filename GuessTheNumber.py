import random # external modules

PlayerName = input("Hello friend, what is you name? ")

number = random.randint(1, 10) # random number generation
Tries = 3
PlayerAttempt = 1

win = False

print("Hi there", PlayerName, "let's get ready to guess numbers!!!") # show name

while PlayerAttempt <= Tries: # indentation reminder
    PlayerGuess = int(input("Guess a number: ")) # take the Player's guess
    if PlayerGuess == number: # Boolean logic
        win = True
        break
    elif PlayerGuess < number: # fancy else if!
        PlayerAttempt += 1 # increment the attempts
        print("OH! That's too low!")
    elif PlayerGuess > number:
        PlayerAttempt += 1 # increment the attempts
        print("OH! That's too high!")

if win:
    print("Great job! You're right", PlayerName, "...the number was:", number)
else:
    print("I'm so sorry", PlayerName, "...the number was:", number)
