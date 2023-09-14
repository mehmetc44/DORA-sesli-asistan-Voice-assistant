import random,time,os,re,phonenumbers,subprocess
from playaudio import playaudio
from gtts import gTTS
import speech_recognition
from phonenumbers import geocoder,carrier,timezone
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import MySubprocess



class Komutlar:
    def konuş(self, konuşma):
        konuşma.lower()
        tts = gTTS(text=konuşma, lang='tr', slow=False)
        file = "Sounds/"+"audio" + str(random.randint(1, 1233442232)) + ".mp3"
        tts.save(file)
        playaudio(file)
        os.remove(file)

    def baslangic_komut(self,süre):
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as kaynak:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(kaynak,duration=1)
            ses = r.listen(kaynak,phrase_time_limit=süre)
        try:
            self.konuşma = r.recognize_google(ses, language="tr")
            self.konuşma = self.konuşma.lower()
            print(self.konuşma)
        except speech_recognition.UnknownValueError:
            print("dediğinizi anyalamadım")
            print("dinliyorum...")
            self.konuşma = self.sesi_kaydet()
        return self.konuşma
    def sesi_kaydet(self):
        r = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as kaynak:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(kaynak,duration=1)
            ses = r.listen(kaynak,phrase_time_limit=8)
        try:
            self.konuşma = r.recognize_google(ses, language="tr")
            self.konuşma = self.konuşma.lower()
            print(self.konuşma)
        except speech_recognition.UnknownValueError:
            print("dediğinizi anyalamadım")
            print("dinliyorum...")
            self.konuşma = self.sesi_kaydet()
        return self.konuşma

    def havadurumu(self,sehir1):
        sehir = sehir1
        apiKey = '6d8588e29198302506e095d95d08a7ea'
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={apiKey}&lang=tr')

        weatherData = response.json()
        hava_durumu = weatherData["weather"][0]["description"]
        sicaklik = round((weatherData['main']['temp'] - 273.15), 2)  # Genel sıcaklık
        hissedilen = round((weatherData['main']['feels_like'] - 273.15), 2)  # hissedilen
        temp_min = round((weatherData['main']['temp_min'] - 273.15), 2)  # Minimum
        temp_max = round((weatherData['main']['temp_max'] - 273.15), 2)  # Maksimum
        self.konuş(f"{sehir} bu gün {hava_durumu}. sıcaklık {sicaklik} derece. hissedilen {hissedilen} derece. detayları anlatmamı istermisin?")
        a = self.sesi_kaydet()
        if "evet" in a or "olur" in a or "anlat" in a:
            self.konuş(f"en yüksek sıcaklık {temp_max} derece. ve en düşük sıcaklık {temp_min} derece.")
        else :
            self.konuş("tamam...")
    def metin_kaydet(self):
        def uzun_konuşma():
            r = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as kaynak:
                r.pause_threshold = 1
                ses = r.listen(kaynak)
                konuşma = r.recognize_google(ses, language="tr")
                konuşma = konuşma.lower()
            return konuşma
        import wmi
        computer = wmi.WMI()
        computer_info = computer.Win32_ComputerSystem()[0]
        usr= computer_info.PrimaryOwnerName
        self.konuş("kaydedeceğim notu söyleyin")

        metin=uzun_konuşma()
        b = random.randint(0,12345)
        dosya = open(fr"C:\Users\{usr}\Desktop\Kayıt{b}.txt","w")
        dosya.write(metin)
        dosya.close()
    def youtube(self,metin):
        self.oi = metin
        if re.search("youtube'dan ", self.oi) != None:
            self.oi = self.oi.replace("youtube'dan ", "")
        elif re.search("bana", self.oi) != None:
            self.oi = self.oi.replace("bana ", "")
        elif re.search("aç", self.oi) != None:
            self.oi = self.oi.replace(" aç", "")
        elif re.search("youtube", self.oi) != None:
            self.oi = self.oi.replace("youtube ", "")
        elif re.search("video", self.oi) != None:
            self.oi = self.oi.replace("video", "")
        elif re.search(" videosunu", self.oi) != None:
            self.oi = self.oi.replace(" videosunu", "")
        path1=os.getcwd()
        os.chdir(MySubprocess.desktop_path.replace(r"//",""))
        subprocess.Popen("start chrome https://www.youtube.com/results?search_query=" + self.oi.replace(" ", "+"),shell=True)
        os.chdir(path1)
    def numaraarastir(self):
        self.konuş("hangi numarayı araştırdığımızı söyle")
        print("dinleniyor...")
        number = self.sesi_kaydet()
        print("araştırıyorum...")
        self.konuş("araştırıyorum...")

        def numara_arastir(numara):
            if number.startswith("artı "):
                numara = number.replace("artı", "+")
                numara_arastir(numara)
            elif number.startswith("+"):
                print("Numara Doğru!")
                Numara = phonenumbers.parse(number)
                zaman = timezone.time_zones_for_number(Numara)
                sim_adi = carrier.name_for_number(Numara, "tr")
                bolge = geocoder.description_for_number(Numara, "tr")
                print("Saat Dilimi :" + str(zaman))
                self.konuş("Saat Dilimi :" + str(zaman).replace("(", ""))
                print("Operatör:", sim_adi)
                self.konuş("Operatör:" + str(sim_adi))
                print("Yaşadığı Ülke(bölge) :", bolge)
                self.konuş("Yaşadığı Ülke(bölge) :" + str(bolge))
            else:
                print(" '+' ülke kodunu kullanarak giriniz.")
                self.konuş("'+' ülke kodunu kullanarak giriniz.")
                numara = self.sesi_kaydet()
                numara_arastir(numara)

        numara_arastir(number)
    def arkaplan_degistir(self,gorsel):
        import ctypes
        path = os.getcwd()
        SPI_SETDESKTOPWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKTOPWALLPAPER, 0, path + fr"\WallPaper\{gorsel}", 3)
    def ekran_goruntusu(self):
        import pyautogui
        from datetime import datetime
        import Cihaz_Bilgileri as cb
        user = cb.kullanici_adi

        date = str(datetime.now()).split(" ")[0].replace("-", "").replace("20", "") + \
               str(datetime.now()).split(" ")[1].split(".")[0].replace(":", "")
        pyautogui.screenshot(fr"C:\Users\{user}\Downloads\screenshot{date}.jpg")





