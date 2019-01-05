import csv
import random
import numpy

def player(height_min, height_max, position):
    s=[]
    for i in range(0, 500):
        s.append([random.randrange(height_min, height_max), position])
    return s

setter=player(165, 190, 1)
opposite=player(185, 205, 4)
center=player(185, 205, 3)
libero=player(165, 180, 6)
spiker=player(177, 205, 2)

x=[setter,opposite,center,libero,spiker]


with open('D:\\Programs\Python\\repositories\\python_codes\\algorithms\\test.csv', 'w', newline='') as f:
    writer = csv.writer(f, quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['height', 'position'])
    for i in x:
        for v in i:
            setter=player(165, 190, 1)
            opposite=player(185, 205, 4)
            center=player(185, 205, 3)
            libero=player(165, 180, 6)
            spiker=player(177, 205, 2)

            x=[setter,opposite,center,libero,spiker]

            writer.writerow(v)
