import datetime

def Tarih():
        #Tarih
    a = datetime.datetime.now()
    date1 = datetime.datetime.strftime(a, '%x')
    date2 = date1.split("/")
    tarih = date2[1]+"/"+date2[0]+"/"+str(a.year)
    return tarih

def Saat():

    #Saat
    b = datetime.datetime.strftime(datetime.datetime.now(), '%X')
    saat = b.split(":")[0] + ":" + b.split(":")[1]
    return saat