import random


def roll_dice():
    """Simulate rolling a six-sided dice."""
    return random.randint(1, 6)


def get_number_of_players():
    """Prompt the user to enter the number of players (2-4)."""
    while True:
        players = input("How many players? [2-4]: ")
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print("Number of players must be between 2 and 4.")
        else:
            print("Invalid input! Please enter a number between 2 and 4.")


def main():
    """Main function to execute the PIG game."""
    players = get_number_of_players()
    max_score = 50
    player_scores = [0] * players

    while max(player_scores) < max_score:
        for player_idx in range(players):
            print(f"\nPlayer {player_idx + 1}'s turn has started.")
            print(f"Your total score is: {player_scores[player_idx]}\n")
            current_score = 0

            while True:
                should_roll = input("Do you want to roll [y/n] or Q to quit: ").lower()
                if should_roll == "q":
                    print("Quitting the game.")
                    return
                if should_roll != "y":
                    break

                roll_value = roll_dice()
                if roll_value == 1:
                    print("You rolled a 1! Turn over.")
                    current_score = 0
                    break
                else:
                    current_score += roll_value
                    print(f"You rolled a {roll_value}.")
                    print(f"Your current score for this turn is {current_score}.")

            player_scores[player_idx] += current_score
            print(f"Your total score is now {player_scores[player_idx]}.")

    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)
    print(f"\nPlayer {winning_idx + 1} wins with a final score of {max_score}!")


if __name__ == "__main__":
    main()