#  Version 1.0.3 CMD Line Version with Prompt

# Run the program using the following command at the prompt:
# `python rand_cmd.py`


# import argparse
# import random

# def generate_numbers(numbers, weights, num_samples):
#     """
#     Generate random numbers based on provided weights.

#     Args:
#         numbers (str): Comma-separated list of numbers.
#         weights (str): Comma-separated list of corresponding weights.
#         num_samples (int): Number of random samples to generate.

#     Returns:
#         list: List of randomly generated numbers.
#     """
#     try:
#         numbers = [int(num) for num in numbers.split(",")]
#         weights = [int(weight) for weight in weights.split(",")]

#         random_numbers = random.choices(numbers, weights=weights, k=num_samples)
#         return random_numbers
#     except ValueError:
#         print("Invalid input format. Please enter valid numbers and weights.")
#         return []

# def main():
#     """
#     Main function to generate and display random numbers based on user input.
#     """
#     numbers = input("Enter comma-separated list of numbers: ")
#     weights = input("Enter comma-separated list of weights: ")
#     num_samples = int(input("Enter the number of samples to generate: "))

#     random_numbers = generate_numbers(numbers, weights, num_samples)

#     if random_numbers:
#         print("Generated Random Numbers:", ", ".join(map(str, random_numbers)))

# if __name__ == "__main__":
#     main()

