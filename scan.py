#!/usr/bin/env python3

import socket
import sys
import os


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner.decode()
    except:
        return None


def checkVulns(banner, filename):
    with open(filename, 'r') as f:
        for line in f:
            if line.strip('\n') in banner:
                print('[+] Server is vulnerable: ' + banner.strip('\n'))


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print('[-] File ' + filename + ' does not exist')
            exit(0)
        if not os.access(filename, os.R_OK):
            print('[-] Access denied for file: ' + filename)
        else:
            print('[-] Usage: ' + str(sys.argv[0]) + ' <vul filename>')
            exit(0)
    else:
        portList = [21, 22, 25, 80, 443, 3000]
        for x in range(147, 150):
            ip = '192.168.95.' + str(x)
            for port in portList:
                banner = retBanner(ip, port)
                if banner:
                    print('[+] ' + ip + ':' + str(port) + ' - ' + banner.strip('\n'))
                    checkVulns(banner, filename)


if __name__ == '__main__':
    main()

