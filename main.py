import random

print(f"\n{'*' * 10} P I G {'*' * 10}\n")

def roll():
    min_value = 1
    max_value = 6
    result = random.randint(min_value, max_value)
    return result





while True:
    players_numbers = input("Please input numbers of players(2-4): ")
    if players_numbers.isdigit():
        players_numbers = int(players_numbers)
        if 2 <= players_numbers <= 4:
            break
        else: print("Please enter a proper value")
    else:
        print("Please enter a proper value")

players_stats = {f"player_{i}" : 0 for i in range(1, players_numbers + 1)}
max_score = 50


while max_score > max(players_stats.values()):
    for turn in players_stats:
        current_score = 0
        print(f"\nIt's turn of {turn}\n")
        while True :
            answer = input("Do you want to roll? (yes/no): ")
            if answer == "yes" or answer == "y":
                player_roll = roll()
                print(f"You rolled {player_roll}")
                if player_roll == 1:
                    current_score = 0
                    players_stats[turn] += current_score
                    break
                else:
                    current_score += player_roll
                    print(current_score)
            elif answer == "no" or answer == "n":
                break
            else:
                print("Please enter a proper answer.")
        players_stats[turn] += current_score
        print(players_stats)
print(f"The winner is {max(players_stats, key=players_stats.get)}")