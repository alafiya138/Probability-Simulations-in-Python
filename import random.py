import random

def coin_toss_simulation(num_tosses):
    """
    Simulates tossing a coin multiple times and calculates experimental probabilities.

    Args:
        num_tosses (int): The number of times to toss the coin.

    Returns:
        tuple: A tuple containing the experimental probability of heads and tails.
    """
    heads_count = 0
    tails_count = 0

    for _ in range(num_tosses):
        outcome = random.choice(['heads', 'tails'])
        if outcome == 'heads':
            heads_count += 1
        else:
            tails_count += 1

    prob_heads = heads_count / num_tosses
    prob_tails = tails_count / num_tosses

    return prob_heads, prob_tails

def dice_roll_simulation(num_rolls):
    """
    Simulates rolling two dice multiple times and calculates the probability of getting a sum of 7.

    Args:
        num_rolls (int): The number of times to roll the two dice.

    Returns:
        float: The experimental probability of getting a sum of 7.
    """
    sum_seven_count = 0

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == 7:
            sum_seven_count += 1

    prob_sum_seven = sum_seven_count / num_rolls
    return prob_sum_seven

if __name__ == "__main__":
    # Scenario a: Tossing a coin 10,000 times
    print("--- Coin Toss Simulation ---")
    num_coin_tosses = 10000
    prob_heads, prob_tails = coin_toss_simulation(num_coin_tosses)
    print(f"Number of coin tosses: {num_coin_tosses}")
    print(f"Experimental probability of Heads: {prob_heads:.4f}")
    print(f"Experimental probability of Tails: {prob_tails:.4f}")
    print("-" * 30)

    # Scenario b: Rolling two dice and computing the probability of getting a sum of 7
    print("\n--- Dice Roll Simulation ---")
    num_dice_rolls = 100000  # A larger number for better approximation
    prob_sum_seven = dice_roll_simulation(num_dice_rolls)
    print(f"Number of dice rolls (two dice): {num_dice_rolls}")
    print(f"Experimental probability of getting a sum of 7: {prob_sum_seven:.4f}")
    print("-" * 30)

    # Theoretical probability for comparison (optional)
    # For a fair coin, theoretical probability of heads/tails is 0.5
    # For two dice, there are 36 possible outcomes. Sum of 7 can be obtained in 6 ways: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1).
    # So, theoretical probability of sum 7 = 6/36 = 1/6 approx 0.1667
    print("\n--- Theoretical Probabilities (for comparison) ---")
    print("Theoretical probability of Heads: 0.5")
    print("Theoretical probability of Tails: 0.5")
    print("Theoretical probability of getting a sum of 7 (two dice): 0.1667 (approx 1/6)")