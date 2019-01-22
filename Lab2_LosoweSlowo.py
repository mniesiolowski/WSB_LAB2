import random



print("GRA 'Wylosuj slowo'")



SLOWA = ("programowanie", "studia", "student")

slowo = random.choice(SLOWA)



dlugosc_slowa = len(slowo)

print("Dlugosc slowa, to: ", dlugosc_slowa)



print("Masz 5 podpowiedzi do wykorzystania")

licznik = 5

x = 5

for _ in range(x):

    lista = input("Podaj litere: ")

    if lista in slowo:

        print("tak")

        licznik -= 1

        print("Liter do wykorzystania: ", licznik)

        range(x - 1)

    else:

        print("nie")

        licznik -= 1

        print("Liter do wykorzystania: ", licznik)

        range(x - 1)

if licznik == 0:

    lista = input("Wyczerpałeś ilość podpowiedzi, podaj słowo: ")

    if lista == slowo:

        print("Gratulacje odnalazłeś poprawne słowo")

    else:

        print("Nie udało ci się odgadnąć słową")

