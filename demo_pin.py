#!/usr/bin/env python3
# author: Merrick Martin
#version: 1.0
#Description: This script will simulate a high street bank PIN machine.

master_pin = "0123"
pin = None

while pin != master_pin:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
    else:
        print("Invalid PIN")
print("Done")