#! /usr/bin/python3

from socket import *
import sys, time
from datetime import datetime
from threading import *

print(r"""
     _________________________________________________________________________________________________________________________
    +                                            Author:- Techwebspot (Jeet)                                                  +
    |-------------------------------------------------------------------------------------------------------------------------|
    +-------------------------------------------------------------------------------------------------------------------------+
    |                         Credit:- Violent python book, null bytes, hackingvision and furas.pl                            |
    +_________________________________________________________________________________________________________________________+
    |                                 __  __                        _                                                         |
    |                                |  \/  | __ _ _ __   __ _  ___| | ___   _  ___  _                                        |
    |                                | |\/| |/ _` | '_ \ / _` |/ _ \ |/ / | | |/ _ \| | | |                                   |
    |                                | |  | | (_| | | | | (_| |  __/   <| |_| | (_) | |_| |                                   |
    |                                |_|  |_|\__,_|_| |_|\__, |\___|_|\_\\__, |\___/ \__,_|                                   |
    |                                                     |___/           |___/                                               |
    |                                        ____                                                                             |
    |                                       / ___|  ___ __ _ _ __  _ __   ___ _ __                                            |
    |                                       \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|                                           |
    |                                        ___) | (_| (_| | | | | | | |  __/ |                                              |
    |                                       |____/ \___\__,_|_| |_|_| |_|\___|_|                                              |
    +_________________________________________________________________________________________________________________________+
    """)

while True:
    try:
        select = str(input("\nWhich type of scan you want: \n 1. Simple Port Scan \n 2. Ultimate Mode: Port Scan + Banner Grabbing (Normal Speed Scan) [Recommended] \n 3. Advanced Mode: Port Scan + Banner Grabbing (Fast speed Scan)   [Not Recommended] \n Enter Index Number:- "))
        
        if "1" in select:
            break
        elif "2" in select:
            break
        elif "3" in select:
            break
        else:
            print("\n[-]Wrong Index Number select. Try again...")
    except KeyboardInterrupt:
        print("\n\n[*] User Requested An Interrupt")
        print("[*] Apllication Shutting Down")
        sys.exit(1)

if select == "1":
    try:
        host = str(input("\n[*] Enter Target Host Address: "))
    except KeyboardInterrupt:
        print("\n\n[*] User Requested An Interrupt")
        print("[*] Apllication Shutting Down")
        sys.exit(1)

    while True:
        try:
            ports = input("\n[*] Enter Target Ports \n For scanning all ports press 'Enter' otherwise write target Ports which you like to scan \n example: 21, 80 \n >:")
            if not ports.strip():
                break
            try:
                s = ports.replace(",", "")
                m = s.replace(" ", "")
                l = int(m)
                if type(l) == int:
                    break
                else:
                    print("[-] Something unknown thing written")    
            except:
                print("[-] Something unknown thing written")
        except KeyboardInterrupt:
            print("\n\n[*] User Requested An Interrupt")
            print("[*] Apllication Shutting Down")
            sys.exit(1)
        
    def connScan(host, port):
        try:
            connSkt = socket(AF_INET, SOCK_STREAM)
            connSkt.connect((host, port))
            print("[+] Tcp Port %d: open" % port)
            connSkt.close()
        except:
            pass

    def portScan(host):
        try:
            tgtIP = gethostbyname(host)
            tgtName = gethostbyaddr(tgtIP)
            print("\n[*] Scan Results for: " + tgtName[0])
            print("[*] Scan Results for: " + tgtIP)
        except:
            print("[-] Cannot resolve '%s': Unknown host" % host)
            return

        print("\n[*] Scanning started: %s\n" % time.strftime("%H:%M:%S"))
        start_time = datetime.now()

        setdefaulttimeout(1)
    
        print("Ports are scanning please wait...")
    
        if ports == "":
            for port in range(1, 5001):
                connScan(host, int(port))
        else:
            for port in ports.split(","):
                try:
                    connSkt = socket(AF_INET, SOCK_STREAM)
                    connSkt.connect((host, int(port)))
                    print("[+] Tcp Port %s: open" % port)
                    connSkt.close()
                except:
                    print("[+] Tcp Port %s: closed" % port)
        
        stop_time = datetime.now()
        total_time_duration = stop_time - start_time
        print("\n[*] Scanning Finished: %s" % time.strftime("%H:%M:%S"))
        print("[*] Scanned Duration: %s" % total_time_duration) 
    
    portScan(host)

if select == "2":
    try:
        host = str(input("\n[*] Enter Target Host Address: "))
    except KeyboardInterrupt:
        print("\n\n[*] User Requested An Interrupt")
        print("[*] Apllication Shutting Down")
        sys.exit(1)

    while True:
        try:
            ports = input("\n[*] Enter Target Ports \n For scanning all ports press 'Enter' otherwise write target Ports which you like to scan \n example: 21, 80 \n >:")
            if not ports.strip():
                break
            try:
                s = ports.replace(",", "")
                m = s.replace(" ", "")
                l = int(m)
                if type(l) == int:
                    break
                else:
                    print("[-] Something unknown thing written")    
            except:
                print("[-] Something unknown thing written")
        except KeyboardInterrupt:
            print("\n\n[*] User Requested An Interrupt")
            print("[*] Apllication Shutting Down")
            sys.exit(1)

    def connScan(host, port):
        try:
            connSkt = socket(AF_INET, SOCK_STREAM)
            connSkt.connect((host, port))
            connSkt.send(str.encode('Data\r\n'))
            results = connSkt.recv(100)
            print("\n[+] Tcp Port %d: open" % port)
            print(results.decode('utf-8'))
            connSkt.close()
        except:
            pass

    def portScan(host):
        try:
            tgtIP = gethostbyname(host)
            tgtName = gethostbyaddr(tgtIP)
            print("\n[*] Scan Results for: " + tgtName[0])
            print("[*] Scan Results for: " + tgtIP)
        except:
            print("[-] Cannot resolve '%s': Unknown host" % host)
            return

        print("\n[*] Scanning started: %s\n" % time.strftime("%H:%M:%S"))
        start_time = datetime.now()

        setdefaulttimeout(1)
    
        print("Ports are scanning please wait...")
    
        if ports == "":
            for port in range(1, 5001):
                connScan(host, int(port))
        else:
            for port in ports.split(","):
                try:
                    connSkt = socket(AF_INET, SOCK_STREAM)
                    connSkt.connect((host, int(port)))
                    connSkt.send(str.encode('Data\r\n'))
                    results = connSkt.recv(100)
                    print("\n[+] Tcp Port %s: open" % port)
                    print(results.decode('utf-8'))
                    connSkt.close()
                except:
                    print("[+] Tcp Port %s: closed" % port + "\n")
        
        stop_time = datetime.now()
        total_time_duration = stop_time - start_time
        print("\n[*] Scanning Finished: %s" % time.strftime("%H:%M:%S"))
        print("[*] Scanned Duration: %s" % total_time_duration) 
    
    portScan(host)

if select == "3":
    print("\nNote:- If you hit with 'Timed out' Error means server blocks your ip because of using Advanced mode then use Ultimate mode ")
    
    screenLock = Semaphore(value=1)

    try:
        host = str(input("\n[*] Enter Target Host Address: "))
    except KeyboardInterrupt:
        print("\n\n[*] User Requested An Interrupt")
        print("[*] Apllication Shutting Down")
        sys.exit(1)

    while True:
        try:
            ports = input("\n[*] Enter Target Ports \n For scanning all ports press 'Enter' otherwise write target Ports which you like to scan \n example: 21, 80 \n >:")
            if not ports.strip():
                break
            try:
                s = ports.replace(",", "")
                m = s.replace(" ", "")
                l = int(m)
                if type(l) == int:
                    break
                else:
                    print("[-] Something unknown thing written")    
            except:
                print("[-] Something unknown thing written")
        except KeyboardInterrupt:
            print("\n\n[*] User Requested An Interrupt")
            print("[*] Apllication Shutting Down")
            sys.exit(1)

    def connScan(host, start_port, end_port):
        for port in range(start_port, end_port):
            try:
                connSkt = socket(AF_INET, SOCK_STREAM)
                connSkt.connect((host, port))
                connSkt.send(str.encode('Data\r\n'))
                results = connSkt.recv(100)
                screenLock.acquire()
                print("\n[+] Tcp Port %d: open" % port)
                print(results.decode('utf-8'))
            except Exception as ex:
                print(ex)
                screenLock.acquire()
            finally:
                screenLock.release()
                connSkt.close()

    def portScan(host):
        try:
            tgtIP = gethostbyname(host)
            tgtName = gethostbyaddr(tgtIP)
            print("\n[*] Scan Results for: " + tgtName[0])
            print("[*] Scan Results for: " + tgtIP)
        except:
            print("[-] Cannot resolve '%s': Unknown host" % host)
            return

        print("\n[*] Scanning started: %s\n" % time.strftime("%H:%M:%S"))
        start_time = datetime.now()

        setdefaulttimeout(1)
    
        print("Ports are scanning please wait...")
    
        if ports == "":
            step = 500
            for start_port in range(1, 5001, step):
                end_port = start_port + step
                t = Thread(target=connScan, args=(host, int(start_port), int(end_port)))
                t.start()
        else:
            for port in ports.split(","):
                try:
                    connSkt = socket(AF_INET, SOCK_STREAM)
                    connSkt.connect((host, int(port)))
                    connSkt.send(str.encode('Data\r\n'))
                    results = connSkt.recv(100)
                    screenLock.acquire()
                    print("\n[+] Tcp Port %s: open" % port)
                    print(results.decode('utf-8'))
                except:
                    screenLock.acquire()
                    print("[+] Tcp Port %s: closed" % port + "\n")
                finally:
                    screenLock.release()
                    connSkt.close()
        
        stop_time = datetime.now()
        total_time_duration = stop_time - start_time
        print("\n[*] Scanning Finished: %s" % time.strftime("%H:%M:%S"))
        print("[*] Scanned Duration: %s" % total_time_duration) 
    
    portScan(host)
