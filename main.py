"""
This project is a solution to the following problem:
"""
import os
from sys import platform

class Main:
    def __init__(self, trip_distance, mpg, gas_cost, e_mpg, e_cost):
        self.trip_distance = trip_distance
        self.mpg = mpg
        self.gas_cost = gas_cost
        self.e_mpg = e_mpg
        self.e_cost = e_cost
        
    def gas_needed(self):
        return (self.trip_distance / self.mpg)
    def gas_cost_infl(self):
        return ((self.trip_distance / self.mpg) * (self.gas_cost + .5))
    def e_charges(self):
        return (self.trip_distance / self.e_mpg)
    def e_cost_total(self):
        return ((self.trip_distance / self.e_mpg) * (self.e_cost))

def title():
    print('\n')
    print(r' _|      _|                                              _|      _|            _|                          ')
    print(r' _|_|  _|_|    _|_|_|    _|_|_|    _|_|    _|_|_|          _|  _|    _|_|_|  _|_|_|_|    _|_|      _|_|_|  ')
    print(r' _|  _|  _|  _|    _|  _|_|      _|    _|  _|    _|          _|    _|    _|    _|      _|_|_|_|  _|_|      ')
    print(r' _|      _|  _|    _|      _|_|  _|    _|  _|    _|          _|    _|    _|    _|      _|            _|_|  ')
    print(r' _|      _|    _|_|_|  _|_|_|      _|_|    _|    _|          _|      _|_|_|      _|_|    _|_|_|  _|_|_|    ')
    print(r'___________________________________________________________________________________________________________')
    print('\n')

def clear_console():
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        return os.system('clear')
    elif platform == "win32":
        return os.system('cls')

#This function is to check the conversion of input values to int or float so we can operate on them. Not included in Main class because it is outside class scope.   
def check_num(str): 
    while True:
        num = input(str)
        try:
            val = int(num)
            print("✅", val)
            return val
        except ValueError:
            try:
                val = float(num)
                print("✅", val)
                return val
            except ValueError:
                print("❌Invlaid entry. Please enter a number")

#This function is to check the result of input values to char so we can operate on them. Not included in Main class because it is outside class scope.
def check_char(str):
    while True:
        char = input(str)[0] #Only allows for one character response.
        try:
            if(char.lower() == 'y'):
                clear_console()
                return start()
            elif(char.lower() == 'n'):
                print('Goodbye 😁')
                break;
            else:
                print('Invalid entry. Please enter either y or n')
        except ValueError:
            print("An exception occured" + ValueError)

#The start function will initialize the program and hold our inputs/class instances to return our result
def start():
    break_point = '==============================================='
    #Put your prompt in the argument
    trip_distance = check_num('Please enter the distance of the trip in miles without commas:')
    print(break_point)
    mpg = check_num('Please enter the average highway MPG of the vehicle:')
    print(break_point)
    gas_cost = check_num('Please enter the current price per gallon of gasoline without a dollar sign:')
    print(break_point)
    e_mpg = check_num('Please enter the distance in miles a certain electric vehicle gets per full charge:')
    print(break_point)
    e_cost = check_num('Please enter the cost of electricity for a full charge wihtout a dollar sign:')

    instance = Main(trip_distance, mpg, gas_cost, e_mpg, e_cost)
    print(break_point)
    print('The gasoline vehicle needs '+ str(round(instance.gas_needed(), 2)) + ' gallons of gas to complete the trip.')
    print('The cost of gas will be $' + str(round(instance.gas_cost_infl(), 2)))
    print('The number of charges the E-Vehicle will need is ' + str(round(instance.e_charges(), 2)) + ' charges.')
    print('The cost of the E-vehicle will be $' + str(round(instance.e_cost_total(), 2)))
    if(instance.gas_cost_infl() > instance.e_cost_total()):
        print('The E-vehicle is cheaper to take. The gas vehicle will cost $' + str(instance.gas_cost_infl() - instance.e_cost_total()) + ' more.')
    else:
        print("The gas vehicle is cheaper to take. The E-vehicle will cost $" + str(instance.e_cost_total() - instance.gas_cost_infl()) + ' more.')
    print(break_point)
    
    check_char("Would you like to start again? (y/n)")

#Initialize program
title()
start()
