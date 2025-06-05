# Michekkle
#A rock, paper, scissors game with a simple AI opponent.

import random  # Import the random module to allow the AI to make random choices

def get_user_choice():
    """
    Prompt the user to enter their choice of 'rock', 'paper', or 'scissors'.
    Continues to prompt until a valid choice is entered.
    Returns the user's validated choice as a string.
    """
    valid_choices = {"rock", "paper", "scissors"}  # Set of valid choices
    user_input = input("Enter rock, paper, or scissors: ").lower()  # Get user input and convert to lowercase
    while user_input not in valid_choices:  # Loop until the input is valid
        print("Invalid choice. Please try again.")  # Inform the user of invalid input
        user_input = input("Enter rock, paper, or scissors: ").lower()  # Prompt again
    return user_input  # Return the valid user choice

def get_ai_choice():
    """
    Randomly select and return the AI's choice of 'rock', 'paper', or 'scissors'.
    """
    return random.choice(["rock", "paper", "scissors"])  # Randomly pick one of the three options

def determine_winner(user_choice, ai_choice):
    """
    Determine the winner of a round based on user and AI choices.
    Returns a string indicating the result: tie, user win, or AI win.
    """
    if user_choice == ai_choice:
        return "It's a tie!"  # Both choices are the same
    # Check all winning conditions for the user
    elif (user_choice == "rock" and ai_choice == "scissors") or \
         (user_choice == "paper" and ai_choice == "rock") or \
         (user_choice == "scissors" and ai_choice == "paper"):
        return "You win!"  # User wins
    else:
        return "AI wins!"  # AI wins

def play_best_of_3():
    """
    Play a best-of-3 series between the user and the AI.
    Tracks and displays the score after each round.
    Declares the overall winner after someone wins 2 rounds.
    """
    user_score = 0  # Initialize user's score
    ai_score = 0    # Initialize AI's score
    round_number = 1  # Track the current round number

    # Continue playing rounds until either the user or AI reaches 2 wins
    while user_score < 2 and ai_score < 2:
        print(f"\nRound {round_number}:")  # Display the round number
        user_choice = get_user_choice()  # Get the user's choice
        ai_choice = get_ai_choice()      # Get the AI's choice
        print(f"You chose: {user_choice}")  # Show user's choice
        print(f"AI chose: {ai_choice}")     # Show AI's choice
        result = determine_winner(user_choice, ai_choice)  # Determine the round result
        print(result)  # Display the result
        if result == "You win!":
            user_score += 1  # Increment user's score if they win
        elif result == "AI wins!":
            ai_score += 1    # Increment AI's score if it wins
        # Ties do not affect the score
        print(f"Score - You: {user_score}, AI: {ai_score}")  # Show current score
        round_number += 1  # Move to the next round

    # After the loop, declare the overall winner
    if user_score == 2:
        print("\nCongratulations! You won the best of 3 series!")  # User wins the series
    else:
        print("\nAI wins the best of 3 series. Better luck next time!")  # AI wins the series

def main():
    """
    Main function to start and manage the game.
    Welcomes the user, starts the first series, and asks if they want to play again.
    """
    print("Welcome to Rock, Paper, Scissors!")  # Greet the user
    play_best_of_3()  # Play the first best-of-3 series
    # Continue playing new series as long as the user wants
    while input("Do you want to play again? (yes/no): ").lower() == "yes":
        play_best_of_3()
    print("Thanks for playing!")  # Thank the user when they are done

if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly


