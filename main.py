from art import logo, vs
from game_data import data
import random
compare_a = random.choice(data)
agaisnt_b = random.choice(data)
player_score = 0
correct_answer = None

def clear_screen():
    print("\n"*80)
def print_player(player):
    return f"{player['name']}, {player['description']}, from {player['country']}"


def check_winner(user_choice):
    if user_choice == 'A':
        if compare_a['follower_count'] > agaisnt_b['follower_count']:
            return True
        else:
            return False
    elif user_choice == 'B':
        if agaisnt_b['follower_count'] > compare_a['follower_count']:
            return True
        else:
            return False
def winner():
    global correct_answer
    global player_score
    global compare_a
    global agaisnt_b

    correct_answer = True
    player_score += 1
    compare_a = agaisnt_b
    agaisnt_b = random.choice(data)
    clear_screen()

def game():

    while True:
        print(logo)
        if correct_answer:
            print(f"You're right! Current score: {player_score} \n")

        print(f"Compare A: {print_player(compare_a)}")
        print(vs)
        print(f"Agaisnt B: {print_player(agaisnt_b)}")
        user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        if user_choice == 'A':
            if check_winner(user_choice):
                winner()
            else:
                clear_screen()
                print(logo)
                print(f"Sorry that's wrong. final score: {player_score}")
                input_choice = input("Do you still want to play?: Type 'yes' or 'no' ")
                if input_choice == 'yes':
                    game()
                else:
                    print("Thanks for playing!")
                    break
        elif user_choice == 'B':
            if check_winner(user_choice):
                winner()
            else:
                clear_screen()
                print(logo)
                print(f"Sorry that's wrong. final score: {player_score}")
                input_choice = input("Do you still want to play?: Type 'yes' or 'no' ")
                if input_choice == 'yes':
                    game()
                else:
                    print("Thanks for playing!")
                    break
game()