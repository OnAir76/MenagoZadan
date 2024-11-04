from datetime import datetime


class Zadanie:
    """
        Klasa reprezentująca zadanie.

        :param tytul: Tytuł zadania.
        :param opis: Opis zadania.
        :param termin_wykonania: Termin wykonania zadania w formacie YYYY-MM-DD.
        """

    def __init__(self, tytul, opis, termin_wykonania=None, **kwargs):
        self.tytul = tytul
        self.opis = opis
        if termin_wykonania is None:
            termin_wykonania = datetime.today().strftime("%Y-%m-%d")
        self.termin_wykonania = datetime.strptime(termin_wykonania, "%Y-%m-%d")
        self.wykonane = False
        self.dodatkowe_informacje = kwargs  # Przechowywanie dodatkowych informacji w słowniku

    def __str__(self):
        """
            Zwraca reprezentację tekstową zadania.
        """
        status = "Wykonane" if self.wykonane else "Niewykonane"
        dodatkowe = ', '.join([f"{key}: {value}" for key, value in self.dodatkowe_informacje.items()])
        return f"{self.tytul} - {self.opis} (Termin: {self.termin_wykonania.date()}) [{status}] {dodatkowe}"

    def oznacz_jako_wykonane(self):
        """
        Oznacza zadanie jako wykonane.
        """
        self.wykonane = True


class ZadaniePriorytetowe(Zadanie):
    """Klasa reprezentująca zadanie priorytetowe."""

    def __init__(self, tytul, opis, termin_wykonania=None, priorytet=None, **kwargs):
        super().__init__(tytul, opis, termin_wykonania, **kwargs)
        self.priorytet = priorytet

    def __str__(self):
        status = super().__str__()
        return f"{status} (Priorytet: {self.priorytet})"


class ZadanieRegularne(Zadanie):
    """Klasa reprezentująca zadanie regularne."""

    def __init__(self, tytul, opis, termin_wykonania=None, powtarzalnosc=None, **kwargs):
        super().__init__(tytul, opis, termin_wykonania, **kwargs)
        self.powtarzalnosc = powtarzalnosc

    def __str__(self):
        status = super().__str__()
        return f"{status} (Powtarzalność: {self.powtarzalnosc})"
