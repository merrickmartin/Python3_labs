#!/usr/bin/env python3
# author: Merrick Martin
#version: 1.0
#Description: This script is lotto generater will generate six random number
""""""
""""""
import random
lotto = [] 
while len(lotto) < 6:
    num = random.randint(1,50)
    if num not in lotto:
        lotto.append(num)
    else:
        print(f"Duplicate number: {num}")
print(f"Lottery numbers:{lotto}")