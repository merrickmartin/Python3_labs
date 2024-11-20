#!/usr/bin/env python3
# author: Merrick Martin
#version: 1.0
#Description: This script is lotto generater will generate six random number
""""""
""""""
import random
white_num = [] 
powerball = []
while len(powerball) < 1:
    red_num = random.randint(1,26)
    if red_num not in powerball:
        powerball.append(red_num)
while len(white_num) < 5:
    white_ball= random.randint(1,69)
    if white_ball not in white_num:
        white_num.append(white_ball)
    else:
        print(f"Duplicate number: {white_ball}")
print(f"Lottery numbers:{white_num} {powerball}")