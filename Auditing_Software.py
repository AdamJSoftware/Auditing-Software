import socket
import platform
import getpass
import subprocess
import uuid
import csv
import os
import sys

exists = os.path.isfile('Resources\ESETAGENT.txt')
if exists:
    os.remove("Resources\ESETAGENT.txt")

exists = os.path.isfile('Resources\ESETANTIVIRUS.txt')
if exists:
    os.remove("Resources\ESETANTIVIRUS.txt")

exists = os.path.isfile('Resources\InstalledPrograms.csv')
if exists:
    os.remove("Resources\InstalledPrograms.csv")

exists = os.path.isfile('Resources\CompanyLog.txt')
if exists:
    os.remove("Resources\CompanyLog.txt")

exists = os.path.isfile('Resources\CPULog.txt')
if exists:
    os.remove("Resources\CPULog.txt")

exists = os.path.isfile('Resources\DiskLog.txt')
if exists:
    os.remove("Resources\DiskLog.txt")

exists = os.path.isfile('Resources\ModelLog.txt')
if exists:
    os.remove("Resources\ModelLog.txt")

exists = os.path.isfile('Resources\RAMLog.txt')
if exists:
    os.remove("Resources\RAMLog.txt")

Device_Type = input("Is this a Desktop (D); a Laptop (L); or a All-In-One (A): ")

l = 0
if Device_Type.upper() == "D":
    Device_Type = "Desktop"
    l = 1

if Device_Type.upper() == "DESKTOP":
    Device_Type = "Desktop"
    l = 1

if Device_Type.upper() == "L":
    Device_Type = "Laptop"
    l = 1

if Device_Type.upper() == "Laptop":
    Device_Type = "Laptop"
    l = 1

if Device_Type.upper() == "A":
    Device_Type = "All-In-One"
    l = 1

if Device_Type.upper() == "All-In-One":
    Device_Type = "All-In-One"
    l = 1

if Device_Type.upper() == "ALLINONE":
    Device_Type = "All-In-One"
    l = 1

if Device_Type.upper() == "ALL IN ONE":
    Device_Type = "All-In-One"
    l = 1

if l == 0:
    input("Invalid answer was given. Press Enter and restart program: ")
    sys.exit()


Location = input('What is the location of this computer?')
Room = input("What room is this computer in?")
Program = input("What program was this computer purchased in?")

hostname = socket.gethostname()
print(hostname)

Version = platform.version()
Version = Version.split(".",1)[0]
Version = "Win" + Version + "Pro"
if Version == "Win6Pro":
    Version = "Win7Pro"
print(Version)

user = getpass.getuser()
print(user)

MAC = hex(uuid.getnode())
MAC = str(MAC)
MAC = MAC[2:]
MAC = MAC.upper()
MAC = ':'.join(a+b for a,b in zip(MAC[::2], MAC[1::2]))
print(MAC)

directory = os.getcwd()
print(directory)

with open('Resources\InstalledPrograms.bat', "w") as WRT:
    WRT = WRT.write("Powershell.exe -executionpolicy remotesigned -File " + directory +"\Resources\InstalledPrograms.ps1")

subprocess.call('Resources\\ram_log.bat')
subprocess.call('Resources\CPULog.bat')
subprocess.call('Resources\DiskLog.bat')
subprocess.call('Resources\ModelLog.bat')
subprocess.call('Resources\CompanyLog.bat')
subprocess.call('Resources\InstalledPrograms.bat')
subprocess.call('Resources\ESETAGENT.bat')
subprocess.call('Resources\ESETANTIVIRUS.bat')

with open("Resources\CPULog.txt", "r", encoding="utf-16") as CPULog:
    CPULog = CPULog.read()

if str(CPULog).__contains__("Core(TM) "):
    CPULog = CPULog.split("Core(TM) ", 1)[1]
    CPULog = CPULog.split(" CPU", 1)[0]
else:
    CPULog = CPULog
    CPULog = CPULog.splitlines()
    CPULog = CPULog[1]

print(CPULog)

with open("Resources\RAMLog.txt", "r", encoding="utf-16") as RAMLog:
    RAMLog = RAMLog.read()
    RAMLog = RAMLog.split('Capacity', 1)[1]
    RAMlength = RAMLog.count('\n')
    RAMlength = RAMlength - 1
    if RAMlength == 1:
        print(str(RAMlength) + " Stick")
    else:
        print(str(RAMlength) + " Sticks")
    RAMLog = RAMLog.rstrip()
    RAMLog = RAMLog.replace(" ", "")
    RAMLog = RAMLog.splitlines()
    NewRAMLog = 0
    i = 1
    while i != int(RAMlength) + 1:
        if RAMLog[i].isdigit():
            NewRAMLog = NewRAMLog + int(RAMLog[i])
            i += 1
        else:
            print("Blank Line")
            i += 1

    RAMLog = NewRAMLog / 1073741824
    RAMLog = int(RAMLog)
    RAMLog = str(RAMLog)
    RAMLog = RAMLog + "GB"
    print(RAMLog)

with open("Resources\DiskLog.txt", "r", encoding="utf-16") as DiskLog:
    DiskLog = DiskLog.read()
    DiskLog = DiskLog.split('Size', 1)[1]
    length = DiskLog.count('\n')
    length = length - 1
    if Device_Type == "Laptop":
        DiskLog = DiskLog.replace(" ", "")
        print(DiskLog)
        DiskLog = DiskLog.splitlines()
        print("Laptop set to 1 Drive")
        NewDiskLog = DiskLog[1]
    else:
        if length == 1:
            print(str(length) + " Drive")
        else:
            print(str(length) + " Drives")
        DiskLog = DiskLog.replace(" ", "")
        print(DiskLog)
        DiskLog = DiskLog.splitlines()
        NewDiskLog = 0
        j = 1
        while j != int(length) + 1:
            if DiskLog[j].isdigit():
                NewDiskLog = NewDiskLog + int(DiskLog[j])
                print(int(DiskLog[j]))
                j += 1
            else:
                print("Blank Line")
                j = int(length) + 1
    DiskLog = int(NewDiskLog)
    DiskLog = DiskLog / 1073741824
    DiskLog = int(DiskLog)
    DiskLog = str(DiskLog)
    DiskLog = DiskLog + "GB"
    print(DiskLog)

with open("Resources\ModelLog.txt", "r", encoding="utf-16") as ModelLog:
    ModelLog = ModelLog.read()

ModelLog = ModelLog.split("\n",1)[1]
ModelLog = ModelLog.replace("\n","")
print(ModelLog)

with open("Resources\CompanyLog.txt", "r", encoding="utf-16") as CompanyLog:
    CompanyLog = CompanyLog.read()

CompanyLog = CompanyLog.split("\n",1)[1]
CompanyLog = CompanyLog.split(" ",1)[0]
CompanyLog = CompanyLog + " " + ModelLog
CompanyLog = CompanyLog.replace("\n","")
print(CompanyLog)

with open("Resources\ESETANTIVIRUS.txt", 'r', encoding='utf-16') as EAV:
    ESETANTIVIRUS = str(EAV.readline())
    if ESETANTIVIRUS != "":
        ESETANTIVIRUS = ESETANTIVIRUS[:5]
        print("ESET AGENT ANTIVIRUS: " + ESETANTIVIRUS)
    else:
        ESETANTIVIRUS = input("ESET ANTIVIRUS NOT FOUND! ENTER VERSION: ")

with open("Resources\ESETAGENT.txt", 'r', encoding='utf-16') as EAT:
    ESETAGENT = str(EAT.readline())
    if ESETAGENT == "":
        ESETAGENT = input("ESET AGENT NOT FOUND! ENTER VERSION: ")
    else:
        ESETAGENT = ESETAGENT[:5]
        print("ESET AGENT VERSION: " + ESETAGENT)

with open("Resources\InstalledPrograms.csv", 'r') as f:
    csv_reader = csv.reader(f)
    your_list = list(csv_reader)
    print(str(len(your_list)) + " Programs installed")
    t = 0
    p = 0
    while p == 0:
        if str(your_list[t]).__contains__("Microsoft Office"):
            str1 = str(your_list[t])
            str1 = str1.split(",")
            print(str1)
            str1 = str(str1[0])
            str1 = str1.replace("'", "")
            str1 = str1.replace("[", "")
            print("MICROSOFT OFFICE FOUND. VERSION: " + str1)
            p = 1
            OFFICE = str1
        else:
            t += 1
            if t == len(your_list) - 1:
                p = 1
                print("PROGRAM NOT FOUND")
                input("Please Input Microsoft Office Version: ")
                OFFICE = "N/A"

row = [Device_Type, ModelLog, hostname, MAC, " ", " ", " ", " ", " ", Location, Room, user, " ", " ", Program, Program, hostname, "themcc.lan", CompanyLog, CPULog, RAMLog, DiskLog, Version, ESETAGENT, ESETANTIVIRUS, OFFICE, "Active", "AJ", " "]

with open('Log.csv', 'a') as writeFile:
    writer = csv.writer(writeFile)
    writer = writer.writerow(row)

input("Completed!")