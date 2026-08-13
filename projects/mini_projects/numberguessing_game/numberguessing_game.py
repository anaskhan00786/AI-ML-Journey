secret_number=25
while True:
    guess=int(input("Enter your guess: "))
    if guess==secret_number:
        break
    elif(guess>secret_number):
        print("Guess is too high!")
    else:
        print("Guess is too low!")