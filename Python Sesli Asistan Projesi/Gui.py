import time
from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import sys
import shutil
import Cihaz_Bilgileri as CB
import DateTime as dt
import threading
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout,QLabel
from PyQt5.QtCore import QTimer,QDateTime
import psutil
import GPUtil as GPU


class Ui_MainWindow(QMainWindow):

    def cpu_sync(self):
        self.stylesheet_DISK="""
        QFrame{
        border-radius: 110px;
        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:stop1 rgba(85, 255, 127, 255), stop:stop2 rgba(255, 255, 255, 0));
        }
        """
        total, used, free = shutil.disk_usage("/")
        a = 1073741824
        toplam = int(total / a)
        kullanilan = int(used / a)
        bos = int(free / a)

        disk = round(kullanilan/toplam*100,1)
        disk1 = (100 - disk) / 100.0
        disk2 = str(disk1 - 0.001)

        self.Yeni_stylesheet_DISK = self.stylesheet_DISK.replace("stop1", str(disk1)).replace("stop2", str(disk2))
        self.circularProgressDISK.setStyleSheet(self.Yeni_stylesheet_DISK)
        self.labelPercentageDISK.setText(QCoreApplication.translate("MainWindow",
                                                                   f"<p align=\"center\"><span style=\" font-size:36pt;\">{str(disk)}</span><span style=\" font-size:30pt; vertical-align:super;\">%</span></p>",
                                                                   None))
        self.labelCredits_2.setText(QCoreApplication.translate("MainWindow",
                                                               f"<html><head/><body><p>TOPLAM: <span style=\" color:#ffffff;\">{toplam} GB</span></p></body></html>",
                                                               None))





        self.stylesheet_CPU = """
        QFrame{
        border-radius: 110px;	
        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{CW_STOP_2} rgba(85, 170, 255, 255), stop:{CW_STOP_1} rgba(255, 255, 255, 0));
        }
"""


        value = psutil.cpu_percent()
        cpu_freq = psutil.cpu_freq(True)[0]
        cpu_freq = str(cpu_freq).split("current=")[1].split(",")[0].split(".")[0]
        # CPU KULLANIMI
        self.labelPercentageCPU.setText(QCoreApplication.translate("MainWindow",f"<p align=\"center\"><span style=\" font-size:36pt;\">{str(value)}</span><span style=\" font-size:30pt; vertical-align:super;\">%</span></p>",None))
        # CPU FREKANSI
        self.labelCredits.setText(QCoreApplication.translate("MainWindow",
                                                             f"<html><head/><body><p>FREKANS: <span style=\" color:#ffffff;\">{cpu_freq} MHz</span></p></body></html>",
                                                             None))
        val1 = (100 - value) / 100.0
        value1 = str(val1 - 0.001)
        self.Yeni_stylesheet_CPU = self.stylesheet_CPU.replace("{CW_STOP_1}", value1).replace("{CW_STOP_2}", str(val1))
        self.circularProgressCPU.setStyleSheet(self.Yeni_stylesheet_CPU)

        stylesheet_ram="""
        QFrame{
        border-radius: 110px;
        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:stop1 rgba(255, 0, 127, 255), stop:stop2 rgba(255, 255, 255, 0));
        }
        """
        p1 = str(psutil.virtual_memory()).split("=")
        a = 1073741824
        toplam_ram = round(int(p1[1].split(",")[0]) / a, 2)
        kullanilan_ram = round(int(p1[4].split(",")[0]) / a, 2)
        ram=round(kullanilan_ram/ toplam_ram*100,1)
        ram1 = (100 - ram) / 100.0
        ram2 = str(ram1 - 0.001)

        self.labelPercentageRAM.setText(QCoreApplication.translate("MainWindow",
                                                                   f"<p align=\"center\"><span style=\" font-size:36pt;\">{str(ram)}</span><span style=\" font-size:30pt; vertical-align:super;\">%</span></p>",
                                                                   None))
        self.labelCredits_3.setText(QCoreApplication.translate("MainWindow",
                                                               f"<html><head/><body><p>TOPLAM: <span style=\" color:#ffffff;\">{toplam_ram} GB</span></p></body></html>",
                                                               None))

        self.Yeni_stylesheet_RAM=stylesheet_ram.replace("stop1",str(ram1)).replace("stop2",str(ram2))
        self.circularProgressRAM.setStyleSheet(self.Yeni_stylesheet_RAM)


    def setupUi(self, MainWindow,):




        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 550)
        MainWindow.setMinimumSize(QtCore.QSize(750, 550))
        MainWindow.setMaximumSize(QtCore.QSize(750, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Photos/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("Photos/Logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("Photos/Logo.jpg"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("Photos/Logo.jpg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("Photos/Logo.jpg"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("Photos/Logo.jpg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("Photos/Logo.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("Photos/Logo.jpg"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 751, 551))
        self.stackedWidget.setObjectName("stackedWidget")

        ##ANA SAYFA
        self.AnaSayfa = QtWidgets.QWidget()
        self.AnaSayfa.setObjectName("AnaSayfa")
        self.ButonlarFrame = QtWidgets.QFrame(self.AnaSayfa)
        self.ButonlarFrame.setGeometry(QtCore.QRect(0, 0, 171, 551))
        self.ButonlarFrame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.ButonlarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButonlarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButonlarFrame.setObjectName("ButonlarFrame")

        ##HAKKINDA BUTON
        self.HakkindaButton = QtWidgets.QPushButton(self.ButonlarFrame)
        self.HakkindaButton.setGeometry(QtCore.QRect(20, 220, 121, 60))
        self.HakkindaButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Photos/About_tr.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HakkindaButton.setIcon(icon1)
        self.HakkindaButton.setIconSize(QtCore.QSize(180, 60))
        self.HakkindaButton.setObjectName("HakkindaButton")

        ##CIHAZ BUTON
        self.CihazButton = QtWidgets.QPushButton(self.ButonlarFrame)
        self.CihazButton.setGeometry(QtCore.QRect(19, 290, 121, 60))
        self.CihazButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Photos/Device_tr.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.CihazButton.setIcon(icon2)
        self.CihazButton.setIconSize(QtCore.QSize(180, 60))
        self.CihazButton.setCheckable(False)
        self.CihazButton.setObjectName("CihazButton")

        #KULLANIM BUTON
        self.KullanimlarButton = QtWidgets.QPushButton(self.ButonlarFrame)
        self.KullanimlarButton.setGeometry(QtCore.QRect(19, 360, 121, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.KullanimlarButton.sizePolicy().hasHeightForWidth())
        self.KullanimlarButton.setSizePolicy(sizePolicy)
        self.KullanimlarButton.setBaseSize(QtCore.QSize(120, 50))
        self.KullanimlarButton.setToolTipDuration(-1)
        self.KullanimlarButton.setWhatsThis("")
        self.KullanimlarButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.KullanimlarButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Photos/SettingsButton_tr.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KullanimlarButton.setIcon(icon3)
        self.KullanimlarButton.setIconSize(QtCore.QSize(180, 60))
        self.KullanimlarButton.setCheckable(False)
        self.KullanimlarButton.setChecked(False)
        self.KullanimlarButton.setAutoRepeat(False)
        self.KullanimlarButton.setAutoExclusive(False)
        self.KullanimlarButton.setAutoDefault(True)
        self.KullanimlarButton.setDefault(False)
        self.KullanimlarButton.setFlat(False)
        self.KullanimlarButton.setObjectName("KullanimlarButton")

        #DORA GIF
        self.gifFrame = QtWidgets.QFrame(self.AnaSayfa)
        self.gifFrame.setGeometry(QtCore.QRect(140, 0, 751, 551))
        self.gifFrame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.gifFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gifFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.gifFrame.setObjectName("gifFrame")
        self.label = QtWidgets.QLabel(self.gifFrame)
        self.label.setGeometry(QtCore.QRect(-30, 0, 421, 541))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("Photos/MainMenu2.gif"))
        self.label.setObjectName("label")
        self.movie = QMovie("Photos/MainMenu2.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.label_2 = QtWidgets.QLabel(self.gifFrame)
        self.label_2.setGeometry(QtCore.QRect(540, 260, 51, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Photos/DateTimePlace.jpg"))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.AnaSayfa)


        self.label_saat = QtWidgets.QLabel(self.gifFrame)
        self.label_saat.setGeometry(QtCore.QRect(410, 260, 130, 121))
        self.label_saat.setStyleSheet("font: 75 10pt \"Segoe Print\";\n"
                                      "")
        self.label_saat.setObjectName("label_saat")
        self.stackedWidget.addWidget(self.AnaSayfa)

        ##HAKKINDA SAYFASI
        self.HakkindaSayfasi = QtWidgets.QWidget()
        self.HakkindaSayfasi.setStyleSheet("QScrollBar{\n"
"    background-color: rgb(14, 67, 147);\n"
"    width:15px;\n"
"    margin: 15px 0 15px 0;\n"
"    boder-radius:10px;\n"
"    \n"
"    border-color: rgb(0, 0, 0);\n"
"    border-top-color: rgb(0, 0, 0);\n"
"    gridline-color: rgb(0, 0, 0);\n"
"    selection-background-color: rgb(0, 0, 0);\n"
"    selection-color: rgb(0, 0, 0);\n"
"    alternate-background-color: rgb(0, 0, 0);\n"
"}\n"
"QScrollBar::handle:vertical{    \n"
"    \n"
"    background-color: rgb(49, 143, 194);\n"
"    min-height:30px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{\n"
"    \n"
"    background-color: rgb(0, 0, 255);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"    \n"
"    background-color: rgb(49, 143, 194);\n"
"    height:15px;\n"
"    border-top-left-radius:7px;\n"
"    border-top-right-radius:7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover{\n"
"    \n"
"    alternate-background-color: rgb(0, 0, 0);\n"
"    background-color: rgb(6, 150, 254);\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"    background-color: rgb(3, 95, 161);\n"
"}\n"
"QScrollBar::add-line:vertical{\n"
"    border:none;\n"
"    background-color: rgb(49, 143, 194);\n"
"    height:15px;\n"
"    border-bottom-left-radius:7px;\n"
"    border-bottom-right-radius:7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin:margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover{\n"
"    background-color: rgb(6, 150, 254);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"    background-color: rgb(3, 95, 161);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{\n"
"    \n"
"    \n"
"    background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar::up-arrow:vertical,QScrollBar::down-arrow:vertical{\n"
"    background:none;\n"
"}")
        self.HakkindaSayfasi.setObjectName("HakkindaSayfasi")
        self.HakkindaBackground = QtWidgets.QLabel(self.HakkindaSayfasi)
        self.HakkindaBackground.setGeometry(QtCore.QRect(0, 0, 751, 551))
        self.HakkindaBackground.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.HakkindaBackground.setText("")
        self.HakkindaBackground.setObjectName("HakkindaBackground")
        self.scrollArea = QtWidgets.QScrollArea(self.HakkindaSayfasi)
        self.scrollArea.setGeometry(QtCore.QRect(20, 10, 731, 531))
        self.scrollArea.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 716, 1522))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.YaziFrame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.YaziFrame.setEnabled(True)
        self.YaziFrame.setMinimumSize(QtCore.QSize(450, 1500))
        self.YaziFrame.setMaximumSize(QtCore.QSize(16777215, 1500))
        self.YaziFrame.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 11pt \"Segoe Print\";\n")
        self.YaziFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.YaziFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.YaziFrame.setObjectName("YaziFrame")
        self.label_3 = QtWidgets.QLabel(self.YaziFrame)
        self.label_3.setGeometry(QtCore.QRect(280, 10, 121, 61))
        self.label_3.setStyleSheet("font: 15pt \"MS UI Gothic\";\n"
"font: 30pt \"Segoe UI\";\n"
"color: rgb(0, 0, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.YaziFrame)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 671, 201))
        self.label_4.setStyleSheet("color: rgb(190, 190, 190);\n"
"color: rgb(120, 120, 120);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.YaziFrame)
        self.label_5.setGeometry(QtCore.QRect(190, 310, 341, 51))
        self.label_5.setStyleSheet("font: 15pt \"Segoe UI\";\n"
"color: rgb(0, 0, 255);\n"
"color: rgb(0, 0, 0);\n"
"color: rgb(49, 143, 194);\n"
"font: 75 15pt \"Segoe Print\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.YaziFrame)
        self.label_6.setGeometry(QtCore.QRect(20, 370, 681, 651))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.YaziFrame)
        self.label_7.setGeometry(QtCore.QRect(190, 1020, 301, 61))
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(49, 143, 194);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.YaziFrame)
        self.label_8.setGeometry(QtCore.QRect(20, 1090, 451, 201))
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.YaziFrame)
        self.label_9.setGeometry(QtCore.QRect(250, 1300, 191, 61))
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(49, 143, 194);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.YaziFrame)
        self.label_10.setGeometry(QtCore.QRect(10, 1350, 621, 151))
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.YaziFrame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        ##HAKKINDA GERI BUTONU
        self.HakkindaGeriFrame = QtWidgets.QFrame(self.HakkindaSayfasi)
        self.HakkindaGeriFrame.setGeometry(QtCore.QRect(0, 0, 131, 101))
        self.HakkindaGeriFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HakkindaGeriFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HakkindaGeriFrame.setObjectName("HakkindaGeriFrame")
        self.HakkindaGeriButton = QtWidgets.QPushButton(self.HakkindaGeriFrame)
        self.HakkindaGeriButton.setGeometry(QtCore.QRect(0, 0, 61, 61))
        self.HakkindaGeriButton.setStyleSheet("background-color: rgb(85, 255, 255,0);")
        self.HakkindaGeriButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Photos/BackButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        """icon4.addPixmap(QtGui.QPixmap("Photos/BackButton_clicked.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap("Photos/BackButton_clicked.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("Photos/BackButton_clicked.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon4.addPixmap(QtGui.QPixmap("Photos/BackButton_clicked.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("Photos/BackButton_clicked.png"), QtGui.QIcon.Active, QtGui.QIcon.On)"""
        self.HakkindaGeriButton.setIcon(icon4)
        self.HakkindaGeriButton.setIconSize(QtCore.QSize(60, 60))
        self.HakkindaGeriButton.setAutoDefault(True)
        self.HakkindaGeriButton.setObjectName("HakkindaGeriButton")
        self.stackedWidget.addWidget(self.HakkindaSayfasi)

        ##CIHAZ BILGILERI
        self.CihazOzellikleri = QtWidgets.QWidget()
        self.CihazOzellikleri.setObjectName("CihazOzellikleri")
        self.cihaz_bilgileri_arkaplan = QtWidgets.QLabel(self.CihazOzellikleri)
        self.cihaz_bilgileri_arkaplan.setGeometry(QtCore.QRect(0, 0, 750, 550))
        self.cihaz_bilgileri_arkaplan.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.cihaz_bilgileri_arkaplan.setObjectName("cihaz_bilgileri_arkaplan")
        self.frame111 = QtWidgets.QFrame(self.cihaz_bilgileri_arkaplan)
        self.frame111.setGeometry(QtCore.QRect(100,25, 551, 80))
        self.frame111.setStyleSheet("""
        border-radius:40px;
background-color: rgb(85, 85, 127, 100);
""")

        self.cihaz_bilgileri_baslik = QtWidgets.QLabel(self.frame111)
        self.cihaz_bilgileri_baslik.setGeometry(QtCore.QRect(10,10, 531, 61))
        self.cihaz_bilgileri_baslik.setStyleSheet("""color: rgb(49, 143, 194);
background-color: rgb(58, 58, 102);
border-radius:30px;""")
        self.cihaz_bilgileri_baslik.setObjectName("cihaz_bilgileri_baslik")

        self.frame110 = QtWidgets.QFrame(self.cihaz_bilgileri_arkaplan)
        self.frame110.setGeometry(QtCore.QRect(10,120, 231, 401))
        self.frame110.setStyleSheet("""
        border-radius:40px;
background-color: rgb(85, 85, 127, 100);
""")
        self.cihaz_bilgileri_cihazbilgileri = QtWidgets.QLabel(self.frame110)
        self.cihaz_bilgileri_cihazbilgileri.setGeometry(QtCore.QRect(10, 10, 211, 381))
        self.cihaz_bilgileri_cihazbilgileri.setStyleSheet("""
border-radius:30px;
background-color: rgb(58, 58, 102);
""")
        self.cihaz_bilgileri_cihazbilgileri.setObjectName("cihaz_bilgileri_cihazbilgileri")



        self.frame109 = QtWidgets.QFrame(self.cihaz_bilgileri_arkaplan)
        self.frame109.setGeometry(QtCore.QRect(260, 120, 481, 401))
        self.frame109.setStyleSheet("""border-radius:40px;
background-color: rgb(85, 85, 127, 100);
""")
        self.cihaz_bilgileri_deger = QtWidgets.QLabel(self.frame109)
        self.cihaz_bilgileri_deger.setGeometry(QtCore.QRect(10, 10, 461, 381))
        self.cihaz_bilgileri_deger.setStyleSheet("""color: rgb(49, 143, 194);
background-color: rgb(58, 58, 102);
border-radius:30px;""")
        self.cihaz_bilgileri_deger.setObjectName("cihaz_bilgileri_deger")






        #CIHAZ OZELLIKLERI GERI BUTON
        self.CihazGeriFrame = QtWidgets.QFrame(self.CihazOzellikleri)
        self.CihazGeriFrame.setGeometry(QtCore.QRect(0, 0, 91, 71))
        self.CihazGeriFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CihazGeriFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CihazGeriFrame.setObjectName("CihazGeriFrame")
        self.CihazGeriButton = QtWidgets.QPushButton(self.CihazGeriFrame)
        self.CihazGeriButton.setGeometry(QtCore.QRect(0, 0, 61, 61))
        self.CihazGeriButton.setStyleSheet("background-color: rgb(85, 255, 255,0);")
        self.CihazGeriButton.setText("")
        self.CihazGeriButton.setIcon(icon4)
        self.CihazGeriButton.setIconSize(QtCore.QSize(60, 60))
        self.CihazGeriButton.setAutoDefault(True)
        self.CihazGeriButton.setObjectName("CihazGeriButton")
        self.stackedWidget.addWidget(self.CihazOzellikleri)

        ##KULLANIMLAR SAYFASI
        self.KullanimlarSayfasi = QtWidgets.QWidget()
        self.KullanimlarSayfasi.setObjectName("KullanimlarSayfasi")
        self.frame = QtWidgets.QFrame(self.KullanimlarSayfasi)
        self.frame.setGeometry(QtCore.QRect(0, 0, 751, 551))
        self.frame.setStyleSheet("\n"
"background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame112 = QtWidgets.QFrame(self.frame)
        self.frame112.setGeometry(QtCore.QRect(100,25, 551, 80))
        self.frame112.setStyleSheet("""
        border-radius:40px;
background-color: rgb(85, 85, 127, 100);
""")

        self.KullanimlarBaslik = QtWidgets.QLabel(self.frame112)
        self.KullanimlarBaslik.setGeometry(QtCore.QRect(10,10, 531, 61))
        self.KullanimlarBaslik.setStyleSheet("""color: rgb(49, 143, 194);
background-color: rgb(58, 58, 102);
border-radius:30px;""")
        self.KullanimlarBaslik.setObjectName("KullanimlarBaslik")



        ##=============================================Kullanım Widgetler==================================================================================
        ##=================================================================================================================================================



        self.circularProgressCPU = QFrame(self.KullanimlarSayfasi)
        self.circularProgressCPU.setObjectName(u"circularProgressCPU")
        self.circularProgressCPU.setGeometry(QRect(10, 200, 220, 220))
        #self.circularProgressCPU.setStyleSheet(u"QFrame{\nborder-radius: 110px;	\nbackground-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.400 rgba(85, 170, 255, 255), stop:0.395 rgba(255, 255, 255, 0));\n}")


        self.circularProgressCPU.setFrameShape(QFrame.StyledPanel)
        self.circularProgressCPU.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.KullanimlarSayfasi)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 200, 220, 220))
        self.circularBg.setStyleSheet(u"QFrame{\n"
                                      "	border-radius: 110px;	\n"
                                      "	background-color: rgba(85, 85, 127, 100);\n"
                                      "}")
        self.circularBg.setFrameShape(QFrame.StyledPanel)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.circularContainer = QFrame(self.KullanimlarSayfasi)
        self.circularContainer.setObjectName(u"circularContainer")
        self.circularContainer.setGeometry(QRect(25, 215, 190, 190))
        self.circularContainer.setBaseSize(QSize(0, 0))
        self.circularContainer.setStyleSheet(u"QFrame{\n"
                                             "	border-radius: 95px;	\n"
                                             "	background-color: rgb(58, 58, 102);\n"
                                             "}")
        self.circularContainer.setFrameShape(QFrame.StyledPanel)
        self.circularContainer.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.circularContainer)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 171, 125))
        self.infoLayout = QGridLayout(self.layoutWidget)
        self.infoLayout.setObjectName(u"infoLayout")
        self.infoLayout.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName = QLabel(self.layoutWidget)
        self.labelAplicationName.setObjectName(u"labelAplicationName")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        self.labelAplicationName.setFont(font)
        self.labelAplicationName.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName.setAlignment(Qt.AlignCenter)

        self.infoLayout.addWidget(self.labelAplicationName, 0, 0, 1, 1)

        self.labelPercentageCPU = QLabel(self.layoutWidget)
        self.labelPercentageCPU.setObjectName(u"labelPercentageCPU")
        font1 = QFont()
        font1.setFamily(u"Roboto Thin")
        font1.setPointSize(30)
        self.labelPercentageCPU.setFont(font1)
        self.labelPercentageCPU.setStyleSheet(u"color: rgb(115, 185, 255); padding: 0px; background-color: none;")
        self.labelPercentageCPU.setAlignment(Qt.AlignCenter)
        self.labelPercentageCPU.setIndent(-1)

        self.infoLayout.addWidget(self.labelPercentageCPU, 1, 0, 1, 1)

        self.labelCredits = QLabel(self.layoutWidget)
        self.labelCredits.setObjectName(u"labelCredits")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        self.labelCredits.setFont(font2)
        self.labelCredits.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits.setAlignment(Qt.AlignCenter)

        self.infoLayout.addWidget(self.labelCredits, 2, 0, 1, 1)

        self.circularBg.raise_()
        self.circularProgressCPU.raise_()
        self.circularContainer.raise_()


        #GPU GRAFİĞİ
        self.circularProgressDISK = QFrame(self.KullanimlarSayfasi)
        self.circularProgressDISK.setObjectName(u"circularProgressDISK")
        self.circularProgressDISK.setGeometry(QRect(265, 200, 220, 220))

        self.circularProgressDISK.setFrameShape(QFrame.StyledPanel)
        self.circularProgressDISK.setFrameShadow(QFrame.Raised)
        self.circularBg_2 = QFrame(self.KullanimlarSayfasi)
        self.circularBg_2.setObjectName(u"circularBg_2")
        self.circularBg_2.setGeometry(QRect(265, 200, 220, 220))
        self.circularBg_2.setStyleSheet(u"QFrame{\n"
                                        "	border-radius: 110px;	\n"
                                        "	background-color: rgba(85, 85, 127, 100);\n"
                                        "}")
        self.circularBg_2.setFrameShape(QFrame.StyledPanel)
        self.circularBg_2.setFrameShadow(QFrame.Raised)
        self.circularContainer_2 = QFrame(self.KullanimlarSayfasi)
        self.circularContainer_2.setObjectName(u"circularContainer_2")
        self.circularContainer_2.setGeometry(QRect(280, 215, 190, 190))
        self.circularContainer_2.setBaseSize(QSize(0, 0))
        self.circularContainer_2.setStyleSheet(u"QFrame{\n"
                                               "	border-radius: 95px;	\n"
                                               "	background-color: rgb(58, 58, 102);\n"
                                               "}")
        self.circularContainer_2.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget_2 = QWidget(self.circularContainer_2)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 40, 171, 127))
        self.infoLayout_2 = QGridLayout(self.layoutWidget_2)
        self.infoLayout_2.setObjectName(u"infoLayout_2")
        self.infoLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_2 = QLabel(self.layoutWidget_2)
        self.labelAplicationName_2.setObjectName(u"labelAplicationName_2")
        self.labelAplicationName_2.setFont(font)
        self.labelAplicationName_2.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_2.setAlignment(Qt.AlignCenter)

        self.infoLayout_2.addWidget(self.labelAplicationName_2, 0, 0, 1, 1)

        self.labelPercentageDISK = QLabel(self.layoutWidget_2)
        self.labelPercentageDISK.setObjectName(u"labelPercentageDISK")
        self.labelPercentageDISK.setFont(font1)
        self.labelPercentageDISK.setStyleSheet(u"color: rgb(115, 255, 171); padding: 0px; background-color: none;")
        self.labelPercentageDISK.setAlignment(Qt.AlignCenter)
        self.labelPercentageDISK.setIndent(-1)

        self.infoLayout_2.addWidget(self.labelPercentageDISK, 1, 0, 1, 1)

        self.labelCredits_2 = QLabel(self.layoutWidget_2)
        self.labelCredits_2.setObjectName(u"labelCredits_2")
        self.labelCredits_2.setFont(font2)
        self.labelCredits_2.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_2.setAlignment(Qt.AlignCenter)

        self.infoLayout_2.addWidget(self.labelCredits_2, 2, 0, 1, 1)

        self.circularBg_2.raise_()
        self.circularProgressDISK.raise_()
        self.circularContainer_2.raise_()












        self.circularProgressRAM = QFrame(self.KullanimlarSayfasi)
        self.circularProgressRAM.setObjectName(u"circularProgressRAM")
        self.circularProgressRAM.setGeometry(QRect(520, 200, 220, 220))
        self.circularProgressRAM.setFrameShape(QFrame.StyledPanel)
        self.circularProgressRAM.setFrameShadow(QFrame.Raised)
        self.circularBg_3 = QFrame(self.KullanimlarSayfasi)
        self.circularBg_3.setObjectName(u"circularBg_3")
        self.circularBg_3.setGeometry(QRect(520, 200, 220, 220))
        self.circularBg_3.setStyleSheet(u"QFrame{\n"
                                        "	border-radius: 110px;	\n"
                                        "	background-color: rgba(85, 85, 127, 100);\n"
                                        "}")
        self.circularBg_3.setFrameShape(QFrame.StyledPanel)
        self.circularBg_3.setFrameShadow(QFrame.Raised)
        self.circularContainer_3 = QFrame(self.KullanimlarSayfasi)
        self.circularContainer_3.setObjectName(u"circularContainer_3")
        self.circularContainer_3.setGeometry(QRect(535, 215, 190, 190))
        self.circularContainer_3.setBaseSize(QSize(0, 0))
        self.circularContainer_3.setStyleSheet(u"QFrame{\n"
                                               "	border-radius: 95px;	\n"
                                               "	background-color: rgb(58, 58, 102);\n"
                                               "}")
        self.circularContainer_3.setFrameShape(QFrame.StyledPanel)
        self.circularContainer_3.setFrameShadow(QFrame.Raised)
        self.layoutWidget_3 = QWidget(self.circularContainer_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(10, 40, 171, 125))
        self.infoLayout_3 = QGridLayout(self.layoutWidget_3)
        self.infoLayout_3.setObjectName(u"infoLayout_3")
        self.infoLayout_3.setContentsMargins(0, 0, 0, 0)
        self.labelAplicationName_3 = QLabel(self.layoutWidget_3)
        self.labelAplicationName_3.setObjectName(u"labelAplicationName_3")
        self.labelAplicationName_3.setFont(font)
        self.labelAplicationName_3.setStyleSheet(u"color: #FFFFFF; background-color: none;")
        self.labelAplicationName_3.setAlignment(Qt.AlignCenter)

        self.infoLayout_3.addWidget(self.labelAplicationName_3, 0, 0, 1, 1)

        self.labelPercentageRAM = QLabel(self.layoutWidget_3)
        self.labelPercentageRAM.setObjectName(u"labelPercentageRAM")
        self.labelPercentageRAM.setFont(font1)
        self.labelPercentageRAM.setStyleSheet(u"color: rgb(255, 44, 174); padding: 0px; background-color: none;")
        self.labelPercentageRAM.setAlignment(Qt.AlignCenter)
        self.labelPercentageRAM.setIndent(-1)

        self.infoLayout_3.addWidget(self.labelPercentageRAM, 1, 0, 1, 1)

        self.labelCredits_3 = QLabel(self.layoutWidget_3)
        self.labelCredits_3.setObjectName(u"labelCredits_3")
        self.labelCredits_3.setFont(font2)
        self.labelCredits_3.setStyleSheet(u"color: rgb(148, 148, 216); background-color: none;")
        self.labelCredits_3.setAlignment(Qt.AlignCenter)

        self.infoLayout_3.addWidget(self.labelCredits_3, 2, 0, 1, 1)

        self.circularBg_3.raise_()
        self.circularProgressRAM.raise_()
        self.circularContainer_3.raise_()

        self.run_ing = QtCore.QTimer()
        self.run_ing.timeout.connect(self.cpu_sync)
        self.run_ing.start(1000)











        ##KULLANIMLAR GERI BUTON
        self.KullanimlarGeriFrame = QtWidgets.QFrame(self.frame)
        self.KullanimlarGeriFrame.setGeometry(QtCore.QRect(0, 0, 71, 61))
        self.KullanimlarGeriFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.KullanimlarGeriFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.KullanimlarGeriFrame.setObjectName("KullanimlarGeriFrame")
        self.KullanimlarGeriButton = QtWidgets.QPushButton(self.KullanimlarGeriFrame)
        self.KullanimlarGeriButton.setGeometry(QtCore.QRect(0, 0, 61, 61))
        self.KullanimlarGeriButton.setStyleSheet("background-color: rgb(85, 255, 255,0);")
        self.KullanimlarGeriButton.setText("")
        self.KullanimlarGeriButton.setIcon(icon4)
        self.KullanimlarGeriButton.setIconSize(QtCore.QSize(60, 60))
        self.KullanimlarGeriButton.setAutoDefault(True)
        self.KullanimlarGeriButton.setObjectName("KullanimlarGeriButton")
        self.stackedWidget.addWidget(self.KullanimlarSayfasi)
        MainWindow.setCentralWidget(self.centralwidget)

        ##BUTON BAGLANTILARI
        self.HakkindaButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.HakkindaSayfasi))
        self.HakkindaGeriButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AnaSayfa))

        self.KullanimlarButton.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.KullanimlarSayfasi))
        self.KullanimlarGeriButton.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.AnaSayfa))

        self.CihazButton.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.CihazOzellikleri))
        self.CihazGeriButton.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.AnaSayfa))

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        zamanlayici = QTimer(self)
        zamanlayici.timeout.connect(self.zamanigoster)
        zamanlayici.start(1000)
    def zamanigoster(self):
        zaman = QTime.currentTime()
        tarih = QDate.currentDate()
        tmetin = tarih.toString("dd/MM/yyyy")
        metin = zaman.toString("hh:mm")
        if zaman.second()%2 == 0:
            metin = metin[:2] + " " + metin[3:]
        self.text0 = f"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">{str(tmetin)}</span></p><p align=\"right\"><span style=\" color:#ffffff;\">{str(metin)}</span></p><p align=\"right\"><span style=\" color:#ffffff;\">Türkiye</span></p></body></html>"
        self.label_saat.setText(self.text0)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DORA"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; font-weight:600;\">DORA</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">DORA v1.0 Mehmet Çakmak tarafından kişisel bir uygulama olarak</span></p><p align=\"center\"><span style=\" font-size:11pt;\">üretilmiştir. Yapımının %100 ünde Pyhton dili kullanımış olup</span></p><p align=\"center\"><span style=\" font-size:11pt;\"> Teelif hakları ve patenti saklıdır. Kaynak kodlarını kullanmak </span></p><p align=\"center\"><span style=\" font-size:11pt;\">isteyenler mehmetc4400@gmail.com üzerinden iletişime geçebilir.</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">NELER YAPABİLİRSİN</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\">&quot;DORA&quot; diyerek DORA yı aktif edebilirsiniz. </p><p align=\"justify\">-Kısmen sohbet edebilir</p><p align=\"justify\">-Hava durumunu öğrenebilir</p><p align=\"justify\">-Bilgisayarınızı kapatıp yeniden başlatabilir.</p><p align=\"justify\">-Söylediğiniz şeyleri metne çevirip kaydedebilir</p><p align=\"justify\">-Spotify,Google,Tureng,LinkedIn,Steam,GitHub açabilir</p><p align=\"justify\">-Döviz çevirici uygulamayı açabilir</p><p align=\"justify\">-İstediğiniz bir numaranın operatör bilgisini öğrenebilir</p><p align=\"justify\">-Duvar Kağıdınızı değiştirebilir</p><p align=\"justify\">-Ekran Görüntüsü aldırabilir</p><p align=\"justify\">-Netflix den film açabilir</p><p align=\"justify\">-Aklından belli aralıkta sayı tutumasını </p><p align=\"justify\"> sağlayabilirsiniz.</p><p align=\"justify\">-Cihaz kullanım bilgilerini görebilirsiniz </p><p>NOT : Yeni sürümler ile daha fazla özellik eklenecektir.</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">EMEĞİ GEÇENLER</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Tasarım: Mehmet ÇAKMAK</span></p><p><span style=\" font-size:11pt;\">Kodlama: Mehmet ÇAKMAK</span></p><p><span style=\" font-size:11pt;\">Fikir Babası: Mehmet ÇAKMAK</span></p><p><span style=\" font-size:11pt;\">İsim Babası: Muaz SAYİR</span></p><p><span style=\" font-size:11pt;\">Moral - Motivasyon Destek: Sena YİĞİT</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">HESAPLAR</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">GitHub : https://github.com/mehmetc44</span></p><p><span style=\" font-size:11pt;\">LinkedIn: https://www.linkedin.com/in/mehmet-%C3%A7akmak-737196241/</span></p><p><span style=\" font-size:11pt;\">İnstagram: mehmetc_official</span></p></body></html>"))
        self.cihaz_bilgileri_arkaplan.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.cihaz_bilgileri_baslik.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">CİHAZ BİLGİLERİ</span></p></body></html>"))


        self.text11= f"<html><head/><body><p><span style=\" color:#ffffff;\">{CB.cihaz_model} </span></p><p><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" color:#ffffff;\">{CB.kullanici_adi}</span></p><p><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" color:#ffffff;\">{CB.isletim_sistemi}</span></p><p><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" color:#ffffff;\">{CB.cpu_adi}</span></p><p><span style=\" color:#ffffff;\"><br/></span></p><p><span style=\" color:#ffffff;\">{CB.ekran_karti_ismi}</span></p></body></html"
        self.cihaz_bilgileri_deger.setText(_translate("MainWindow",f"""<html><head/><body><p align=\'center\'><span style=\' font-size:11pt; color:#ffffff;\'>{CB.cihaz_model}</span></p><p align=\'center\'><span style=\' 
font-size:11pt;\'><br/></span></p><p align=\'center\'><span style=\' font-size:11pt; color:#ffffff;\'>
{CB.kullanici_adi}</span></p><p align=\'center\'><span style=\' font-size:11pt;\'><br/></span></p><p align=\'center\'>
<span style=\' font-size:11pt; color:#ffffff;\'>{CB.isletim_sistemi}</span></p><p align=\'center\'><span style=\' font-size:11pt;
\'><br/></span></p><p align=\'center\'><span style=\' font-size:11pt; color:#ffffff;\'>{CB.cpu_adi}</span></p><p align=\'center\'><span style=
\' font-size:11pt;\'><br/></span></p><p align=\'center\'><span style=\' font-size:11pt; color:#ffffff;\'>{CB.ekran_karti_ismi}</span></p></body></html>""" ))
        self.cihaz_bilgileri_cihazbilgileri.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">CİHAZ MODELİ : </span></p><p align=\"center\"><span style=\" font-size:11pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">AKTİF KULLANICI:</span></p><p align=\"center\"><span style=\" font-size:11pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">İŞLETİM SİSTEMİ:</span></p><p align=\"center\"><span style=\" font-size:11pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">CPU MODELİ:</span></p><p align=\"center\"><span style=\" font-size:11pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:11pt; color:#ffffff;\">EKRAN KARTI MODELİ:</span></p></body></html>"))

        self.KullanimlarBaslik.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">KULLANIMLAR</span></p></body></html>"))

        self.text10 = f"<html><head/><body><p align=\"right\"><span style=\" color:#ffffff;\">{dt.Tarih()}</span></p><p align=\"right\"><span style=\" color:#ffffff;\">{dt.Saat()}</span></p><p align=\"right\"><span style=\" color:#ffffff;\">Türkiye</span></p></body></html>"
        self.label_saat.setText(_translate("MainWindow",self.text10))
        self.labelAplicationName.setText(QCoreApplication.translate("MainWindow", u"<strong>CPU</strong> USAGE", None))


        self.labelAplicationName_2.setText(
            QCoreApplication.translate("MainWindow", u"<strong>DISK</strong> USAGE", None))
        self.labelAplicationName_3.setText(QCoreApplication.translate("MainWindow", u"<strong>RAM</strong> USAGE", None))



def arayuz():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




