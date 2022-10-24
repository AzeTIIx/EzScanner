from pystyle import *
from tqdm import trange
import socket, argparse, subprocess


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
            banner = r.recv(1024).decode()
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
        print ('[+] {}' .format(str(banner))) 
    return o


    
def rangescan(begin, end, ip2):
    for ping in range(begin,end):
        address = ip2 + str(ping)
        res = subprocess.call(['ping', '-c', '1', '-w', '1',  address], stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
        
        if res == 0:
            print(Colorate.Color(Colors.green,"{} is up" .format(address), True))
        elif res == 2:
            print("no response from", address)
        else:
            print(Colorate.Color(Colors.red,"ping to {} is closed" .format(address), True))    
    




def main():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    
    nmap = subparser.add_parser('nmap', help='Perform a NMAP scan on a target')
    hostup = subparser.add_parser('isup', help='List all up hosts on a range')

    nmap.add_argument('-b', type=int, help='First port to be scanned in the range')
    nmap.add_argument('-e', type=int, help='Last port to be scanned in the range')
    nmap.add_argument('-ip', help='IP to scan')
    

    hostup.add_argument('-b', type=int, help='First port to be scanned in the range')
    hostup.add_argument('-e', type=int, help='Last port to be scanned in the range')
    hostup.add_argument('-ip', help='IP to scan')


    args = parser.parse_args()
    
    

    if args.command == 'nmap':
        title()
        begin = args.b
        end =args.e
        ip = args.ip

        o = []
        o.append(scan(begin, end, ip))
        
        
    
    elif args.command == 'isup':
        title()
        begin = args.b
        end =args.e
        ip = args.ip
        net1 = ip.split('.')
        a='.'
        ip2 = net1[0] + a + net1[1] + a + net1[2] + a
        end = end + 1
        rangescan(begin, end, ip2)
        
 
        
