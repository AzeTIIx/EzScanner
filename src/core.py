from platform import platform
from pystyle import *
from tqdm import trange
import nmap, sys, os, platform


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
    target = sys.argv[4]
    return begin, end, target

def scan(begin, end, target):
    o = []

    for i in trange(int(begin), int(end)+1):
        res = nmap.PortScanner().scan(target,str(i))
        res = res['scan'][target]['tcp'][i]['state']
        
        if res == "open":
            o.append(i)
            
    if len(o) < 1 :
        print(Colorate.Color(Colors.red,"Every port in the range are closed or filtered", True))
    else:
        for i in range(len(o)):
            print("Port {} is open" . format(o[i]))
    
    
        
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
        begin, end, target = params()
        scan(begin, end, target)

