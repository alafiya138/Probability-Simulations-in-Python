Probability Simulations in PythonThis repository contains Python scripts that use Monte Carlo simulation techniques to calculate experimental probabilities for common statistical scenarios, such as coin tosses and dice rolls.🚀 OverviewThe primary goal of this project is to demonstrate how large numbers of random trials (simulations) can be used to approximate theoretical probabilities. The script provides functions to simulate:Coin Tosses: Calculating the experimental probability of landing on 'Heads' or 'Tails'.Dice Rolls: Calculating the experimental probability of getting a specific sum (e.g., a sum of 7) when rolling two six-sided dice.🛠️ Featurescoin_toss_simulation(num_tosses): Simulates a coin toss for a specified number of iterations using random.choice.dice_roll_simulation(num_rolls): Simulates rolling two dice and tracks how often the sum equals 7 using random.randint.Comparative Analysis: The script prints both the experimental results and the theoretical expectations for easy comparison.📋 PrerequisitesTo run this project, you simply need Python 3.x installed on your machine. No external libraries are required as it uses the built-in random module.💻 UsageClone the repository:Bashgit clone https://github.com/alafiya138/Probability-Simulations-in-Python.git
cd Probability-Simulations-in-Python
Run the simulation script:Bashpython "import random.py"
📊 Example OutputWhen you run the script, you will see output similar to this:Plaintext--- Coin Toss Simulation ---
Number of coin tosses: 10000
Experimental probability of Heads: 0.5012
Experimental probability of Tails: 0.4988
------------------------------

--- Dice Roll Simulation ---
Number of dice rolls (two dice): 100000
Experimental probability of getting a sum of 7: 0.1664
------------------------------

--- Theoretical Probabilities (for comparison) ---
Theoretical probability of Heads: 0.5
Theoretical probability of Tails: 0.5
Theoretical probability of getting a sum of 7 (two dice): 0.1667 (approx 1/6)
🧠 Theoretical BackgroundLaw of Large Numbers: As the number of trials increases, the experimental probability tends to get closer to the theoretical probability.Sum of 7 logic: There are 36 possible outcomes when rolling two dice. A sum of 7 can be achieved in 6 ways: (1,6), (2,5), (3,4), (4,3), (5,2), and (6,1). Thus, the theoretical probability is $6/36 = 1/6 \approx 0.1667$.
