from os.path import join
import string
import secrets

letters = string.ascii_letters
digits = string.digits
special_character = string.punctuation

password = letters + digits + special_character
password_length = int(input("Enter the password length: "))

pwd = ''
for i in range(password_length):
    pwd += ''.join(secrets.choice(password))

print(pwd)
