#DiceRoll.py
#Name: Bennett McDonald 
#Date: 3/2/25
#Assignment: dice roll
import random

def main():
    # Create an empty list to count occurrences of each sum (from 2 to 12)
    rolls = [0] * 11  # Index 0 will represent sum 2, index 11 will represent sum 12

    # Set the number of rolls (at least 10,000)
    num_rolls = 10000

    # Simulate the dice rolls
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)  # Roll the first die
        die2 = random.randint(1, 6)  # Roll the second die
        roll_sum = die1 + die2      # Find the sum of the two dice

        # Increment the count for the corresponding sum
        rolls[roll_sum - 2] += 1

    # Display statistics for the dice rolls
    print(f"After {num_rolls} rolls:")
    for sum_value in range(2, 13):
        count = rolls[sum_value - 2]
        percentage = (count / num_rolls) * 100
        print(f"Sum {sum_value}: {count} times ({percentage:.2f}%)")

if __name__ == '__main__':
    main()