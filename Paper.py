import random

username = input("Rock, Paper, or Scissors? ")

# Generate a random choice for the computer
computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

print(f"Computer chooses {computer_choice}")

if username == 'Rock':
    if computer_choice == 'Paper':
        print("You LOST")
    elif computer_choice == 'Rock':
        print("It's a DRAW")
    else:
          print("You WIN")
elif username == 'Paper':
    if computer_choice == 'Scissors':
        print("You LOST")
    elif computer_choice == 'Paper':
         print("It's a DRAW")
    else:
        print("You WIN")
elif username == 'Scissors':
    if computer_choice == 'Rock':
           print("You LOST")
    elif computer_choice == 'Scissors':
        print("It's a DRAW")
    else:
        print("You WIN")
else:
     print("Invalid choice. Please choose Rock, Paper, or Scissors.")
