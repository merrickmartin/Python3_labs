#!/usr/bin/env python3
# author: Merrick Martin
#version: 1.0
#Description: This script is Exercise#2

#Prompt the user for input of lap and fuel use during the qualifying round.
#calcualate user input and print required f

def formula1():
    laps = int(input("Total number of laps: "))
    fuel = float(input("What is the average amount of fuel that was consumed per lap: "))
    required_fuel = laps * fuel
    contingency = required_fuel * 1.5
    print(f"{contingency} kg")

formula1()