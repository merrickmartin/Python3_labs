#!/usr/bin/env python3
# author: Merrick Martin
#version: 1.0
#Description: This script is Exercise#2

#Prompt the user to input there first and and last name
first_name = input("What is your first name: ")
last_name = input("what is your last name: ")
print(f"{first_name} {last_name}")

name = [first_name, last_name]
names = {"first" :first_name, "last":last_name}
print(names)