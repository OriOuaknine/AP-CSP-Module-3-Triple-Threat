"""
Triple threat simulation game for AP Computer Science Principles.
Monarch High School - Boulder Valley School District
Ori Ouaknine - November 2024
"""

import random

def main() -> None:
    cost_to_play: int = 3
    base_prize: int = 17
    mega_number: int = 10
    mega_multiplier: int = 10

    min_plays: int = 1000
    max_plays: int = 5000
    
    print("Games Played,Total Collected,Total Paid Out,Total Profit")

    num_days: int = 10
    
    for _ in range(num_days):
        num_plays: int = random.randint(min_plays, max_plays)
        
        total_collected: int = 0;
        total_payout: int = 0
        total_profit: int = 0
        for _ in range(num_plays):
            roll_1: int = random.randint(1, 6)
            roll_2: int = random.randint(1, 6)
            roll_3: int = random.randint(1, 6)
            
            payout: int = 0
            if roll_1 == roll_2 and roll_2 == roll_3:
                if roll_1 == mega_number:
                    payout = base_prize * mega_multiplier
                else:
                    payout = base_prize * roll_1
        
            profit: int = cost_to_play - payout
            
            total_collected += cost_to_play
            total_payout += payout
            total_profit += profit
            
        print(f"{num_plays},{total_collected},{total_payout},{total_profit}")    
        

if __name__ == "__main__":
    main()
