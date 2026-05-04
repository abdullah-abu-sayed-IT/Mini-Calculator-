import random

def guessing_game():
    print("--- Guessing Game ---")
    number = random.randint(1, 10)
    print("Ami 1 theke 10 er moddhe ekta number bhebechi. Bolo to seta koto?")
    
    while True:
        try:
            guess = int(input("Tomar guess: "))
            
            if guess < number:
                print("Areh na! Arektu boro number bolo.")
            elif guess > number:
                print("Beshi boro hoye gelo! Choto kichu bolo.")
            else:
                print(f"Ere baap re! Tumi to jene gele! Thik dhorecho, number-ti chilo {number}.")
                break
        except ValueError:
            print("Shudhu number likho bondhu!")

guessing_game()
