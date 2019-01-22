

print("Wpisz słowo, które ma zostać wyświetlone w odwrotnej kolejności:")

x = input()

l_x = len(x)

for i in range(l_x, 0, -1):

    print(x[::-1])



