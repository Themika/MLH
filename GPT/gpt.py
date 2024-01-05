import random

def generate_useless_string(length):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))

def print_useless_message():
    useless_string = generate_useless_string(10)
    print(f"Processing data: {useless_string[::-1]} - {len(useless_string)}")

if __name__ == "__main__":
    print_useless_message()
