import random,time,os,re,phonenumbers,datetime
from playsound import playsound
from playaudio import playaudio
from gtts import gTTS
import speech_recognition
import pyaudio
from phonenumbers import geocoder,carrier,timezone
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import SohbetSeti
from KomutSeti import Komutlar
import threading
import Cihaz_Bilgileri as CB
import MySubprocess,subprocess


def eylemebasla():
    print("dinleniyor...")
    konuşma = asistan.sesi_kaydet()
    if "uyu" in konuşma or "uyku modu" in konuşma or "uykuya geç" in konuşma:
        asistan.konuş(random.choice(SohbetSeti.Sohbet["uykumodu"]))
        AsistanCalismaFonksiyonu()
    else:
        asistan.eylem(konuşma)
        eylemebasla()
def AsistanCalismaFonksiyonu():
    while 1:
        print("dinliyorum...")
        ses = asistan.baslangic_komut(3)
        if "dora" in ses :
            asistan.konuş(random.choice(SohbetSeti.Sohbet["hazır"]))
            eylemebasla()



class assistant(Komutlar):
    def __init__(self):
        self.Dongu = True
    def eylem(self,konuşma):
        def sohbetsecim(secim):
            return random.choice(SohbetSeti.Sohbet[secim])
        def baskabisey():
            self.konuş(sohbetsecim("yardım"))
            konuşma1 = self.sesi_kaydet()
            print("dinliyorum...")
            if "evet" in konuşma1 or "var" in konuşma1:
                self.konuş(sohbetsecim("emir_iste"))
                print("dinliyorum...")
                ses = self.sesi_kaydet()

                self.eylem(ses)
            elif "hayır" in konuşma1 or "sağol" in konuşma1:
                self.konuş("tamamdır")
                AsistanCalismaFonksiyonu()
            else:
                eylemebasla()

        if "youtube'dan" in konuşma or "youtube" in konuşma or "video aç" in konuşma or "videosunu aç" in konuşma or "videosu aç" in konuşma:
            self.konuş("açıyorum")
            metin = konuşma
            asistan.youtube(metin)
            baskabisey()
        elif "netlix" in konuşma and "aç" in konuşma:
            self.konuş("açıyorum")
            MySubprocess.Netflix()
            baskabisey()
        elif "spotify" in konuşma and "aç" in konuşma:
            self.konuş("açıyorum")
            MySubprocess.spotify()
            baskabisey()
        elif "tureng" in konuşma and "aç" in konuşma:
            self.konuş("açıyorum")
            MySubprocess.tureng()
            baskabisey()
        elif "valorant" in konuşma and "aç" in konuşma:
            self.konuş("açıyorum")
            MySubprocess.valorant()
            baskabisey()
        elif "linkedin" in konuşma and "aç" in konuşma:
            self.konuş("açıyorum")
            MySubprocess.linkedin()
            baskabisey()
        elif "steam" in konuşma and "aç" in konuşma:
            self.konuş("açıyorum")
            MySubprocess.steam()
            baskabisey()
        elif "github" in konuşma and "aç" in konuşma:
            self.konuş("açıyorum")
            MySubprocess.Github()
            baskabisey()
        elif "google" in konuşma and "aç" in konuşma:
            self.konuş("açıyorum")
            MySubprocess.Google()
            baskabisey()
        elif "chrome" in konuşma and "aç" in konuşma:
            self.konuş("açıyorum")
            MySubprocess.Google()
            baskabisey()
        elif "numarayı araştır" in konuşma or "numaryı sorgula" in konuşma:
            self.numaraarastir()
            baskabisey()
        elif"döviz çevir" in konuşma:
            import CurrencyConventer
            baskabisey()
        elif "söylediklerimi kaydet" in konuşma or "söyleyeceklerimi kaydet" in konuşma or "dediklerimi kaydet" in konuşma or "diyeceklerimi kaydet" in konuşma:
            self.konuş("kaydedeceğim şeyleri söyle")
            print("metni dinliyorum...")
            self.metin_kaydet()
            self.konuş("kayıt başarılı")
            baskabisey()
        elif "hava durumu" in konuşma or "havadurumu" in konuşma :
            metin = konuşma.split(" ")[0]
            self.havadurumu(metin)
            baskabisey()
        elif "hava" in konuşma and "nasıl" in konuşma:
            metin = konuşma.split('\'')[0]
            self.havadurumu(metin)
            baskabisey()
        elif "bilgisayarı kapat" in konuşma or "cihazı kapat" in konuşma:
            subprocess.Popen("shudown /s", shell=True)
            baskabisey()
        elif "bilgisayarı yeniden başlat" in konuşma or "cihazı yeniden başlat" in konuşma:
            subprocess.Popen("shudown /r", shell=True)
            baskabisey()
        elif "arka plan değiştir" in konuşma or "arka planı değiştir" in konuşma or "duvar kağıdı değiştir" in konuşma or "duvar kağıdını değiştir" in konuşma:
            self.konuş("değiştiriyorum...")
            liste = os.listdir(os.getcwd() + r"\WallPaper")
            self.arkaplan_degistir(random.choice(liste))
            self.konuş("beğendin mi")
            print("dinliyorum...")
            cevap = self.sesi_kaydet()
            if "evet" in cevap or "çok güzel" in cevap:
                self.konuş("tabi güzel olacak ben yaptım sonuçta")
            baskabisey()
        elif "ekran görüntüsü al" in konuşma or "ss al" in konuşma:
            self.ekran_goruntusu()
            self.konuş("aldım.")
            baskabisey()
        elif "sayı tut" in konuşma or "sayı söyle" in konuşma:
            sayi = re.findall("\d+", konuşma)
            self.konuş(str(random.randint(int(sayi[0]), int(sayi[1]))))
            baskabisey()
        elif "teşekkürler" in konuşma or  "teşekkür ederim" in konuşma:
            self.konuş(sohbetsecim("rica"))
            baskabisey()
        elif "nasılsın" in konuşma or "durumlar nasıl" in konuşma or "hayat nasıl" in konuşma or "hayatın nasıl" in konuşma:
            self.konuş(sohbetsecim("iyiyim"))
        elif "nasılım" in konuşma or "nasıl görünüyorum" in konuşma:
            self.konuş(sohbetsecim("övgü"))
        elif "harika" in konuşma:
            self.konuş("sağol adamım sende harika görünüyorsun.")
        else:
            self.konuş("üzgünüm dediğinizi anlamadım ne yapmamı istersiniz")
            print("dinliyorum...")
            eylemebasla()
asistan = assistant()



import Gui


t1 = threading.Thread(target=AsistanCalismaFonksiyonu)

t2= threading.Thread(target=Gui.arayuz)
t2.start()
t1.start()
