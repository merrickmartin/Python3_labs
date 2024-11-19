#!/usr/bin/env python3
# author: Merrick Martin
#version: 1.0#Description: This script is use to range of numbers by steps of -2


raw_input = int (input("Please enter an integer: "))
if raw_input.is_integer():
    for i in range(raw_input, -1, -2):
        print(i)
else:
    print("Please enter an integer: ")
