import socket
import platform
import getpass
import subprocess
import uuid
import csv
import os
import sys

def remove_func():
    exists = os.path.isfile(r'Resources\agent.txt')
    if exists:
        os.remove(r"Resources\agent.txt")

    exists = os.path.isfile(r'Resources\antivirus.txt')
    if exists:
        os.remove(r"Resources\antivirus.txt")

    exists = os.path.isfile(r'Resources\installed_programs.csv')
    if exists:
        os.remove(r"Resources\installed_programs.csv")

    exists = os.path.isfile(r'Resources\company_log.txt')
    if exists:
        os.remove(r"Resources\company_log.txt")

    exists = os.path.isfile(r'Resources\cpu_log.txt')
    if exists:
        os.remove(r"Resources\cpu_log.txt")

    exists = os.path.isfile(r'Resources\disk_log.txt')
    if exists:
        os.remove(r"Resources\disk_log.txt")

    exists = os.path.isfile(r'Resources\model_log.txt')
    if exists:
        os.remove(r"Resources\model_log.txt")

    exists = os.path.isfile(r'Resources\ram_log.txt')
    if exists:
        os.remove(r"Resources\ram_log.txt")


def device_func():
    global device_type
    device_type = input("Is this a Desktop (D); a Laptop (L); or a All-In-One (A): ")

    l = 0
    if device_type.upper() == "D":
        device_type = "Desktop"
        l = 1

    if device_type.upper() == "DESKTOP":
        device_type = "Desktop"
        l = 1

    if device_type.upper() == "L":
        device_type = "Laptop"
        l = 1

    if device_type.upper() == "Laptop":
        device_type = "Laptop"
        l = 1

    if device_type.upper() == "A":
        device_type = "All-In-One"
        l = 1

    if device_type.upper() == "All-In-One":
        device_type = "All-In-One"
        l = 1

    if device_type.upper() == "ALLINONE":
        device_type = "All-In-One"
        l = 1

    if device_type.upper() == "ALL IN ONE":
        device_type = "All-In-One"
        l = 1

    if l == 0:
        input("Invalid answer was given. Press Enter and restart program: ")
        sys.exit()

    return device_type



def location_func():
    global location
    location = input('What is the location of this computer?')

    return location


def room_func():
    global room
    room = input("What room is this computer in?")

    return room


def program_func():
    global program
    program = input("What program was this computer purchased in?")

    return program


def hostname_func():
    global hostname
    hostname = socket.gethostname()
    print(hostname)

    return hostname


def version_func():
    global version
    version = platform.version()
    version = version.split(".", 1)[0]
    version = "Win" + version + "Pro"
    if version == "Win6Pro":
        version = "Win7Pro"
    print(version)

    return version


def user_func():
    global user
    user = getpass.getuser()
    print(user)

    return user


def mac_func():
    global mac
    mac = hex(uuid.getnode())
    mac = str(mac)
    mac = mac[2:]
    mac = mac.upper()
    mac = ':'.join(a + b for a, b in zip(mac[::2], mac[1::2]))
    print(mac)

    return mac


def directory_func():
    global directory
    directory = os.getcwd()

    return directory


def bat_files_func(directory):
    with open(r'Resources\installed_programs.bat', "w") as wrt:
        wrt = wrt.write("Powershell.exe -executionpolicy remotesigned -File " + directory + "\Resources\installed_programs.ps1")

    subprocess.call(r'Resources\ram_log.bat')
    subprocess.call(r'Resources\cpu_log.bat')
    subprocess.call(r'Resources\disk_log.bat')
    subprocess.call(r'Resources\model_log.bat')
    subprocess.call(r'Resources\company_log.bat')
    subprocess.call(r'Resources\installed_programs.bat')
    subprocess.call(r'Resources\agent.bat')
    subprocess.call(r'Resources\antivirus.bat')


def cpu_func():
    global cpu_log
    with open(r"Resources\cpu_log.txt", "r", encoding="utf-16") as cpu_log:
        cpu_log = cpu_log.read()

    if str(cpu_log).__contains__("Core(TM) "):
        cpu_log = cpu_log.split("Core(TM) ", 1)[1]
        cpu_log = cpu_log.split(" CPU", 1)[0]
    else:
        cpu_log = cpu_log
        cpu_log = cpu_log.splitlines()
        cpu_log = cpu_log[1]

    print(cpu_log)

    return cpu_log


def ram_func():
    global ram_log
    with open(r"Resources\ram_log.txt", "r", encoding="utf-16") as ram_log:
        ram_log = ram_log.read()
        ram_log = ram_log.split('Capacity', 1)[1]
        RAMlength = ram_log.count('\n')
        RAMlength = RAMlength - 1
        if RAMlength == 1:
            print(str(RAMlength) + " Stick")
        else:
            print(str(RAMlength) + " Sticks")
        ram_log = ram_log.rstrip()
        ram_log = ram_log.replace(" ", "")
        ram_log = ram_log.splitlines()
        new_ram_log = 0
        i = 1
        while i != int(RAMlength) + 1:
            if ram_log[i].isdigit():
                new_ram_log = new_ram_log + int(ram_log[i])
                i += 1
            else:
                print("Blank Line")
                i += 1

        ram_log = new_ram_log / 1073741824
        ram_log = int(ram_log)
        ram_log = str(ram_log)
        ram_log = ram_log + "GB"
        print(ram_log)

        return ram_log


def disk_func(device_type):
    global disk_log
    with open(r"Resources\disk_log.txt", "r", encoding="utf-16") as disk_log:
        disk_log = disk_log.read()
        disk_log = disk_log.split('Size', 1)[1]
        length = disk_log.count('\n')
        length = length - 1
        if device_type == "Laptop":
            disk_log = disk_log.replace(" ", "")
            print(disk_log)
            disk_log = disk_log.splitlines()
            print("Laptop set to 1 Drive")
            new_disk_log = disk_log[1]
        else:
            if length == 1:
                print(str(length) + " Drive")
            else:
                print(str(length) + " Drives")
            disk_log = disk_log.replace(" ", "")
            print(disk_log)
            disk_log = disk_log.splitlines()
            new_disk_log = 0
            j = 1
            while j != int(length) + 1:
                if disk_log[j].isdigit():
                    new_disk_log = new_disk_log + int(disk_log[j])
                    print(int(disk_log[j]))
                    j += 1
                else:
                    print("Blank Line")
                    j = int(length) + 1
        disk_log = int(new_disk_log)
        disk_log = disk_log / 1073741824
        disk_log = int(disk_log)
        disk_log = str(disk_log)
        disk_log = disk_log + "GB"
        print(disk_log)

        return disk_log


def model_func():
    global model_log
    with open(r"Resources\model_log.txt", "r", encoding="utf-16") as model_log:
        model_log = model_log.read()

    model_log = model_log.split("\n", 1)[1]
    model_log = model_log.replace("\n", "")
    print(model_log)

    return model_log


def company_func(model_log):
    global company_log
    with open(r"Resources\company_log.txt", "r", encoding="utf-16") as company_log:
        company_log = company_log.read()

    company_log = company_log.split("\n", 1)[1]
    company_log = company_log.split(" ", 1)[0]
    company_log = company_log + " " + model_log
    company_log = company_log.replace("\n", "")
    print(company_log)

    return company_log


def antivirus_func():
    global antivirus
    with open(r"Resources\antivirus.txt", 'r', encoding='utf-16') as EAV:
        antivirus = str(EAV.readline())
        if antivirus != "":
            antivirus = antivirus[:5]
            print("ESET AGENT ANTIVIRUS: " + antivirus)

            return antivirus
        else:
            antivirus = input("ESET ANTIVIRUS NOT FOUND! ENTER version: ")

            return antivirus


def agent_func():
    global agent
    with open(r"Resources\agent.txt", 'r', encoding='utf-16') as EAT:
        agent = str(EAT.readline())
        if agent == "":
            agent = input("ESET AGENT NOT FOUND! ENTER version: ")

            return agent
        else:
            agent = agent[:5]
            print("ESET AGENT version: " + agent)

            return agent


def office_func():
    global office
    with open(r"Resources\installed_programs.csv", 'r') as f:
        csv_reader = csv.reader(f)
        your_list = list(csv_reader)
        print(str(len(your_list)) + " programs installed")
        t = 0
        p = 0
        while p == 0:
            if str(your_list[t]).__contains__("Microsoft office"):
                str1 = str(your_list[t])
                str1 = str1.split(",")
                print(str1)
                str1 = str(str1[0])
                str1 = str1.replace("'", "")
                str1 = str1.replace("[", "")
                print("MICROSOFT office FOUND. version: " + str1)
                p = 1
                office = str1

                return office
            else:
                t += 1
                if t == len(your_list) - 1:
                    p = 1
                    print("program NOT FOUND")
                    office = input("Please Input Microsoft office version: ")

                    return office


def finale_func(device_type, hostname, mac, location, version, program, room, user, model_log, company_log, cpu_log, ram_log, disk_log, agent, antivirus, office):

    row = [device_type, model_log, hostname, mac, " ", " ", " ", " ", " ", location, room, user, " ", " ", program,
           program, hostname, "themcc.lan", company_log, cpu_log, ram_log, disk_log, version, agent, antivirus,
           office, "Active", "AJ", " "]

    with open('Log.csv', 'a') as writeFile:
        writer = csv.writer(writeFile)
        writer = writer.writerow(row)

    return "Done"


try:
    remove_func()
except:
    print("Remove function was not executed")

try:
    device_func()
except Exception:
    print("Device function was not executed")

try:
    location_func()
except:
    print("Location function was not executed")

try:
    room_func()
except:
    print("Room function was not executed")

try:
    program_func()
except:
    print("Program function was not executed")

try:
    hostname_func()
except:
    print("Hostname function was not executed")

try:
    version_func()
except:
    print("Version function was not executed")

try:
    user_func()
except:
    print("User function was not executed")

try:
    mac_func()
except Exception:
    print("MAC function was not executed")

try:
    directory_func()
except:
    print("Directory function was not executed")

try:
    bat_files_func(directory)
except:
    print("Bat files function was not executed")

try:
    cpu_func()
except:
    print("CPU function was not executed")

try:
    ram_func()
except:
    print("RAM function was not executed")

try:
    disk_func(device_type)
except:
    print("Disk function was not executed")

try:
    model_func()
except:
    print("Model function was not executed")

try:
    company_func(model_log)
except Exception:
    print("Company function was not executed")

try:
    antivirus_func()
except:
    print("Antivirus function was not executed")

try:
    agent_func()
except:
    print("Agent function was not executed")

try:
    office_func()
except:
    print("Office function was not executed")

try:
    finale_func(device_type, hostname, mac, location, version, program, room, user, model_log, company_log, cpu_log, ram_log, disk_log, agent, antivirus, office)
except:
    print("Finale function was not executed")


input("Completed!")