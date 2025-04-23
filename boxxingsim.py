import random

print("Welcome to your next boxing round, Champion!")

moves = {
    1: "The Jab",
    2: "The Cross",
    3: "The Lead Hook",
    4: "The Rear Hook",
    5: "The Lead Uppercut",
    6: "The Rear Uppercut"
}

winning_rules = {
    1: 3, 2: 1, 3: 5, 4: 2, 5: 6, 6: 4   
}

loosing_rules = {
    1: 5, 2: 3, 3: 6, 4: 2, 5: 4, 6: 1   
}

print("\nChoose your move:")
for number, name in moves.items():
    print(f"{number}: {name}")

try:
    player_move = int(input("Enter the number of your move (1-6): "))
    if player_move not in moves:
        print("Invalid move! Try again with a number between 1 and 6.")
        exit()
except ValueError:
    print("Invalid input! Please enter a number between 1 and 6.")
    exit()

opponent_move = random.randint(1, 6)
print(f"\nYou chose: {moves[player_move]}")
print(f"Opponent chose: {moves[opponent_move]}")

if player_move == opponent_move:
    print("It's a tie!")
elif winning_rules[player_move] == opponent_move:
    print("You win this round!")
elif winning_rules[opponent_move] == player_move:
    print("Opponent wins this round.")
else:
    print("No clear winner. That was unexpected.")
