#!/usr/bin/env python3
# author: Merrick Martin
#version: 1.0#Description: This script is use to check if the user input year is a leap year

year = int(input("Enter the year you want to check if it's Leap Year: "))
if year % 400 == 0:
    print(f"{year} is a leap year.")
elif year % 4 == 0 and year % 100 >= 1:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap yea.")