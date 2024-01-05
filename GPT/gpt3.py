import random

def generate_useless_number():
    return random.randint(1, 100)

def check_even_odd(number):
    return "even" if number % 2 == 0 else "odd"

def print_useless_message():
    random_number = generate_useless_number()
    result = check_even_odd(random_number)
    print(f"Processing data: The randomly generated number is {random_number}, and it is {result}.")

if __name__ == "__main__":
    print_useless_message()
