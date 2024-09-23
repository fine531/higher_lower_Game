from art import logo, vs
from game_data import data
import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the function to clear the console
clear_console()

# Print the logo
print(logo)

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Generate random accounts from the game data.
account_1 = random.choice(data)
account_2 = random.choice(data)

# Ensure account_1 and account_2 are different
while account_1 == account_2:
    account_2 = random.choice(data)

score = 0
while True:
    print(f"Compare A: {format_data(account_1)}")
    print(vs)
    print(f"Against B: {format_data(account_2)}")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers = account_1["follower_count"]
    b_followers = account_2["follower_count"]

    if check_answer(guess, a_followers, b_followers):
        score += 1
        print(f"You are right! Current score: {score}")
        account_1 = account_2
        account_2 = random.choice(data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
