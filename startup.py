#!/usr/bin/python
import subprocess

with open("/boot/ipaddress.txt", 'rb') as fo:
    ip = fo.read().strip('\n')

subprocess.Popen(['/sbin/ifconfig', 'eth0', ip, 'netmask', '255.255.255.0'], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()

while True:
    if ip == '192.168.0.1':
        subprocess.Popen(['/boot/beocat/fractal-store.py',], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()
    else:
        subprocess.Popen(['/boot/beocat/fractal-generate.py',], stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()
