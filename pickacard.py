#!/usr/bin/env python3
# author: Merrick Martin
#version: 1.0
#Description: This script is Exercise#1
import showcard

number = input("Pick a card (1-52): ")

filename = "BMP" +number + ".GIF"
showcard.display_file(filename)