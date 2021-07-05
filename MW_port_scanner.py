import argparse, socket, threading, nmap

'''
In any form of attack, phsyical or digital, the first step is reconaissance. Find the vulnerabilities.

The following program is a recon script that can perform 2 scans one for open TCP ports and another broader scan over ACK, RST, FIN, or SYN-ACK.
'''

# portscan takes hostname and ports as params
# attempts to resolve IP and open ports
# returns IP address and attempts to connect each individual port using connscan

def port_scan(tgt_host, tgt_ports):
    
    # get the ip of given domain
    try:
        tgt_ip = socket.gethostbyname(tgt_host)
    except socket.herror:
        print(f'[-] Cannot Resolve {tgt_host}: Unknown Host')
        return

    # get host name from ip
    #   gethostbyaddr returns tuple (host name, IP aliases, host ip address)
    try:
        tgt_name = socket.gethostbyaddr(tgt_ip)
        print(f'\n[+] Scan results for: {tgt_name[0]}')
    except socket.herror:
        print(f'\n[-] Scan results for: {tgt_ip}')

    # complete the scan before continuing
    socket.setdefaulttimeout(1)

    # scanning many hosts/ports would take a long time
    # threading used to simultaneously scan
    #   thread takes function and arguments as params
    for port in tgt_ports:
        thread = threading.Thread(target=conn_scan, args=(tgt_host, int(port)))
        thread.start()


# connscan takes tgthost and tgtport as params
# attempts to connect to target host and por
# return open port message if succesful, closed message if failure

def conn_scan(tgt_host, tgt_port):
    
    # threading samaphore lock used to keep console output linear
    # screen lock aquires the semaphore lock space 
    # it will only print the next port scan result once the previous grab has been released
    screen_lock = threading.Semaphore()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn_skt:
        try:
            conn_skt.connect((tgt_host, tgt_port))
            conn_skt.send(b'response packet\r\n')
            results = conn_skt.recv(100).decode('utf-8')
            screen_lock.acquire()
            print(f'[+] {tgt_port}/tcp open\n\t[>] {results}')
        except OSError:
            screen_lock.acquire()
            print(f'[-] {tgt_port}/tcp closed')
        finally:
            screen_lock.release()


# nmap scan basically does the same as above but has more flexibility in the ports it can scan, however we will still use it for simple TCP scan 

def nmap_scan(tgt_host, tgt_ports):

    nm = nmap.PortScanner()
    for port in tgt_ports:

        nm.scan(tgt_host, port)
        state = nm[tgt_host]['tcp'][int(port)]['state']
        print(f'[+] {tgt_host} tcp/{port} {state}')


# MAIN FUNCTION WILL BE REMOVED ONCE ALL FILES ARE COMPLETE AND INTEGRATED
# main function users argparser to construct valid arguments in the command line

if __name__ == '__main__':

    parser = argparse.ArgumentParser(usage='[+] Usage: MW_port_scanner.py TARGET_HOST -p TARGET_PORTS\n  [>] Example: python3 MW_port_scanner.py scan.me.org -p 23,24,80')

    parser.add_argument('tgt_host', type=str, metavar='TARGET_HOST', help='specify target host (IP or domain name)')
    parser.add_argument('-p', required=True, type=str, metavar='TAREGT_PORTS', help='specify target port(s), comma separated and no spaces')

    args = parser.parse_args()
    args.tgt_ports = str(args.p).split(',')
    
    port_scan(args.tgt_host, args.tgt_ports)
    nmap_scan(args.tgt_host, args.tgt_ports)