#Python: String Representations of Objects
#Implement two vehicle classes: 

#Car:
#The constructor for Car must take two arguments. The first of them is its maximum speed, and the second one is a string that denotes the units in which the speed is given: either "km/h" or "mph".
#The class must be implemented to return a string based on the arguments. For example, if car is an object of class Car with a maximum speed of 120, and the unit is "km/h", then printing car prints the following string: "Car with the maximum speed of 120 km/h", without quotes. If the maximum speed is 94 and the unit is "mph", then printing car prints in the following string: "Car with the maximum speed of 94 mph", without quotes.

 

#Boat:

#The constructor for Boat must take a single argument denoting its maximum speed in knots.
#The class must be implemented to return a string based on the argument. For example, if boat is an object of class Boat with a maximum speed of 82, then printing boat prints the following string: "Boat with the maximum speed of 82 knots", without quotes.

 
#The implementations of the classes will be tested by a provided code stub on several input files. Each input file contains several queries, and each query constructs an object of one of the classes.  It then prints the string representation of the object to the standard output.


#Constraints
#1 ≤ the number of queries in one test file ≤ 100
#The lengths of each of the words is at most 10.

#Sample Case 0
#Sample Input

#STDIN           Function
#-----           -------
#2             → number of queries, q = 2
#car 151 km/h  → query parameters = ["car 151 km/h", "boat 77"]
#boat 77
#Sample Output

#Car with the maximum speed of 151 km/h
#Boat with the maximum speed of 77 knots
#Explanation

#There are 2 queries. In the first of them, an object of class Car with the maximum speed of 151 in km/h is constructed, and then its string representation is printed to the output. In the second query, an object of class Boat is constructed with the maximum speed of 77 knots, and then its string representation is printed to the output.


#SOlution:

#!/bin/python3

import math
import os
import random
import re
import sys


class Car:
    def __init__(self, maxspeed, speed_unit):
        self.maxspeed=maxspeed
        self.speed_unit=speed_unit
    def __str__(self):
        sen1="Car with the maximum speed of {} {}".format(self.maxspeed,self.speed_unit)
        return sen1

class Boat:
    def __init__(self,maxspeed):
        self.maxspeed=maxspeed
    def __str__(self):
        sen1="Boat with the maximum speed of {} knots".format(self.maxspeed)
        return sen1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
