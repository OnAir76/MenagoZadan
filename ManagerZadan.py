from datetime import datetime
from zadania import Zadanie, ZadaniePriorytetowe, ZadanieRegularne

class ManagerZadan:
    """
    Klasa zarządzająca listą zadań.

    :param zadania: Lista zadań.
    """

    def __init__(self):
        self.zadania = []

    def dodaj_zadanie(self, zadanie):
        """
        Dodaje zadanie do listy.

        :param zadanie: Zadanie do dodania.
        """
        self.zadania.append(zadanie)

    def usun_zadanie(self, zadanie):
        """
        Usuwa zadanie z listy.

        :param zadanie: Zadanie do usunięcia.
        """
        """Usuwa zadanie z listy."""
        if zadanie in self.zadania:
            self.zadania.remove(zadanie)

    def oznacz_jako_wykonane(self, zadanie):
        """Oznacza zadanie jako wykonane."""
        zadanie.oznacz_jako_wykonane()

    def edytuj_zadanie(self, zadanie, nowy_tytul, nowy_opis, nowy_termin):
        """Edycja szczegółów zadania."""
        zadanie.tytul = nowy_tytul
        zadanie.opis = nowy_opis
        zadanie.termin_wykonania = datetime.strptime(nowy_termin, "%Y-%m-%d")

    def wyswietl_zadania(self):
        """Wyświetla wszystkie zadania."""
        for zadanie in self.zadania:
            print(zadanie)

    def sortuj_zadania(self):
        """Sortuje zadania według terminu wykonania."""
        self.zadania.sort(key=lambda z: z.termin_wykonania)

    def zapisz_do_pliku(self, nazwa_pliku):
        """Zapisuje zadania do pliku tekstowego."""
        with open(nazwa_pliku, 'w') as plik:
            for zadanie in self.zadania:
                plik.write(
                    f"{zadanie.tytul};{zadanie.opis};{zadanie.termin_wykonania.strftime('%Y-%m-%d')};{int(zadanie.wykonane)}\n")

    def wczytaj_z_pliku(self, nazwa_pliku):
        """Wczytuje zadania z pliku tekstowego."""
        try:
            with open(nazwa_pliku, 'r') as plik:
                for linia in plik:
                    tytul, opis, termin, wykonane = linia.strip().split(';')
                    zadanie = Zadanie(tytul, opis, termin)
                    zadanie.wykonane = bool(int(wykonane))
                    self.dodaj_zadanie(zadanie)
        except FileNotFoundError:
            print(f"Plik {nazwa_pliku} nie został znaleziony.")
        except Exception as e:
            print(f"Wystąpił błąd podczas wczytywania z pliku: {e}")
