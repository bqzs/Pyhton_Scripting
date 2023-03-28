import secrets
import string
alphabet = string.ascii_letters + string.digits
pwd_len = int(input("enter th epassword llength : "))
password = ''.join(secrets.choice(alphabet) for i in range(pwd_len))



print(password)