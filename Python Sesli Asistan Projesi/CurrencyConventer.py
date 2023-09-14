import tkinter
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import requests
from tkinter import *
import customtkinter



class CurrencyConventer:
    def __init__(self):
        self.pencere = Tk()
        self.pencere.title('Döviz Çevirici')
        html = requests.get("https://canlidoviz.com/").content
        self.soup = BeautifulSoup(html, "html.parser")

        canvas = Canvas(self.pencere, width=750, height=450 ) #çizilebilir pencere oluşturduk
        canvas.pack()#canvası yerleştirdik.
        self.pencere.resizable(width=False,height=False)
    def Frames(self):
        self.limg = Label(self.pencere,background="#062531")
        self.limg.place(x=0,y=0,relheight=1,relwidth=1)
        #ÜST KISIM
        self.ust_kisim = Frame(self.pencere,bg='#01141e')
        self.ust_kisim.place(relx=0.07,rely=0.05,relheight=0.2,relwidth=0.85)

        #SOL ALT
        self.sol_alt = Frame(self.pencere, bg='#01141e')
        self.sol_alt.place(relx=0.07,rely=0.3,relheight= 0.6,relwidth=0.3)
        #SAĞ ALT
        self.sag_alt = Frame(self.pencere,bg='#01141e')
        self.sag_alt.place(relx=0.4, rely= 0.3,relheight= 0.6,relwidth=0.52)
    def DovizDegerleri(self):

        degerler = self.soup.find_all("td", {"class": "canli text-mobile-value"})
        degerler2 = self.soup.findChildren("div",{"class":"currency-card__content"})

        self.dolar = round(float(str(degerler[0]).split(">")[1].split("<")[0].replace(",",".")),4)
        self.euro = round(float(str(degerler[1]).split(">")[1].split("<")[0].replace(",",".")),4)
        self.sterlin = round(float(str(degerler[4]).split(">")[1].split("<")[0].replace(",",".")),4)
        self.frang = round(float(str(degerler[14]).split(">")[1].split("<")[0].replace(",",".")),4)
        self.bitcoin= round(float(str(degerler2[0]).split('<')[3].split('>')[1].replace(",",".")),4)
        gram= str(degerler[2]).split(">")[1].split("<")[0].replace(".","")
        gram= gram[:-5] + "." +gram[-4:]
        self.gram_altin = round(float(gram),4)
        ons = str(degerler[15]).split(">")[1].split("<")[0].replace(".", "")
        ons = ons[:-5] + "." + ons[-4:]
        self.ons_altin = round(float(ons),4)
        ceyrek = str(degerler[17]).split(">")[1].split("<")[0].replace(".", "")
        ceyrek = ceyrek[:-5] + "." + ceyrek[-4:]
        self.ceyrek_altin = round(float(ceyrek),4)
        tam = str(degerler[19]).split(">")[1].split("<")[0].replace(".", "")
        tam = tam[:-5] + "." + tam[-4:]

        self.tam_altın = round(float(tam),4)
        #DOLAR
        dolar_metin = Label(self.ust_kisim, text="USD", fg='light blue', bg='#01141e', font='calibri 14 bold')
        dolar_metin.place(relx=0.1, rely=0.1)
        dolar_deger_metin = Label(self.ust_kisim, text=self.dolar, fg='white', bg='#01141e', font='calibri 14 bold')
        dolar_deger_metin.place(relx=0.08, rely=0.5)
        #EURO
        euro_metin = Label(self.ust_kisim, text="EUR", fg='light blue', bg='#01141e', font='calibri 14 bold')
        euro_metin.place(relx=0.27, rely=0.1)
        euro_deger_metin = Label(self.ust_kisim, text=self.euro, fg='white', bg='#01141e', font='calibri 14 bold')
        euro_deger_metin.place(relx=0.25, rely=0.5)
        #STERLIN
        sterlin_metin = Label(self.ust_kisim, text="GBP", fg='light blue', bg='#01141e', font='calibri 14 bold')
        sterlin_metin.place(relx=0.45, rely=0.1)
        sterlin_deger_metin = Label(self.ust_kisim, text= self.sterlin, fg='white', bg='#01141e', font='calibri 14 bold')
        sterlin_deger_metin.place(relx=0.43, rely=0.5)
        #FRANK
        frank_metin = Label(self.ust_kisim, text="CHF", fg='light blue', bg='#01141e', font='calibri 14 bold')
        frank_metin.place(relx=0.62, rely=0.1)
        frank_deger_metin = Label(self.ust_kisim, text= self.frang, fg='white', bg='#01141e', font='calibri 14 bold')
        frank_deger_metin.place(relx=0.6, rely=0.5)
        #BITCOIN
        bitcoin_metin = Label(self.ust_kisim, text="BTC", fg='light blue', bg='#01141e', font='calibri 14 bold')
        bitcoin_metin.place(relx=0.80, rely=0.1)
        bitcoin_deger_metin = Label(self.ust_kisim, text= self.bitcoin, fg='white', bg='#01141e', font='calibri 14 bold')
        bitcoin_deger_metin.place(relx=0.79, rely=0.5)
        #GRAM ALTIN
        gram_altin_metin = Label(self.sol_alt, text="GRAM A.", fg='light green', bg='#01141e', font='calibri 14 bold')
        gram_altin_metin.place(relx=0.08, rely=0.1)
        gram_altin_deger_metin = Label(self.sol_alt, text= self.gram_altin, fg='white', bg='#01141e', font='calibri 14 bold')
        gram_altin_deger_metin.place(relx=0.07, rely=0.2)
        #ONS ATIN
        ons_altin_metin = Label(self.sol_alt, text="ONS A.", fg='light green', bg='#01141e', font='calibri 14 bold')
        ons_altin_metin.place(relx=0.56, rely=0.1)
        ons_altin_deger_metin = Label(self.sol_alt, text=self.ons_altin, fg='white', bg='#01141e', font='calibri 14 bold')
        ons_altin_deger_metin.place(relx=0.55, rely=0.2)

        #CEYREK ALTIN
        ceyrek_altin_metin = Label(self.sol_alt, text="CEYREK A.", fg='light green', bg='#01141e', font='calibri 14 bold')
        ceyrek_altin_metin.place(relx=0.08, rely=0.5)
        ceyrek_altin_deger_metin = Label(self.sol_alt, text=self.ceyrek_altin, fg='white', bg='#01141e', font='calibri 14 bold')
        ceyrek_altin_deger_metin.place(relx=0.07, rely=0.6)
        #TAM ALTIN
        tam_altin_metin = Label(self.sol_alt, text="TAM A.", fg='light green', bg='#01141e', font='calibri 14 bold')
        tam_altin_metin.place(relx=0.56, rely=0.5)
        tam_altin_deger_metin = Label(self.sol_alt, text=self.tam_altın, fg='white', bg='#01141e', font='calibri 14 bold')
        tam_altin_deger_metin.place(relx=0.54, rely=0.6)

        self.Secenek = customtkinter.CTkOptionMenu(button_color="#1a4d68",fg_color="#1a4d68",master= self.sag_alt, values=["TL","USD", "EUR", "GBP", "CHF","BTC","GRAM A.","ONS A.","CEYREK A.","TAM A."],width= 10,corner_radius=50)
        self.Secenek.place(relx=0.12 , rely=0.3)
        self.Secenek.set("me")
        self.Secenek2 = customtkinter.CTkOptionMenu(button_color="#1a4d68",fg_color="#1a4d68",master=self.sag_alt,values=['TL',"USD", "EUR", "GBP", "CHF", "BTC", "GRAM A.", "ONS A.","CEYREK A.", "TAM A."],width=50,corner_radius=50,)
        self.Secenek2.place(relx=0.6, rely=0.3)
        metin = Label(self.sag_alt, text="Çevirici", fg='white', bg='#01141e', font='calibri 20 bold')
        metin.place(relx=0.36,rely=0.04)
        metin2 = Label(self.sag_alt, text="==>", fg='white', bg='#01141e', font='calibri 20 bold')
        metin2.place(relx=0.43, rely=0.28)

        self.entry1 = customtkinter.CTkEntry(master= self.sag_alt,width=120,height=25,corner_radius=15)
        self.entry1.place(relx=0.1,rely=0.55)





        def hesapla():
            entry_degeri = int(self.entry1.get())
            ilk = self.Secenek.get()
            ikinci = self.Secenek2.get()


            if ilk == 'USD':
                if ikinci == 'TL':
                    self.deger = self.dolar * entry_degeri
                elif ikinci == 'EUR':
                    self.deger=self.dolar/self.euro*entry_degeri
                elif ikinci == 'GBP':
                    self.deger=self.dolar/self.sterlin*entry_degeri
                elif ikinci == 'CHF':
                    self.deger=self.dolar/self.frang*entry_degeri
                elif ikinci == 'BTC':
                    self.deger=self.bitcoin*entry_degeri
                elif ikinci == 'GRAM A.':
                    self.deger=self.dolar/self.gram_altin*entry_degeri
                elif ikinci == 'ONS A.':
                    self.deger = self.dolar/self.ons_altin*entry_degeri
                elif ikinci == 'CEYREK A.' :
                    self.deger = self.dolar/self.ceyrek_altin * entry_degeri
                elif ikinci == "TAM A.":
                    self.deger = self.dolar/self.tam_altın * entry_degeri

            elif ilk == 'EUR':
                if ikinci == 'TL':
                    self.deger = self.euro * entry_degeri
                elif ikinci == 'USD':
                    self.deger = self.euro / self.dolar * entry_degeri
                elif ikinci == 'GBP':
                    self.deger = self.euro / self.sterlin * entry_degeri
                elif ikinci == 'CHF':
                    self.deger = self.euro / self.frang * entry_degeri
                elif ikinci == 'BTC':
                    self.deger = self.bitcoin*self.dolar/self.euro * entry_degeri
                elif ikinci == 'GRAM A.':
                    self.deger = self.euro / self.gram_altin * entry_degeri
                elif ikinci == 'ONS A.':
                    self.deger = self.euro / self.ons_altin * entry_degeri
                elif ikinci == 'CEYREK A.':
                    self.deger = self.euro / self.ceyrek_altin * entry_degeri
                elif ikinci == "TAM A.":
                    self.deger = self.euro / self.tam_altın * entry_degeri

            elif ilk == 'GBP':
                if ikinci == 'TL':
                    self.deger = self.sterlin * entry_degeri
                elif ikinci == 'USD':
                    self.deger = self.sterlin / self.dolar * entry_degeri
                elif ikinci == 'EUR':
                    self.deger = self.sterlin / self.euro * entry_degeri
                elif ikinci == 'CHF':
                    self.deger = self.sterlin / self.frang * entry_degeri
                elif ikinci == 'BTC':
                    self.deger = self.bitcoin * self.dolar / self.sterlin * entry_degeri
                elif ikinci == 'GRAM A.':
                    self.deger = self.sterlin / self.gram_altin * entry_degeri
                elif ikinci == 'ONS A.':
                    self.deger = self.sterlin / self.ons_altin * entry_degeri
                elif ikinci == 'CEYREK A.':
                    self.deger = self.sterlin / self.ceyrek_altin * entry_degeri
                elif ikinci == "TAM A.":
                    self.deger = self.sterlin / self.tam_altın * entry_degeri
            elif ilk == 'TL':
                if ikinci == 'GBP':
                    self.deger = self.sterlin * entry_degeri
                elif ikinci == 'USD':
                    self.deger = self.dolar * entry_degeri
                elif ikinci == 'EUR':
                    self.deger =  self.euro * entry_degeri
                elif ikinci == 'CHF':
                    self.deger =  self.frang * entry_degeri
                elif ikinci == 'BTC':
                    self.deger = self.bitcoin *  entry_degeri
                elif ikinci == 'GRAM A.':
                    self.deger = self.gram_altin * entry_degeri
                    self.deger = 1 / self.deger
                elif ikinci == 'ONS A.':
                    self.deger =  self.ons_altin * entry_degeri
                    self.deger = 1 / self.deger
                elif ikinci == 'CEYREK A.':
                    self.deger =  1/(self.ceyrek_altin * entry_degeri)
                elif ikinci == "TAM A.":
                    self.deger =  self.tam_altın * entry_degeri
                    self.deger=1/self.deger
            elif ilk == 'CHF':
                if ikinci == 'TL':
                    self.deger = self.frang * entry_degeri
                elif ikinci == 'USD':
                    self.deger = self.frang / self.dolar * entry_degeri
                elif ikinci == 'EUR':
                    self.deger = self.frang / self.euro * entry_degeri
                elif ikinci == 'GBP':
                    self.deger = self.frang / self.sterlin * entry_degeri
                elif ikinci == 'BTC':
                    self.deger = self.bitcoin * self.dolar / self.frang * entry_degeri
                elif ikinci == 'GRAM A.':
                    self.deger = self.frang / self.gram_altin * entry_degeri
                elif ikinci == 'ONS A.':
                    self.deger = self.frang / self.ons_altin * entry_degeri
                elif ikinci == 'CEYREK A.':
                    self.deger = self.frang / self.ceyrek_altin * entry_degeri
                elif ikinci == "TAM A.":
                    self.deger = self.frang / self.tam_altın * entry_degeri
            elif ilk == 'BTC':
                if ikinci == 'TL':
                    self.deger = self.bitcoin * entry_degeri * self.dolar
                elif ikinci == 'USD':
                    self.deger = self.bitcoin * entry_degeri
                elif ikinci == 'EUR':
                    self.deger = self.bitcoin / self.euro * self.dolar * entry_degeri
                elif ikinci == 'CHF':
                    self.deger = self.bitcoin / self.frang * entry_degeri * self.dolar
                elif ikinci == 'GBP':
                    self.deger = self.bitcoin * self.dolar / self.sterlin * entry_degeri
                elif ikinci == 'GRAM A.':
                    self.deger = self.bitcoin / self.gram_altin * self.dolar * entry_degeri
                elif ikinci == 'ONS A.':
                    self.deger = self.bitcoin *self.dolar/ self.ons_altin * entry_degeri
                elif ikinci == 'CEYREK A.':
                    self.deger = self.bitcoin * self.dolar / self.ceyrek_altin * entry_degeri
                elif ikinci == "TAM A.":
                    self.deger = self.bitcoin * self.dolar / self.tam_altın * entry_degeri
            elif ilk == 'GRAM A.':
                if ikinci == 'TL':
                    self.deger = self.gram_altin * entry_degeri
                elif ikinci == 'USD':
                    self.deger = self.gram_altin / self.dolar * entry_degeri
                elif ikinci == 'EUR':
                    self.deger = self.gram_altin / self.euro * entry_degeri
                elif ikinci == 'GBP':
                    self.deger = self.gram_altin / self.sterlin * entry_degeri
                elif ikinci == 'BTC':
                    self.deger = self.bitcoin * self.dolar / self.gram_altin * entry_degeri
                elif ikinci == 'CHF':
                    self.deger = self.gram_altin / self.frang * entry_degeri
                elif ikinci == 'ONS A.':
                    self.deger = self.gram_altin / self.ons_altin * entry_degeri
                elif ikinci == 'CEYREK A.':
                    self.deger = self.gram_altin / self.ceyrek_altin * entry_degeri
                elif ikinci == "TAM A.":
                    self.deger = self.gram_altin / self.tam_altın * entry_degeri
            elif ilk == 'CEYREK A.':
                if ikinci == 'TL':
                    self.deger = self.ceyrek_altin * entry_degeri
                elif ikinci == 'USD':
                    self.deger = self.ceyrek_altin / self.dolar * entry_degeri
                elif ikinci == 'EUR':
                    self.deger = self.ceyrek_altin / self.euro * entry_degeri
                elif ikinci == 'GBP':
                    self.deger = self.ceyrek_altin / self.sterlin * entry_degeri
                elif ikinci == 'BTC':
                    self.deger = self.bitcoin * self.dolar / self.ceyrek_altin * entry_degeri
                elif ikinci == 'CHF':
                    self.deger = self.ceyrek_altin / self.frang * entry_degeri
                elif ikinci == 'ONS A.':
                    self.deger = self.ceyrek_altin / self.ons_altin * entry_degeri
                elif ikinci == 'GRAM A.':
                    self.deger = self.ceyrek_altin / self.gram_altin * entry_degeri
                elif ikinci == "TAM A.":
                    self.deger = self.ceyrek_altin / self.tam_altın * entry_degeri
            elif ilk == 'ONS A.':
                if ikinci == 'TL':
                    self.deger = self.ons_altin * entry_degeri
                elif ikinci == 'USD':
                    self.deger = self.ons_altin / self.dolar * entry_degeri
                elif ikinci == 'EUR':
                    self.deger = self.ons_altin / self.euro * entry_degeri
                elif ikinci == 'GBP':
                    self.deger = self.ons_altin / self.sterlin * entry_degeri
                elif ikinci == 'BTC':
                    self.deger = self.bitcoin * self.dolar / self.ons_altin * entry_degeri
                elif ikinci == 'CHF':
                    self.deger = self.ons_altin / self.frang * entry_degeri
                elif ikinci == 'ONS A.':
                    self.deger = self.ons_altin / self.ceyrek_altin * entry_degeri
                elif ikinci == 'GRAM A.':
                    self.deger = self.ons_altin / self.gram_altin * entry_degeri
                elif ikinci == "TAM A.":
                    self.deger = self.ons_altin / self.tam_altın * entry_degeri
            elif ilk == 'TAM A.':
                if ikinci == 'TL':
                    self.deger = self.tam_altın * entry_degeri
                elif ikinci == 'USD':
                    self.deger = self.tam_altın / self.dolar * entry_degeri
                elif ikinci == 'EUR':
                    self.deger = self.tam_altın/ self.euro * entry_degeri
                elif ikinci == 'GBP':
                    self.deger = self.tam_altın / self.sterlin * entry_degeri
                elif ikinci == 'BTC':
                    self.deger = self.bitcoin * self.dolar / self.tam_altın * entry_degeri
                elif ikinci == 'CHF':
                    self.deger = self.tam_altın/ self.frang * entry_degeri
                elif ikinci == 'CEYREK A.':
                    self.deger = self.tam_altın / self.ceyrek_altin * entry_degeri
                elif ikinci == 'GRAM A.':
                    self.deger = self.tam_altın / self.gram_altin * entry_degeri
                elif ikinci == "ONS A.":
                    self.deger =  self.tam_altın/self.ons_altin * entry_degeri
            elif ilk == ikinci:
                self.deger = 1 * entry_degeri

            label.configure(text=str(round(self.deger, 4)),text_color="black")

        label = customtkinter.CTkLabel(master=self.sag_alt, text='Sonuc', width=120, height=23, corner_radius=15,
                                       bg_color="light blue", fg_color='white',text_color="black")
        label.place(relx=0.73, rely=0.586, anchor=tkinter.CENTER)
        button = customtkinter.CTkButton(master=self.sag_alt,text="Çevir",command= hesapla,width=120,height=32,border_width=0,corner_radius=15)
        button.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)


        self.pencere.mainloop()


doviz = CurrencyConventer()
doviz.Frames()
doviz.DovizDegerleri()