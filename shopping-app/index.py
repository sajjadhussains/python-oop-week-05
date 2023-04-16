# Shopping cart design

class User:
    user_lst=[]#class variable
    def __init__(self,username,password) -> None:
        self.username=username
        self.password=password

class Item:
    def __init__(self,itemId,price,description,quantity) -> None:
        self.itemId=itemId
        self.price=price
        self.description=description
        self.quantity=quantity

class ShoppingBasket:
    user_lst=[]
    user_ordered_data={}
    items_db={}
    def get_userlst(self):
        return self.user_lst
    
    def create_account(self):
        name=input("Enter your name: ")
        isNameExist=False
        for user in self.get_userlst(): #user already ache ki na
            if user.username==name:
                print('Vai tomar to account kholai ache!!')
                isNameExist=True
                break
        if isNameExist==False:
            password=input("Enter your password: ")
            self.new_user=User(name,password)
            self.user_lst.append(vars(self.new_user))
            print("Account created successfully")

a1=ShoppingBasket()
a1.create_account()
print(a1.get_userlst())

# items={'rahat':[{'itemId':1,'price':250,'description':'sustainable product','quantity':2}]}
# items['rahat'].append({'itemId':2,'price':350,'description':'heavy product','quantity':10})
# print(len(items['rahat']))