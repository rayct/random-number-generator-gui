#  Version 1.0.3a CMD Line Version with Prompt
# * Run the program using the following command:
# `python random_number_generator_cmd_prompt.py`


# import argparse
# import random

# def generate_numbers(numbers, weights, num_samples):
#     try:
#         numbers = [int(num) for num in numbers.split(",")]
#         weights = [int(weight) for weight in weights.split(",")]

#         random_numbers = random.choices(numbers, weights=weights, k=num_samples)
#         return random_numbers
#     except ValueError:
#         print("Invalid input format. Please enter valid numbers and weights.")
#         return []

# def main():
#     numbers = input("Enter comma-separated list of numbers: ")
#     weights = input("Enter comma-separated list of weights: ")
#     num_samples = int(input("Enter the number of samples to generate: "))

#     random_numbers = generate_numbers(numbers, weights, num_samples)

#     if random_numbers:
#         print("Generated Random Numbers:", ", ".join(map(str, random_numbers)))

# if __name__ == "__main__":
#     main()