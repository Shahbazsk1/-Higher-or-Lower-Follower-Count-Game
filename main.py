import random
from game_data import data


# Display art
from art import logo, vs
print(logo)


def format_data(account):
    # format the account data into the printable format
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_des},from {account_country}"


def check_answer(user_guess, a_follower, b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == "b"


score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
     # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


     # Ask user for the guess
    guess = input("Who has more follower? Type 'A' or 'B': ").lower()


     # clear screen
    print("\n" * 5)
    print(logo)

     # check if user is correct
     # - Get follower count of each account
    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower, b_follower)
     # - use if statement to check if user is correct

     # Give user feedback on their guess
    if is_correct:
        score += 1
        print(f"You are right! current score: {score}")
    else:
        print(f"Your are wrong. final score: {score} ")
        game_should_continue = False


 # Score Keeping

 # Make the game repeatable

 # making account at position B become the next account at position A.