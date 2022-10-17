from platform import platform
from pystyle import *
from tqdm import trange
import socket, sys, os, platform


def title():
    banner = """
    ██████╗░██╗░░░██╗██████╗░███████╗███╗░░██╗████████╗███████╗░██████╗████████╗───▄█▌─▄─▄─▐█▄
    ██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝───██▌▀▀▄▀▀▐██
    ██████╔╝░╚████╔╝░██████╔╝█████╗░░██╔██╗██║░░░██║░░░█████╗░░╚█████╗░░░░██║░░░───██▌─▄▄▄─▐██
    ██╔═══╝░░░╚██╔╝░░██╔═══╝░██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░───▀██▌▐█▌▐██▀
    ██║░░░░░░░░██║░░░██║░░░░░███████╗██║░╚███║░░░██║░░░███████╗██████╔╝░░░██║░░░▄██████─▀─██████▄
    ╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░"""

    print(Center.XCenter(Colorate.Vertical(Colors.blue_to_purple, banner, 2)))


def params():
    begin = sys.argv[2]
    end = sys.argv[3]
    ip = sys.argv[4]
    return begin, end, ip

def scan(begin, end, ip):
    o = []

    for port in trange(int(begin), int(end)+1):
        try:
            r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            r.settimeout(0.2)
            r.connect((ip, port))
            r.settimeout(None)
            r.close()
            o.append(port)
        except:
            pass


    if len(o) < 1 :
        print(Colorate.Color(Colors.red,"Every port in the range are closed or filtered", True))
    else:
        for i in range(len(o)):
            print(Colorate.Color(Colors.green,"Port {} is open" . format(o[i]), True))

def isup(host):
    os_system = platform.system()
    if(os_system=="Linux"):
        cmd = str("ping -c 4 " + host)
        os.system(cmd)
    else:
        cmd = str("ping " + host)
        os.system(cmd)

def main():
    n = len(sys.argv)

    if(sys.argv[1] == "--help"):
        title()
        print("Usage : \n")
        print("nmap port scan : \n")
        print("     PyPentest --nmap [first port] [last port] [target ip]\n")
        print("check if host is up : \n")
        print("     PyPentest --isup [target ip]\n")
    elif (sys.argv[1] == "--isup"):
        title()
        host = sys.argv[2]
        isup(host)

    elif (n < 3):
        error = "Error, synthax is main.py [first port] [last port] [target]"
        print(Colorate.Color(Colors.red, error, True))

    elif(sys.argv[1] == '--nmap'):
        title()
        begin, end, ip = params()
        scan(begin, end, ip)

