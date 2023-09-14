import wmi
import os
import psutil
import DateTime as dt
import GPUtil as GPU
GPUs = GPU.getGPUs()
for gpu in GPUs:
    print("GPU RAM Free: {0:.0f}MB | Used: {1:.0f}MB | Util {2:3.0f}% | Total {3:.0f}MB".format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil*100, gpu.memoryTotal))

dt.Tarih()

#SICAKLIK ÖLÇÜLERİ

computer = wmi.WMI()
computer_info = computer.Win32_ComputerSystem()[0]
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0]

ram_GB = round(float(os_info.TotalVisibleMemorySize) / 1048576,2 ) # KB to GB
ram_yuzdesi = psutil.virtual_memory()[2]
cpu_kullanimi = psutil.cpu_percent()

cihaz_model = computer_info.Model
kullanici_adi= computer_info.PrimaryOwnerName
cpu_adi = proc_info.Name
isletim_sistemi= os_info.Caption
ekran_karti_ismi= gpu_info.Name