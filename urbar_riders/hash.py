import hashlib

email="sajjad@gmail.com"
passwrod="distanceFromToxicPeople"

pwd=passwrod.encode()

hashed_password=hashlib.md5(pwd).hexdigest()
your_password=hashlib.md5("distanceFromToxicPeople".encode()).hexdigest()
if hashed_password==your_password:
    print("password matched")
else:
    print("Password didn't matched")