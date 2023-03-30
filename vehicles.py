from abc import ABC,abstractmethod

class Vehicle:
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

    def start_driving(self):
        print(self.vehicle_type,'started')
        self.status='unavailable'
        return super().start_driving()

    def trip_finished(self):
        print(self.vehicle_type,self.license_plate,'trip completed')
        self.status='availabale'
        return super().trip_finished()
class Bike(Vehicle):
    def __init__(self, vehicle_type,license_plate,rate, driver) -> None:
        super().__init__(vehicle_type, rate, driver)

    def start_driving(self):
        print(self.vehicle_type,'started')
        self.status='unavailabale'
        return super().start_driving()

    def trip_finished(self):
        print(self.vehicle_type,self.license_plate,'trip completed')
        self.status='availabale'
        return super().trip_finished()
class Cng(Vehicle):
    def __init__(self, vehicle_type,license_plate,rate, driver) -> None:
        super().__init__(vehicle_type, rate, driver)

    def start_driving(self):
        print(self.vehicle_type,'started')
        self.status='unavailabale'
        return super().start_driving()

    def trip_finished(self):
        print(self.vehicle_type,self.license_plate,'trip completed')
        self.status='availabale'
        return super().trip_finished()
    
