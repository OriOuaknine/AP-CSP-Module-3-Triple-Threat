"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Ori Ouaknine - Nov 2024
"""

import random

def play_game():
    amount_to_play = 1 
    base_prize = 10 
    payout = 0 

    dice = [random.randint(1, 6) for _ in range(3)]
    
    if dice[0] == dice[1] and dice[2]:
        payout = dice[0] * base_prize
    else:
        payout = 0
    
    return amount_to_play, payout, dice

def simulate_day():
    games_played = random.randint(1000, 5000)
    
    total_collected = 0
    total_paid_out = 0

    for _ in range(games_played):
        amount_to_play, payout, dice = play_game()
        total_collected += amount_to_play
        total_paid_out += payout
    
    profit = total_collected - total_paid_out
    
    print(f"{games_played},{total_collected},{total_paid_out},{profit}")

def main():
    days = int(input("Enter the number of days to simulate: "))
    
    print("Games Played,Total Collected,Total Paid Out,Profit")
    
    for _ in range(days):
        simulate_day()

if __name__ == "__main__":
    main()

