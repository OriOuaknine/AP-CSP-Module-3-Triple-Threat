# AP Computer Science Principles 
## Module 3 - Triple-Threat Lab
We will use this lab throughout module 3 to introduce a few concepts with pseudrandomization and simulations.
At each step of the way, you will refactor your code to introduce new concepts. Refactoring means that you are re-organizing it without changing the external functionality.

## Step 1: Write the base progam
You are designing a new, simple casino game. The idea is to earn money for the casino **in the long run** while also giving the player the impression that they can easily win.

### Rules
1. To play, pays an amount up front. Start this off at $1.
2. During a play, the player rolls three dice. If all three dice are equal, the player wins!
3. A base prize is set. Start with $10. That base prize is multiplied by the value of the dice:

```
    1-1-1 = 1 * $10 = $10
    2-2-2 = 2 * $10 = $20
    3-3-3 = 3 * $10 = $30
    4-4-4 = 4 * $10 = $40
    5-5-5 = 5 * $10 = $50

    However, rolling all 6s, yields in a mega-multiplier of 10
    6-6-6 = 10 * $10 = $100
```

Write the program so that the amount to play and base prize are variables. When you run the program, it should play the game once.

The output should look like this. **Note:** This output will change over time.

```
Casino collects: $1
Player rolls: 1-2-4
Casino pays out: $0
Profit: $1
```

## Step 2: Run the game multiple times - model one day
Playing the game once isn't super useful because as a casino, we'd like to make money over time, even if we lose a few hundred games.

Put the game code in a loop that will model a certain number of plays in a day. You can set that value at a random number between 1,000 and 5,000.

Instead of outputting 1,000-5,000 results, add some more variables. You will need to keep track of how much money you take in during the day and how much you pay out. You can also keep a variable for profit.

Your output should look like this
```
Games Played,Total Collected,Total Paid Out,Profit
2483,2483,1330,1553
```

This format is called a **comma-separated values** (CSV) format where the data is separated out by commas.

## Step 3: Run the game for multiple days
Set the number of days you want to run the simulation. Make this a variable, but set the value, or better yet, prompt the user for a value.

You'll need to put your game runnning loop inside of another loop for the days - so a loop inside of a loop.

Why don't we just run it days * games per day? The reason is we've made the number of games played per day a variable to see if that might have influence.

You should output the result of each day in the CSV format above, like this:
```
Games Played,Total Collected,Total Paid Out,Profit
2483,2483,1330,1553
1320,1320,5203,-3883
3423,3423,3402,21
```
