#!/usr/bin/env python3
# author: Merrick Martin
#version: 1.0
#Description: This script is use to find the hight of a projectile.

# importing math module and pi for calcuation 
import math
from math import pi
from math import tan
from math import cos

def get_height():
    barrel_height = float(input("What is the height of the barrel: "))
    horizontal_distance = float(input("What is the horizontal distance travel: "))
    initial_velocity = float(input("What is the initial velocity: "))        
    elevation = float(input("What is the elevation in degrees: "))
    theta = elevation * (pi/180)
    gravity = 9.81
    height = ((barrel_height + horizontal_distance) * tan(theta) -
             (gravity*(horizontal_distance **2)/2((initial_velocity*cos(theta)))**2))
    return height

