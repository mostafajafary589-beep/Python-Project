import random

def play():
    secret = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Guess The Number (1-100): "))
        except ValueError:
            print("Please Enter The Right Number :!")
            continue
        attempts += 1
        if guess < secret:
            print("The Biggest")
        elif guess > secret:
            print("The Smallest")
        else:
            print(f"Right during {attempts} attempts")
            break

play()