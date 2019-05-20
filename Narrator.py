import tkinter as tk


class Narrator():
    def __init__(self):
        self._pole_tekstowe = None
        self._wydarzenia = []

    def ustaw_pole_tekstowe(self, pol_tekst):
        self._pole_tekstowe = pol_tekst

    def org_umarl_przez_org(self, o1, o2):
        self._wydarzenia.append(str(o1) + " umarl" + o1.plec() + " przez " + str(o2))

    def org_rozmnozyl_sie(self, o):
        self._wydarzenia.append(str(o) + " rozmnozyl" + o.plec() + " sie")

    def org_uzyl_mocy(self, o, nazwa):
        self._wydarzenia.append(str(o) + " uzyl" + o.plec() + " mocy: " + nazwa)

    def mocy_pozostalo(self, nazwa, pozostalo):
        self._wydarzenia.append("Mocy " + nazwa + " pozostało: " +str(pozostalo) + " rund.")

    def moc_odnowi_sie_za(self, nazwa, odnowienie):
        self._wydarzenia.append("Moc " + nazwa + " odnowi się za: " + str(odnowienie) + " rund.")

    def moc_odnowiona(self, nazwa):
        self._wydarzenia.append("Moc " + nazwa + " zostala odnowiona.")

    def wczytano_gre(self, nazwa):
        self._wydarzenia.append("Wczytano gre o nazwie: " + nazwa)

    def opowiadaj(self):
        self._pole_tekstowe.config(state=tk.NORMAL)
        self._pole_tekstowe.delete('1.0', tk.END)
        #self._pole_tekstowe.update()
        for st in self._wydarzenia:
            self._pole_tekstowe.insert(tk.END, st + "\n")

        self._wydarzenia.clear()
        self._pole_tekstowe.config(state=tk.DISABLED)
