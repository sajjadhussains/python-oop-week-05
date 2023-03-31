from abc import ABC,abstractmethod
import time
class Vehicle(ABC):
    speed={
        'car':30,
        'bike':50,
        'cng':15
    }
    def __init__(self,vehicle_type,license_plate,rate,driver) -> None:
        self.vehicle_type=vehicle_type
        self.rate=rate
        self.license_plate=license_plate
        self.driver=driver
        self.status='available'
        self.speed=self.speed[vehicle_type]

    @abstractmethod
    def start_driving(self):
        pass
    @abstractmethod
    def trip_finished(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type,license_plate,rate, driver) -> None:
        super().__init__(vehicle_type,license_plate, rate, driver)

    def start_driving(self,start,destination):
        print(self.vehicle_type,self.license_plate,'started')
        self.status='unavailable'
        distance=abs(start-destination)
        for i in range(0,distance):
            time.sleep(0.5)
            print(f'Driving: {self.license_plate} current position:{i} of {distance}\n')
        # return super().start_driving()
        self.trip_finished()

    def trip_finished(self):
        self.status='availabale'
        print(self.vehicle_type,self.license_plate,'trip completed')

class Bike(Vehicle):
    def __init__(self, vehicle_type,license_plate,rate, driver) -> None:
        super().__init__(vehicle_type, license_plate,rate, driver)

    def start_driving(self,start,destination):
        print(self.vehicle_type,self.license_plate,'started')
        self.status='unavailable'
        distance=abs(start-destination)
        for i in range(0,distance):
            time.sleep(0.5)
            print(f'Driving: {self.license_plate} current position:{i} of {distance}\n')
        # return super().start_driving()
        self.trip_finished()

    def trip_finished(self):
        self.status='availabale'
        print(self.vehicle_type,self.license_plate,'trip completed')

class Cng(Vehicle):
    def __init__(self, vehicle_type,license_plate,rate, driver) -> None:
        super().__init__(vehicle_type,license_plate, rate, driver)

    def start_driving(self,start,destination):
        print(self.vehicle_type,self.license_plate,'started')
        self.status='unavailable'
        distance=abs(start-destination)
        for i in range(0,distance):
            time.sleep(0.5)
            print(f'Driving: {self.license_plate} current position:{i} of {distance}\n')
        # return super().start_driving()
        self.trip_finished()

    def trip_finished(self):
        self.status='availabale'
        print(self.vehicle_type,self.license_plate,'trip completed')
    
