#! /usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
print(Belgium)
hypens = "-"
print(f"{hypens * 81} .....")
print(Belgium.replace(",",":"))
new_Belgium = Belgium.split(",")
belgium_pop = new_Belgium[1]
brussel_pop = new_Belgium[3]
pop = int(belgium_pop) + int(brussel_pop)
print(pop)
print(hypens * 81)
