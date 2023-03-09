logo="""
  _   _                 _                  _____                     _                _____                      
 | \ | |               | |                / ____|                   (_)              / ____|                     
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ _ _ __   __ _  | |  __  __ _ _ __ ___   ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __| | '_ \ / _` | | | |_ |/ _` | '_ ` _ \ / _ \
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \ | | | | (_| | | |__| | (_| | | | | | |  __/
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/_|_| |_|\__, |  \_____|\__,_|_| |_| |_|\___|
                                                                              __/ |                              
                                                                             |___/                               
"""
print(logo)
import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number=random.randint(1,100)
print(number)
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=='easy':
    attempts=10
elif difficulty=='hard':
    attempts=5
to_continue=True
while to_continue:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess==number:
        to_continue=False
        print(f"You have guessed the number {number} in {attempts} attempts. Congratulations!")
        break
    if attempts<=1:
        to_continue=False
        print(f"The number is {number}. You lost!")
        break
    if guess>number:
        print("Too high.")
        print("Guess again.")
    elif guess<number:
        print("Too low.")
        print("Guess again.")  
    attempts-=1
    
