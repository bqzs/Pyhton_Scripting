import secrets
import string

alphabet = string.ascii_letters + string.digits
pwd_len = int(input("Enter the password length: "))
password = ''.join(secrets.choice(alphabet) for i in range(pwd_len))

print("Your randomly generated password is:", password)
