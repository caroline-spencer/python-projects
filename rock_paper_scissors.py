# Rock, Paper, Scissors game
import random    # This module imports the Python code for random number generation

wins, ties, losses = 0, 0, 0   # global variables to track number of wins, ties, and losses

# This function defines a loop that iterates as long as the user continues to play.
#    Calls get_choices function to get the player and computer choices.
#    Calls play_game function with the choices to decide the winner/tie
#    Calls display_summary_results function to display total games, wins, losses, and ties
def main():
    play_again = True
    while play_again:
        computer_choice, player_choice = get_choices()
        play_again = play_game(computer_choice, player_choice)
    display_summary_results()


# This function uses the random.choice method to generate the computer's choice (rock, paper, or scissors).
# Prompts the player for their choice.
# If an invalid value is entered, continue to prompt until a valid value is provided.
# Important: Do NOT change the 2 statements provided. You will need to add code to complete the function.
def get_choices():
    valid_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(valid_choices)
    player_choice = input('Enter choice (rock,paper,scissors): ')
    while player_choice != 'rock' and player_choice != 'paper' and player_choice != 'scissors':
        print('Try again. Enter rock, paper, or scissors.')
        player_choice = input('Enter choice (rock,paper,scissors): ')
    return computer_choice, player_choice


# This function determines the winner/tie based on the computer and player's choices that are passed to this function.
# Prints the choices, and checks the possible combinations to determine the winner/tie.
# Prints the result, e.g., 'Computer wins!', 'You win!', or 'it's a tie!'
# Keeps track of the number of wins/losses/ties so far.
def play_game(computer, player):
    print("Your choice: " + player + "\nComputer choice: " + computer)
    global wins
    global ties
    global losses
    if player == 'rock':
        if computer == 'rock':
            print('It\'s a tie!')
            ties = ties + 1
        elif computer == 'paper':
            print('Computer wins!')
            losses = losses + 1
        elif computer == 'scissors':
            print('You win!')
            wins = wins + 1
    elif player == 'paper':
        if computer == 'paper':
            print('It\'s a tie!')
            ties = ties + 1
        elif computer == 'rock':
            print('You win!')
            wins = wins + 1
        elif computer == 'scissors':
            print('Computer wins!')
            losses = losses + 1
    elif player == 'scissors':
        if computer == 'scissors':
            print('It\'s a tie!')
            ties = ties + 1
        elif computer == 'paper':
            print('You win!')
            wins = wins + 1
        elif computer == 'rock':
            print('Computer wins!')
            losses = losses + 1
    keep_playing = input('Play again? (yes/no) ')
    while keep_playing != 'yes' and keep_playing != 'no':
        print('Try again. Enter yes or no.')
        keep_playing = input('Play again? (yes/no) ')
    if keep_playing == 'yes':
        playing_again = True
    elif keep_playing == 'no':
        playing_again = False
    return playing_again


# Once the player has decided to stop playing, display total number of games, wins, losses, and ties
def display_summary_results():
    global wins
    global losses
    global ties
    total_games = wins + losses + ties
    print('You played', total_games, 'games')
    print(wins, 'wins')
    print(losses, 'losses')
    print(ties, 'ties')


main()
