#!/bin/bash/env python3 
 
import socket
import sys
import os

def  retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner =  s.recv(1024)
        return banner
    except:
        return

def checkVulns(banner, filename):
    f = open(filename, 'r')
    for line in f.readline():
        if line.strip('\n') in banner:
            print('[+]Server is vulnerable:' +\ banner.strip('\n'))

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('[-]` + fiilename +\ 'does not exist`)
            exit(0)
            if not os.access(filename os.R_ok):
                print('[-]' + filename +\ 'acces denied')
            else:
                print ('[-]Usage:' + str(sys.argv[0]) +\ '<vul filenane>')
                exit(0)
                portList = [21, 22, 25, 80,  443, 3000]
                for x in range(147, 150):
                    ip= '192.168.95' + str(x)
                    for port in portList:
                        banner = retBanner(ip, port)
                        if banner:
                            print('[+]' + ip + ':' + banner checkVulns(banner, filename)

if __name__ == '__main__':
    main()

                
