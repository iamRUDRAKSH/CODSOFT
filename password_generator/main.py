import random
import string

def generate_pass():
    try:
        length = int(input("No. of characters in the password(4-16): "))
        if length < 4 or length > 16:
                print("Length must be between 4 and 16.")
                return
        
        alphabets = input("Should password contain alphabets?(y/n): ")
        numbers = input("Should password contain numbers?(y/n): ")
        symbols = input("Should password contain special characters[@,_,!]?(y/n): ")
        characters = ""

        if alphabets == 'y':
            characters += string.ascii_letters
        if numbers == 'y':
            characters += string.digits
        if symbols == 'y':
            characters += '@_!'
        
        if not characters:
                print("You must select at least one character type.")
                return

        return ''.join(random.choice(characters) for _ in range(length))
    except ValueError:
         print("Please enter a valid number.")

password = generate_pass()
print(f"Generated password: {password}")
