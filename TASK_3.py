# FIRST WE IMPORT 2 MODULES

import random
import string

# THEN WE ARE DEFINE THE FUNCTION BY USING def KEYWORD

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# THEN WE ARE DEFINING THE main CLASS 

def main():
    length = int(input("Enter password length (min 4): "))
    if length < 4:
        print("Length must be at least 4.")
        return
    print("Generated Password:", generate_password(length))


# THEN WE ARE CALLING THE main CLASS

if __name__ == "__main__":
    main()

