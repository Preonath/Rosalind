with open("R12.txt", "r") as fi:
    l = fi.readline().split(" ")
    a = float(l[0])
    b = float(l[1])
    c = float(l[2])
    d = float(l[3])
    e = float(l[4])
    f = float(l[5])
    fi.close()

total_offspring = (a * 2.0) + (b * 2.0) + (c * 2.0) + (d * 2.0*.75) + (e*2.0*.5) + (f*0.0)

print(total_offspring)