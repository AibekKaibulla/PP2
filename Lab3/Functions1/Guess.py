import random
def guessGame():
    guessNumber=random.randint(1, 20)
    tries=0
    num=0
    name=input("Hello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of number between 1 and 20.")
    while(num!=guessNumber):
        num=int(input("Take a guess\n"))
        tries+=1
        if(num<guessNumber):
            print("\nYour guess is too low.")
        elif(num>guessNumber):
            print("\nYour guess is too big.")
    print(f"Good job, {name}! You guessed my number in {tries} guesses!")

guessGame()