class Computer:
    
    # What attributes will it need?
    price: float
    os: str
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, os:str, amt:float):
        self.os = os
        self.price = amt

    def priceUpdate(self, new_price.float):
        self.price = new_price

    def osUpdate(self, new_os.str):
        self.os = new_os

    def retrieveComputerInformation(self, price:float, os:str):
        print("This computer has an operating system of", os, ".\nIts current retail price is", price)
    # What methods will you need?
