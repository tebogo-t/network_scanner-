#!/usr/bin/env python3

import socket
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
                print('[+] Server is vulnerable: ' + banner)


def main():
    filename = input("Enter the vulnerability filename: ")

    if not os.path.isfile(filename):
        print('[-] File ' + filename + ' does not exist')
        exit(1)

    if not os.access(filename, os.R_OK):
        print('[-] Access denied for file: ' + filename)
        exit(1)

    portList = [21, 22, 25, 80, 443, 3000]
    ip_range = input("Enter the IP range (e.g., 192.168.0.1-10): ")

    start_ip, end_ip = ip_range.split('-')
    start_ip_parts = start_ip.split('.')
    end_ip_parts = end_ip.split('.')

    for i in range(int(start_ip_parts[3]), int(end_ip_parts[3]) + 1):
        ip = f"{start_ip_parts[0]}.{start_ip_parts[1]}.{start_ip_parts[2]}.{i}"
        for port in portList:
            banner = retBanner(ip, port)
            if banner:
                print(f'[+] {ip}:{port} - Checking vulnerabilities...')
                checkVulns(banner, filename)


if __name__ == '__main__':
    main()

