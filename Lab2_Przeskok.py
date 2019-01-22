start = int(input('Podaj początek zakresu: '))

stop = int(input('Podaj koniec zakresu: '))

jump = int(input('Podaj przeskok: '))





for i in range(start, stop):

    print(start)

    start += jump

    if start >= stop:

        break



