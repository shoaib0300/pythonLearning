import  random
import string

def generate_password(length=18):
    letters = string.ascii_letters
    digits = string.digits
    special_character = "@!#%$*%(ˆ)*_<>?|{}"

    characters = letters + digits + special_character
    password = ''

    # Generate the password by randomly selecting characters
    for _ in range(length):
        password += random.choice(characters)

    return password

passwords = generate_password()

print("Generated_password: ", passwords)