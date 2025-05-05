class Computer:
    
    # What attributes will it need?
    price: float
    os: int
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, os:int, amt:float):
        self.os = os
        self.price = amt

    def priceUpdate(self, new_price.float):
        self.price = new_price

    def osUpdate(self, new_os.int):
        self.os = new_os
    # What methods will you need?
