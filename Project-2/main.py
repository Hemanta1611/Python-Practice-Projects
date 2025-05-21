# Random Password Generator

import random
import string

def generate_password():
    length = int(input("Enter the length of the password: ").strip())
    if length < 8:
        print("Password length must be at least 8 characters long.")
        generate_password()
    else:
        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower()
        include_special = input("Include special characters? (yes/no): ").strip().lower()
        include_numbers = input("Include numbers? (yes/no): ").strip().lower()

        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        special = string.punctuation
        numbers = string.digits

        all = lower + upper + special + numbers

        # there can be 8 cases:
        # case 1: no uppercase, no special, no numbers
        if include_uppercase == "no" and include_special == "no" and include_numbers == "no":
            s = random.choices(lower, k=length)
            random.shuffle(s)
            return s

        # case 2: no uppercase, no special, yes numbers
        if include_uppercase == "no" and include_special == "no" and include_numbers == "yes":
            s = random.choices(numbers)
            s = s + random.choices(lower, k=length-1)
            random.shuffle(s)
            return s

        # case 3: no uppercase, yes special, no numbers
        if include_uppercase == "no" and include_special == "yes" and include_numbers == "no":
            s = random.choices(special)
            s = s + random.choices(lower, k=length-1)
            random.shuffle(s)
            return s

        # case 4: no uppercase, yes special, yes numbers
        if include_uppercase == "no" and include_special == "yes" and include_numbers == "yes":
            s = random.choices(special)
            s = s + random.choices(numbers)
            s = s + random.choices(lower, k=length-2)
            random.shuffle(s)
            return s

        # case 5: yes uppercase, no special, no numbers
        if include_uppercase == "yes" and include_special == "no" and include_numbers == "no":
            s = random.choices(upper)
            s = s + random.choices(lower, k=length-1)
            random.shuffle(s)
            return s

        # case 6: yes uppercase, no special, yes numbers
        if include_uppercase == "yes" and include_special == "no" and include_numbers == "yes":
            s = random.choices(upper)
            s = s + random.choices(numbers)
            s = s + random.choices(lower, k=length-2)
            random.shuffle(s)
            return s

        # case 7: yes uppercase, yes special, no numbers
        if include_uppercase == "yes" and include_special == "yes" and include_numbers == "no":
            s = random.choices(upper)
            s = s + random.choices(special)
            s = s + random.choices(lower, k=length-2)
            random.shuffle(s)
            return s

        # case 8: yes uppercase, yes special, yes numbers
        if include_uppercase == "yes" and include_special == "yes" and include_numbers == "yes":
            s = random.choices(upper)
            s = s + random.choices(special)
            s = s + random.choices(numbers)
            s = s + random.choices(lower, k=length-3)
            random.shuffle(s)
            return s

password = generate_password()
print("Your password is: ", "".join(password))

