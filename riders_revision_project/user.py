import hashlib

class User:
    def __init__(self,name,email,password) -> None:
        self.name=name
        self.email=email
        pwd_encode=password.encode()
        hashed_pwd=hashlib.md5(pwd_encode).hexdigest()
        print(hashed_pwd)

user1=User('alaim','alaim@gmail.com','shuvo')

