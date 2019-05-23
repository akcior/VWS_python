import tkinter as tk
from Plansza import Plansza
from Gatunki import Gatunki


class Okno_sym(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # .grid_propagate(True)
        # self.grid_columnconfigure(4,minsize=100)
        # label1 = tk.Label(text="aslfdkjasdf").grid(row=0, column=1)
        # label1.grid(row=1, column=1)
        self.geometry('1120x480')
        plansza = Plansza(self)
        plansza.pack(side=tk.LEFT)  # grid(row=0, column=0)
        # label = tk.Label(text="pole narratora").grid(row=1, column=0)
        ramka_narratora = tk.Frame(self)
        scrollbar = tk.Scrollbar(self)
        ramka_narratora.config(width=480, height=480)
        pole_narratora = tk.Text(ramka_narratora, yscrollcommand=scrollbar.set)
        pole_narratora.config(width=480)
        # for i in range(1000):
        #     pole_narratora.insert(tk.END, str(i) +"\n")
        plansza.ustaw_pole_narratora(pole_narratora)
        scrollbar.config(command=pole_narratora.yview, width=15)
        pole_narratora.pack(side=tk.LEFT, expand=0, fill=tk.Y)  # grid(row=0, column=2)
        ramka_narratora.pack(side=tk.LEFT, expand=0, fill=tk.NONE)
        ramka_narratora.pack_propagate(False)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)  # grid(row=0, column=3)
        menubar = tk.Menu(self)
        menubar.add_command(label="Quit", command=self.quit)
        menubar.add_command(label="Nastepna runda", command=plansza.nastepna_runda)
        menubar.add_command(label="Super moc", command=plansza.super_moc)
        menubar.add_command(label="Nowa gra", command=plansza.nowa_gra)
        menubar.add_command(label="Zapisz gre", command=plansza.zapisz_gre)
        menubar.add_command(label="Wczytaj gre", command=plansza.wczytaj_gre)
        self.org_do_stworzenia = tk.StringVar(self)
        self.org_do_stworzenia.set("Stworz organizm")
        opt_menu = tk.OptionMenu(self, self.org_do_stworzenia, *Gatunki.list())
        opt_menu.pack(side=tk.LEFT)
        # menubar.add_command(label="Stworz organizm", command=opt_menu.pack)
        self.bind("<Key>", plansza.obsluga_klawatury)
        self.title("Swiat Wirtualny Jakub Lecki 175494")
        self.config(menu=menubar)
