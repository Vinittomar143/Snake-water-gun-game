import random

list1 = ["snake", "gun", "water"]

print("Welcome to the game of snake, water, and gun")
print("You have to choose one of the three options:\nsnake\nwater\ngun")
print("Type 'exit' to quit the game.")

win_rounds = 3

user_wins = 0
computer_wins = 0

while True:
  computer = random.choice(list1)
  user = input("Your Choice: ")

  if user.lower() == "exit":
    break

  if user.lower() in list1:
    print(f"Computer Choose: {computer}")

    if user == computer:
      print("Ah! it's a draw🤝")
    elif user == "snake" or computer == "gun":
        print("Alas! you lose👎")
        computer_wins += 1
    elif user == "water" or computer == "snake":
        print("Alas! you lose👎")
        computer_wins += 1
    elif user == "gun" or computer == "water":
        print("Alas! you lose👎")
        computer_wins += 1
    else:
      print("Hurray! you won👍")
      user_wins += 1

    
    if user_wins == win_rounds:
      print(f"🎉🎉🎉Congratulations!\nYou won the game with {user_wins} rounds!")
      break
    elif computer_wins == win_rounds:
      print(f"😢😢😢The computer won the game with {computer_wins} rounds!")
      break

  else:
    print("Invalid choice. Please choose from: 🐍, 💧, or 🔫, or type 'exit' to quit.")
