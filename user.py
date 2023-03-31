import hashlib,threading
from random import random,randint,choice
from brta import BRTA
license_authority=BRTA()
from vehicles import Car
from vehicles import Bike
from vehicles import Cng
from ride_manager import uber

class UserAlreadyExists(Exception):
    def __init__(self,email, *args: object) -> None:
        print(f'{email} already exist.')
        super().__init__(*args)
class User:
    def __init__(self,name,email,password) -> None:
        self.name=name
        self.email=email
        pwd_encrypted=hashlib.md5(password.encode()).hexdigest()
        alreadyExist=False
        with open('users.txt','r') as file:
            if email in file.read():
                # raise UserAlreadyExists(email)
                alreadyExist=True
        file.close()
        if alreadyExist==False:
            with open('users.txt','a') as file:
                file.write(f'{email} {pwd_encrypted}\n')
                file.close()
        # print(self.name,"Created successfully")
    @staticmethod
    def log_in(email,password):
        stored_password=''
        with open('users.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                if email in line:
                    stored_password=line.split(" ")[1]
                    hashed_password=hashlib.md5(password.encode()).hexdigest()
                    if hashed_password==stored_password:
                        print("Valid User")
                        return True
                    else:
                        print("Invalid User")
                        return False
        file.close()

class Rider(User):
    def __init__(self, name, email, password,location,balance) -> None:
        super().__init__(name, email, password)
        self.location=location
        self.balance=balance
        self.__trip_history=[]
    def set_location(self,location):
        self.location=location
    def get_location(self):
        return self.location
        super().__init__(name, email, password)
    def request_trip(self,destination):
        pass
    def get_trip_history(self):
        return self.__trip_history
    
    def start_a_trip(self,fare,trip_info):
        print(f'A trip started for {self.name}')
        self.balance-=fare
        # self.location=destination
        self.__trip_history.append(trip_info)

class Driver(User):
    def __init__(self, name, email, password,location,license) -> None:
        super().__init__(name, email, password)
        self.location=location
        self.__trip_history=[]
        self.license=license
        self.valid_driver=license_authority.validate_license(email,license)
        self.earning=0
        self.vehicle=None

    def take_driving_test(self):
        result=license_authority.take_driving_test(self.email)
        if result ==False:
            self.license=None
        else:
            self.license=result
            self.valid_driver=True

    def register_a_vehicle(self,vehicle_type,license_plate,rate):
        if self.valid_driver is True:
            if vehicle_type=='car':
                self.vehicle=Car(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            elif vehicle_type=='bike':
                self.vehicle=Bike(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
            else:
                self.vehicle=Cng(vehicle_type,license_plate,rate,self)
                uber.add_a_vehicle(vehicle_type,self.vehicle)
        else:
            # print('You are not a valid driver')
            pass

    def start_a_trip(self,start,destination,fare,trip_info):
        self.earning+=fare
        self.location=destination
        # start thread
        trip_thread=threading.Thread(target=self.vehicle.start_driving,args=(start,destination,))
        trip_thread.start()
        self.vehicle.start_driving(start,destination)
        self.__trip_history.append(trip_info)
        
        
vehicles_type=['car','bike','cng']
rider1=Rider('rider1','rider1@gmail.com','rider1',randint(0,30),1000)
rider2=Rider('rider2','rider2@gmail.com','rider2',randint(0,30),1000)
rider3=Rider('rider3','rider3@gmail.com','rider3',randint(0,30),1000)

for i in range(1,100):
    driver1=Driver(f'driver{i}',f'driver{i}@gmail.com',f'driver{i}',randint(0,100),randint(1000,9999))
    driver1.take_driving_test()
    driver1.register_a_vehicle(choice(vehicles_type),randint(10000,99999),10)
print(uber.get_available_cars())
uber.find_a_vehicle(rider1,choice(vehicles_type),randint(1,100))
uber.find_a_vehicle(rider2,choice(vehicles_type),randint(1,100))
uber.find_a_vehicle(rider3,choice(vehicles_type),randint(1,100))
uber.find_a_vehicle(rider1,choice(vehicles_type),randint(1,100))
uber.find_a_vehicle(rider1,choice(vehicles_type),randint(1,100))

print(rider1.get_trip_history())
print(uber.total_income())