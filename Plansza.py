import tkinter as tk
from Swiat import Swiat
from Punkt import Punkt
from Gatunki import Gatunki
from PIL import Image, ImageTk


class Plansza(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self._swiat = Swiat(Punkt(10, 10))
        self._rozmiar_ramki = Punkt(480, 480)
        self._rozmiar_swiata = self._swiat.get_rozmiar
        self._rozmiar_obrazka = self._rozmiar_ramki / self._rozmiar_swiata
        self.config(width=self._rozmiar_ramki.x, height=self._rozmiar_ramki.y)
        self._canvas = tk.Canvas(self, width=self._rozmiar_ramki.x, height=self._rozmiar_ramki.y)
        self._canvas.bind("<Button-1>", lambda event: self.klik(event))
        self._obrazki_raw = {}
        self._obrazki = {}
        # for g in Gatunki:
        # g = Gatunki.WILK
        for g in Gatunki:
            name = "assets/" + g.name.lower() + ".png"
            plik = Image.open(name)
            self._obrazki_raw[g] = plik.crop(box=(0, 0, 32, 32))
            self._obrazki[g] = ImageTk.PhotoImage(plik.resize((self._rozmiar_obrazka.x,
                                                               self._rozmiar_obrazka.y),
                                                              Image.ANTIALIAS))
        plik = Image.open("assets/celownik.png")
        self._obrazki_raw["celownik"] = plik.crop(box=(0, 0, 32, 32))
        self._obrazki["celownik"] = ImageTk.PhotoImage(plik.resize((self._rozmiar_obrazka.x,
                                                                    self._rozmiar_obrazka.y),
                                                                   Image.ANTIALIAS))
        self.rysuj()

    def nastepna_runda(self):
        self._swiat.nastepna_runda()
        self.rysuj()

    def nowa_gra(self):
        from tkinter import simpledialog
        nowy_rozmiar = Punkt()
        nowy_rozmiar.x = tk.simpledialog.askinteger("Nowa gra", "Podaj szerokosc")
        nowy_rozmiar.y = tk.simpledialog.askinteger("Nowa gra", "Podaj wysokosc")
        if nowy_rozmiar.x == None or nowy_rozmiar.y == None:
            return

        self._rozmiar_swiata = nowy_rozmiar
        self._rozmiar_obrazka = self._rozmiar_ramki / self._rozmiar_swiata
        # zmiana rozmiaru obrazkow
        for key in self._obrazki_raw:
            self._obrazki[key] = ImageTk.PhotoImage(self._obrazki_raw[key].resize((self._rozmiar_obrazka.x,
                                                                                   self._rozmiar_obrazka.y),
                                                                                  Image.ANTIALIAS))
        self._swiat.nowa_gra(nowy_rozmiar)
        self.rysuj()

    def rysuj(self):
        self._canvas.delete("all")
        skala = Punkt()
        skala.x = self._rozmiar_obrazka.x / 32
        skala.y = self._rozmiar_obrazka.y / 32
        self._canvas.create_rectangle(0, 0, self._rozmiar_ramki.x, self._rozmiar_ramki.y, fill="#55D24B")
        for i in range(self._rozmiar_swiata.x):
            self._canvas.create_line(i * self._rozmiar_obrazka.x, 0, i * self._rozmiar_obrazka.x, self._rozmiar_ramki.y)

        for j in range(self._rozmiar_swiata.y):
            self._canvas.create_line(0, j * self._rozmiar_obrazka.y, self._rozmiar_ramki.x, j * self._rozmiar_obrazka.y)

        for o in self._swiat.get_wszystkie_organizmy():
            pozycja = o.get_pozycja
            self._canvas.create_image(pozycja.x * self._rozmiar_obrazka.x + int(self._rozmiar_obrazka.x * 0.5),
                                      pozycja.y * self._rozmiar_obrazka.y + int(self._rozmiar_obrazka.y * 0.5),
                                      image=self._obrazki[o.get_gatunek])
            if o.get_gatunek == Gatunki.CZLOWIEK and o.get_nastepny_ruch != Punkt(0, 0):
                self._canvas.create_image(
                    (pozycja.x + o.get_nastepny_ruch.x) * self._rozmiar_obrazka.x + int(self._rozmiar_obrazka.x * 0.5),
                    (pozycja.y + o.get_nastepny_ruch.y) * self._rozmiar_obrazka.y + int(self._rozmiar_obrazka.y * 0.5),
                    image=self._obrazki["celownik"])
        self._canvas.pack()


    def klik(self,event):
        if self.master.org_do_stworzenia.get() != "Stworz organizm":

            poz = Punkt()
            poz.x = int(event.x/self._rozmiar_obrazka.x)
            poz.y = int(event.y/self._rozmiar_obrazka.y)
            self._swiat.stworz_organizm(Gatunki[self.master.org_do_stworzenia.get()],poz)
            self.master.org_do_stworzenia.set("Stworz organizm")
            self.rysuj()

    def obsluga_klawatury(self, event):
        czlowiek = self._swiat.get_czlowiek()
        if czlowiek != None:
            if event.keysym == "Down":
                czlowiek.set_nastepny_ruch(Punkt(0, 1))
            elif event.keysym == "Left":
                czlowiek.set_nastepny_ruch(Punkt(-1, 0))
            elif event.keysym == "Up":
                czlowiek.set_nastepny_ruch(Punkt(0, -1))
            elif event.keysym == "Right":
                czlowiek.set_nastepny_ruch(Punkt(1, 0))
            self.rysuj()

    def super_moc(self):
        cz = self._swiat.get_czlowiek()
        if cz != None:
            cz.aktywuj_moc()
            self._swiat.narrator.opowiadaj()

    def ustaw_pole_narratora(self, pole):
        self._swiat.narrator.ustaw_pole_tekstowe(pole)

    def zapisz_gre(self):
        from tkinter import filedialog
        nazwa = tk.filedialog.asksaveasfilename(initialdir="/", title="Select file")
        # print(plik)
        plik = open(nazwa, "w")
        self._swiat.zapisz(plik)
        plik.close()

    def wczytaj_gre(self):
        from tkinter import filedialog
        nazwa_pliku = tk.filedialog.askopenfilename()
        plik = open(nazwa_pliku, "r")
        if plik != None:
            self._swiat.wczytaj(plik)
            plik.close()
            self._rozmiar_swiata = self._swiat.get_rozmiar.get_lokacja
            self._rozmiar_obrazka = self._rozmiar_ramki / self._rozmiar_swiata
            # zmiana rozmiaru obrazkow
            for key in self._obrazki_raw:
                self._obrazki[key] = ImageTk.PhotoImage(self._obrazki_raw[key].resize((self._rozmiar_obrazka.x,
                                                                                       self._rozmiar_obrazka.y),
                                                                                      Image.ANTIALIAS))
            self.rysuj()
