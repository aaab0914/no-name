# 2. Number Guessing Game
import random
while True:
    print("\n=== Number Guessing Game ===")
    secret = random.randint(1, 10)
    attempts = 0
    
    while True:
        guess = int(input("Guess number (1-10): "))
        attempts += 1
        
        if guess == secret:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break
        elif guess < secret:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
            
    if input("Play again? (y/n): ").lower() != 'y':
        print("Thank for playing!")
        break
        