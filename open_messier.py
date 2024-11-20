import sys
with open("messier.txt", "r")as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith("M"):
            mes_num = line[:6].rstrip()
            com_name = line[6:40].rstrip()
            object_type = line[40:64].rstrip()
            constellation = line[64:].rstrip()
            if not com_name: com_name ="no name"
            print(f"|{mes_num}|{com_name}|{object_type}|{constellation}|")

  