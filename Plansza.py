import tkinter as tk
from Swiat import Swiat
from Punkt import Punkt
from Gatunki import Gatunki
from PIL import Image, ImageTk


class Plansza(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#55D24B")
        self.master = master
        # self.bind("<Button-1>", Plansza.klik)
        self._swiat = Swiat(Punkt(10, 10))
        self._rozmiar_ramki = Punkt(480, 480)
        self._rozmiar_swiata = self._swiat.get_rozmiar
        self._rozmiar_obrazka = self._rozmiar_ramki / self._rozmiar_swiata
        self.config(width=self._rozmiar_ramki.x, height=self._rozmiar_ramki.y)
        self._canvas = tk.Canvas(self, width=self._rozmiar_ramki.x, height=self._rozmiar_ramki.y)
        self._canvas.bind("<Button-1>", Plansza.klik)
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
                                      pozycja.y * self._rozmiar_obrazka.x + int(self._rozmiar_obrazka.y * 0.5),
                                      image=self._obrazki[o.get_gatunek])
            if o.get_gatunek == Gatunki.CZLOWIEK and o.get_nastepny_ruch != Punkt(0,0):
                self._canvas.create_image((pozycja.x + o.get_nastepny_ruch.x) * self._rozmiar_obrazka.x + int(self._rozmiar_obrazka.x * 0.5),
                                          (pozycja.y + o.get_nastepny_ruch.y) * self._rozmiar_obrazka.x + int(self._rozmiar_obrazka.y * 0.5),
                                      image=self._obrazki["celownik"])
        self._canvas.pack(fill=tk.BOTH, expand=1)

        # def stworz_widgets(self):
        #     self.hi_there = tk.Button(self)
        #     self.hi_there["text"] = "Hello World\n(click me)"
        #     self.hi_there["command"] = self.say_hi
        #     self.hi_there.pack(side="top")
        #
        #     self.quit = tk.Button(self, text="QUIT", fg="red",
        #                           command=self.master.destroy)
        #     self.quit.pack(side="bottom")
        #
        # def say_hi(self):
        #     print("hi there, everyone!")

    @staticmethod
    def klik(event):
        print("Clicked at:", event.x, event.y)

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

    def ustaw_pole_narratora(self, pole):
        self._swiat.narrator.ustaw_pole_tekstowe(pole)