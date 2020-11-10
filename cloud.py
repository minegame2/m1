from colorama import init, AnsiToWin32, Fore, Back, Style
import socket
import sys
import os
import time
# os.system('cls' or 'clear') 
stream = AnsiToWin32(sys.stderr).stream


def __start__():
    print(Fore.CYAN+"""
             ___    
__      _____| | ___ ___  _ __ ___   _____
\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _  /
 \ V  V /  __/ | (_| (_) | | | | | |  __/
  \_/\_/ \___|_|\___\___/|_| |_| |_|\___|""", file = stream)
    subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']

    site = input("url >>")
    if site == "":
        try:
            print(Fore.RED+" [!] "+Fore.BLUE+"Please Enter Address :) \n")
            time.sleep(1.5)
            sys.exit()
        except:
            return
    for sub in subdom:
        try:
            hosts = str(sub) + "." + str(site)
            bypass = socket.gethostbyname(str(hosts))
            #print('Cloudflare Bypassed ! Real IP Address => '+bypass)
            print (" [!] CloudFlare Bypass " + str(bypass) + ' | ' + str(hosts))
        except Exception:
            pass
    try:
        input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()
__start__()

#TopLearn.com