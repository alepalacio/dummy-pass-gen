import random
import string

print("""
=========================================
    Welcome to your Password Generator
=========================================
""")
alpha = string.ascii_letters
numbers = '0123456789'
specials = '!$%&?¡¿+*[]'
chars = f"{alpha}{numbers}{specials}"

num_pass = int(input('How many passwords do you want to generate?: '))
passw_len = int(input('How long do you want your password?: '))

print("""
    Your passwords:
""")

for pwd in range(num_pass):
    passwords = ''
    for char in range(passw_len):
        passwords += random.choice(chars)
    print(passwords)