"""
main.py - Główny moduł aplikacji do zarządzania zadaniami.
"""
from zadania import Zadanie, ZadaniePriorytetowe, ZadanieRegularne
from ManagerZadan import ManagerZadan
from datetime import datetime
import time

def czas_wykonania(func):
    """Dekorator do mierzenia czasu wykonania funkcji."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Czas wykonania funkcji '{func.__name__}': {end_time - start_time:.4f} sekund")
        return result
    return wrapper

def menu():
    """
       Wyświetla menu opcji dla użytkownika.
    """
    print("\n1. Dodaj zadanie")
    print("2. Usuń zadanie")
    print("3. Oznacz jako wykonane")
    print("4. Edytuj zadanie")
    print("5. Wyświetl zadania")
    print("6. Sortuj zadania")
    print("7. Zapisz zadania do pliku")
    print("8. Wczytaj zadania z pliku")
    print("9. Wyjście")

def main():
    """
    Główna funkcja programu, która zarządza logiką aplikacji.
    """
    manager = ManagerZadan()
    while True:
        menu()
        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            typ_zadania = input("Typ zadania \n1 - priorytetowe\n2 - regularne \n").lower()
            tytul = input("Tytuł: ")
            opis = input("Opis: ")
            termin = input("Termin (YYYY-MM-DD) [naciśnij Enter, aby ustawić na dzisiaj]: ")
            if termin == "":
                termin = datetime.today().strftime("%Y-%m-%d")

            # Wprowadzenie dodatkowych informacji
            dodatkowe_informacje = {}
            while True:
                klucz = input("Podaj dodatkowy klucz (lub naciśnij Enter, aby zakończyć): ")
                if klucz == "":
                    break
                wartosc = input(f"Podaj wartość dla {klucz}: ")
                dodatkowe_informacje[klucz] = wartosc

            if typ_zadania == "1":
                priorytet = input("Priorytet: ")
                zadanie = ZadaniePriorytetowe(tytul, opis, termin, priorytet, **dodatkowe_informacje)
            elif typ_zadania == "2":
                powtarzalnosc = input("Powtarzalność: ")
                zadanie = ZadanieRegularne(tytul, opis, termin, powtarzalnosc, **dodatkowe_informacje)
            else:
                zadanie = Zadanie(tytul, opis, termin, **dodatkowe_informacje)

            manager.dodaj_zadanie(zadanie)

        elif wybor == "2":
            tytul = input("Podaj tytuł zadania do usunięcia: ")
            for zadanie in manager.zadania:
                if zadanie.tytul == tytul:
                    manager.usun_zadanie(zadanie)
                    break

        elif wybor == "3":
            tytul = input("Podaj tytuł zadania do oznaczenia jako wykonane: ")
            for zadanie in manager.zadania:
                if zadanie.tytul == tytul:
                    manager.oznacz_jako_wykonane(zadanie)
                    break

        elif wybor == "4":
            tytul = input("Podaj tytuł zadania do edycji: ")
            for zadanie in manager.zadania:
                if zadanie.tytul == tytul:
                    nowy_tytul = input("Nowy tytuł: ")
                    nowy_opis = input("Nowy opis: ")
                    nowy_termin = input("Nowy termin (YYYY-MM-DD) [naciśnij Enter, aby nie zmieniać]: ")
                    if nowy_termin == "":
                        nowy_termin = zadanie.termin_wykonania.strftime("%Y-%m-%d")  # Nie zmieniaj daty, jeśli nie podano
                    manager.edytuj_zadanie(zadanie, nowy_tytul, nowy_opis, nowy_termin)
                    break

        elif wybor == "5":
            manager.wyswietl_zadania()

        elif wybor == "6":
            manager.sortuj_zadania()
            print("Zadania zostały posortowane według terminu wykonania.")

        elif wybor == "7":
            nazwa_pliku = input("Podaj nazwę pliku do zapisu: ")
            manager.zapisz_do_pliku(nazwa_pliku)

        elif wybor == "8":
            nazwa_pliku = input("Podaj nazwę pliku do wczytania: ")
            manager.wczytaj_z_pliku(nazwa_pliku)

        elif wybor == "9":
            print("Koniec programu.")
            break

if __name__ == "__main__":
    main()
