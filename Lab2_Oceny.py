# importujemy funkcje z modułu Lab2_Oceny2 
from Lab2_Oceny2 import drukuj, srednia, mediana, odchylenie


def main(args):
    przedmioty = set(['polski', 'angielski']) 
    drukuj(przedmioty, "Lista przedmiotów zawiera: ")

    print("\nAby przerwać wprowadzanie przedmiotów, naciśnij Enter.")
    while True:
        przedmiot = input("Podaj nazwę przedmiotu: ")
        if len(przedmiot):
            if przedmiot in przedmioty:  
                print("Ten przedmiot już mamy :-)")
            przedmioty.add(przedmiot)  
        else:
            drukuj(przedmioty, "\nTwoje przedmioty: ")
            przedmiot = input("\nZ którego przedmiotu wprowadzisz oceny? ")
          
            if przedmiot not in przedmioty:
                print("Brak takiego przedmiotu, możesz go dodać.")
            else:
                break  

    oceny = []  
    ocena = None  
    print("\nAby przerwać wprowadzanie ocen, podaj 0 (zero).")

    while not ocena:
        try:
            ocena = int(input("Podaj ocenę (1-6): "))
            if (ocena > 0 and ocena < 7):
                oceny.append(float(ocena))
            elif ocena == 0:
                break
            else:
                print("Błędna ocena.")
            ocena = None
        except ValueError:
            print("Błędne dane!")

    drukuj(oceny, przedmiot.capitalize() + " - wprowadzone oceny: ")
    s = srednia(oceny)  
    m = mediana(oceny)  
    o = odchylenie(oceny, s) 
    print("\nŚrednia: {0:5.2f}".format(s))
    print("Mediana: {0:5.2f}\nOdchylenie: {1:5.2f}".format(m, o))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))