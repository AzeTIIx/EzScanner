from platform import platform
from pystyle import *
from tqdm import trange
import socket, sys, os, platform, argparse


def title():
    banner = """
    ██████╗░██╗░░░██╗██████╗░███████╗███╗░░██╗████████╗███████╗░██████╗████████╗───▄█▌─▄─▄─▐█▄
    ██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝████╗░██║╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝───██▌▀▀▄▀▀▐██
    ██████╔╝░╚████╔╝░██████╔╝█████╗░░██╔██╗██║░░░██║░░░█████╗░░╚█████╗░░░░██║░░░───██▌─▄▄▄─▐██
    ██╔═══╝░░░╚██╔╝░░██╔═══╝░██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░░╚═══██╗░░░██║░░░───▀██▌▐█▌▐██▀
    ██║░░░░░░░░██║░░░██║░░░░░███████╗██║░╚███║░░░██║░░░███████╗██████╔╝░░░██║░░░▄██████─▀─██████▄
    ╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░░░░╚═╝░░░"""

    print(Center.XCenter(Colorate.Vertical(Colors.blue_to_purple, banner, 2)))



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
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    
    nmap = subparser.add_parser('nmap')
    hostup = subparser.add_parser('isup')

    nmap.add_argument('-b', type=int)
    nmap.add_argument('-e', type=int)
    nmap.add_argument('-target')
    
    hostup.add_argument('-ip')

    args = parser.parse_args()

    if args.command == 'nmap':
        title()
        begin = args.b
        end =args.e
        ip = args.target
        scan(begin, end, ip)
        
    elif args.command == 'isup':
        title()
        ip = args.ip
        isup(ip)
    
        
