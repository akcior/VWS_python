import tkinter as tk
from Plansza import Plansza


class Okno_sym(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # .grid_propagate(True)
        # self.grid_columnconfigure(4,minsize=100)
        # label1 = tk.Label(text="aslfdkjasdf").grid(row=0, column=1)
        # label1.grid(row=1, column=1)
        self.geometry('960x480')
        self.plansza = Plansza(self)
        self.plansza.grid(row=0, column=0)
        label = tk.Label(text="pole narratora").grid(row=1, column=0)
        menubar = tk.Menu(self)
        menubar.add_command(label="Quit", command=self.quit)
        menubar.add_command(label="Nastepna runda", command=self.plansza.nastepna_runda)
        self.title("Swiat Wirtualny Jakub Lecki 175494")
        self.config(menu=menubar)
