from pystyle import *
from tqdm import trange
import socket, argparse, subprocess

#Declaration of the banner
def title():
    banner = """ 
███████╗███████╗░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██╔════╝╚════██║██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗      █▓▒▓█▀██▀█▄░░▄█▀██▀█▓▒▓█
█████╗░░░░███╔═╝╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝      █▓▒░▀▄▄▄▄▄█░░█▄▄▄▄▄▀░▒▓█
██╔══╝░░██╔══╝░░░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗      █▓▓▒░░░░░▒▓░░▓▒░░░░░▒▓▓█
███████╗███████╗██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
╚══════╝╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝"""

    print(Center.XCenter(Colorate.Vertical(Colors.blue_to_purple, banner, 2)))



def scan(begin, end, ip):
    """
    It takes a range of ports and an IP address as arguments, and returns a list of open ports with the service and 
    the banner
    
    :param begin: The beginning port number to scan
    :param end: The last port to scan
    :param ip: The IP address of the target
    :return: a list of open ports.
    """
    o = []
    service = []
    banner = []

    for port in trange(int(begin), int(end)+1):
        try:
            r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            r.settimeout(0.2)
            r.connect((ip, port))
            service.append(socket.getservbyport(port))
            banner.append(grab(ip, port))
            r.settimeout(None)
            o.append(port)
            r.close() 
            
        except:
            pass


# Checking if the list of open ports is empty, and if it is, it prints a message saying that every
# port in the range is closed or filtered. If the list is not empty, it prints the open ports, the
# service running on the port, and the banner.
    if len(o) < 1 :
        print(Colorate.Color(Colors.red,"Every port in the range are closed or filtered", True))
    else:
        for i in range(len(o)):
            print(Colorate.Color(Colors.green,"[+] Port {} is open" . format(o[i]), True))
            print ('Service : {}' .format(str(service[i]))) 
            print ('{}' .format(str(banner[i]))) 
    return o


def grab(ip, port):
    """
    Try to connect to the IP address and port number specified, and if it works, return the banner,
    otherwise return the string 'Banner grab failed'.
    
    Now, let's use the function to grab the banner from a web server
    
    :param ip: The IP address of the target
    :param port: The port number to connect to
    :return: The banner of the service running on the port.
    """
    fail = "Banner grab failed"
    try:  
        s=socket.socket()  
        s.settimeout(2)
        s.connect((ip,port)) 
        banner = s.recv(100)  
        return banner 
    except:  
        return fail  
    

    
def rangescan(begin, end, ip2):
    """
    It takes a range of numbers, and pings each number in the range, and prints the result
    
    :param begin: the beginning of the range of IP addresses to scan
    :param end: the last IP address in the range
    :param ip2: The first three octets of the IP address
    """
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
    """
    This function is the main function of the program. It takes in the arguments from the command line
    and then calls the appropriate function based on the command given
    """
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    
    nmap = subparser.add_parser('nmap', help='Perform a NMAP scan on a target')
    hostup = subparser.add_parser('isup', help='List all up hosts on a range')

    nmap.add_argument('-b', type=int, help='First port to be scanned in the range')
    nmap.add_argument('-e', type=int, help='Last port to be scanned in the range')
    nmap.add_argument('-ip', help='IP to scan')
    

    hostup.add_argument('-b', type=int, help='First ip to be scanned in the range')
    hostup.add_argument('-e', type=int, help='Last ip to be scanned in the range')
    hostup.add_argument('-ip', help='IP to scan')


    args = parser.parse_args()
    
    

    if args.command == 'nmap':
        title()
        begin = args.b
        end =args.e
        ip = socket.gethostbyname(args.ip)

        o = []
        o.append(scan(begin, end, ip))
        
        
    
    elif args.command == 'isup':
        title()
        begin = args.b
        end =args.e
        ip = socket.gethostbyname(args.ip)
        net1 = ip.split('.')
        a='.'
        ip2 = net1[0] + a + net1[1] + a + net1[2] + a
        end = end + 1
        rangescan(begin, end, ip2)
        
