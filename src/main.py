from pystyle import *
import nmap, sys

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
    begin = sys.argv[1]
    end = sys.argv[2]
    target = sys.argv[3]
    return begin, end, target

def scan(begin, end, target):
    scanner = nmap.PortScanner()

    for i in range (int(begin), int(end)+1):
        res = scanner.scan(target,str(i))
        res = res['scan'][target]['tcp'][i]['state']
        print(f'port {i} is {res}.')
    

if __name__ =='__main__':
    n = len(sys.argv)
    
    if(sys.argv[1] == "--help"):
        print("Usage : \n")
        print("     main.py [first port] [last port] [target ip]\n")
        
    elif (n < 3):
        print("Error, synthax is main.py  [first port] [last port] [target]")
        
    else:
        title()
        begin, end, target = params()
        scan(begin, end, target)

