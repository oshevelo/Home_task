class Car:
    distance = int(input())
    if distance > 99999:
        print("Error!")
    open_doors = int(input())
    if open_doors > 4:
        open_doors = 4
    close_dore = int(input())
    if close_dore > open_doors:
        close_dore = open_doors
#konstruction
    def __init__(self, height, wigth, price, manufactured, speed, doors, color, plaсe, car_mileage):
        self.height = height
        self.wigth = wigth
        self.price = price
        self.manufactured = manufactured
        self.speed = speed
        self.doors = doors
        self.color = color
        self.plaсe = plaсe
        self.car_mileage = car_mileage
    def move(self, distance):
        distance = distance or self.distance
        car_mileage =+ distance
        print('sold for {}'.format(self.car_mileage))
        print(car_mileage)
    def open(self, open_doors =+1):
        open_doors = open_doors or self.open_doors
        print('sold for {}'.format(self.open_doors))
        print(open_doors)
    def close(self, close_doors =+1):
        close_doors = close_doors or self.close_doors
        print('sold for {}'.format(self.open_doors))
        print(close_doors)


class Track(Car):
    def __init__(self, trailer=int(input()), capacity=int(input())):
        if trailer > 2:
            self.trailer = 2
        self.capacity = capacity
    def add_trailer (self, trailer =+ 1):
        trailer = trailer or self.trailer





class Passenger_car(Car):
    def __init__(self, comfortable, car_mileage):
        self.comfortable = comfortable

class Man (Track):
    height = 280
    wight = 270
    car_mileage = 20000
    speed = 60
    place = 2
    manufactured = "Germany"
    price = 300000
    trailer = 2
    capacity = 5000

class Renaut (Passenger_car):
    height = 200
    wight = 230
    car_mileage = 2000
    speed = 60
    place = 2
    manufactured = "France"
    price = 15000
