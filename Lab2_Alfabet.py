x = 0

for i in range(65, 91):

    litera = chr(i)

    x += 1

    tmp = litera + litera.lower()

    print(tmp, end="")



t = 0

for i in range(65, 91):

    litera = chr(i)

    t += 1

    tmp = litera.lower() + litera

    print(tmp, end="")