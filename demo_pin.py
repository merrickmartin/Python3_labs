#!/usr/bin/env python3
# author: Merrick Martin
#version: 1.0
#Description: This script will simulate a high street bank PIN machine.

import getpass

master_pin = "0123"
pin = None
attempt = 0

while pin != master_pin and attempt < 3:
    pin = getpass.getpass("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
    else:
        print("Invalid PIN")
        attempt += 1
print("Done")