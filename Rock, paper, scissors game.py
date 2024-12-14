import random 
 
def rock_paper_scissors(): 
    print("Welcome to Rock, Paper, Scissors!") 
    print("Instructions: Choose 'rock', 'paper', or 'scissors' to play against the computer.") 
     
    user_score = 0 
    computer_score = 0 
     
    while True: 
        print("\n--- New Round ---") 
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower() 
        while user_choice not in ['rock', 'paper', 'scissors']: 
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.") 
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower() 
 
        computer_choice = random.choice(['rock', 'paper', 'scissors']) 
        print(f"You chose: {user_choice}") 
        print(f"Computer chose: {computer_choice}") 
 
       # Determine the result
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
         
        # Display scores 
        print(f"Score -> You: {user_score}, Computer: {computer_score}") 
 
        # Ask to play again 
        play_again = input("Do you want to play another round? (yes/no): ").lower() 
        while play_again not in ['yes', 'no']: 
            play_again = input("Invalid response. Do you want to play another round? (yes/no): ").lower() 
        if play_again == 'no': 
            break 
 
    # Final Scores 
    print("\n--- Final Scores ---") 
    print(f"You: {user_score}") 
    print(f"Computer: {computer_score}") 
    if user_score > computer_score: 
        print("Congratulations! You are the overall winner!") 
    elif user_score < computer_score: 
        print("Computer wins the game! Better luck next time!") 
    else: 
        print("It's a tie overall! Great match!") 
    print("Thanks for playing Rock, Paper, Scissors!") 
 
# Run the game 
rock_paper_scissors() 
 