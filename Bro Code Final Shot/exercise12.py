# slot machine exercise
import random


def spin():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    return [random.choice(symbols) for _ in range(3) ]

def print_row(row):
    print(" | ".join(row))

def get_payout(bet, row):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "⭐":
            return bet *4
        elif row[0] == "🔔":
            return bet*8
        elif row[0] == "🍉":
            return bet *9
        elif row[0] == "🍋":
            return bet * 10
    else:
        return 0


def main():
    balance = 100

    print("Welcome to the Slotting game")
    print("Symbols : 🍒 🍉 🍋 🔔 ⭐")

    while balance>0:
        print(f"Current balance : ${balance}.")
        bet = (input("Enter your bet amount : "))
        if not bet.isdigit():
            print("Please enter a valid number!")
            continue
        bet = int(bet)
        if bet > balance:
            print("You don't have enough funds!")
            continue
        if bet <= 0:
            print("Bet must be greater than 0")
            continue
        balance -= bet

        row = spin()
        print_row(row)
        payout = get_payout(bet, row)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost this round!")
        balance += payout

        play_again = input("Do you want to play again? [Y/N] : ")
        if play_again.upper() != "Y":
            print("Thanks for playing! Visit again!")
            break

if __name__ == '__main__':
    main()