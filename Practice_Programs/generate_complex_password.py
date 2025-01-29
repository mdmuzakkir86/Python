# Python 3.11.4
import random
# We can also use inbuilt string also to represent Alphabets, numbers, special charecters

'''
  Have provided min and max as assigned parameters because if we want to change min or max, 
  we can assigne min or max to arg in method while calling,
  So we don't need to change method logic
'''

def produce_complex_password(
        min_length = 10, 
        max_length = 12, 
        min_lower = 2,
        max_lower = 5, 
        min_upper = 2, 
        max_upper = 5, 
        min_numeric = 2, 
        max_numeric = 5, 
        min_special = 2,
        max_special = 5 
    ):
    
    all_chars = (
        "abcdefghijklmnopqrstuvwxyz" +
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
        "0123456789" +
        "!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
    )

    length = random.randint(min_length, max_length)
    lower_count = random.randint(min_lower, max_lower)
    upper_count = random.randint(min_upper, max_upper)
    numeric_count = random.randint(min_numeric, max_numeric)
    special_count = random.randint(min_special, max_special)

    password = []

    for _ in range(lower_count):
        password.append(random.choice("abcdefghijklmnopqrstuvwxyz"))

    for _ in range(upper_count):
        password.append(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    for _ in range(numeric_count):
        password.append(random.choice("0123456789"))

    for _ in range(special_count):
        password.append(random.choice("!@#$%^&*()-_=+[]{}|;:'\",.<>?/"))

    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    password = ''.join(password)

    return password


print("Generated Password:", produce_complex_password())
