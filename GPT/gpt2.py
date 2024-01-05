import random

def generate_useless_numbers():
    return [random.randint(1, 100) for _ in range(5)]

def print_useless_information(numbers):
    total_sum = sum(numbers)
    print(f"Processing data: The sum of the random numbers is {total_sum}.")

if __name__ == "__main__":
    random_numbers = generate_useless_numbers()
    print_useless_information(random_numbers)
