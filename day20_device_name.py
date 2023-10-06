'''
Day 20 of '30 days of 30
 Programs challenege '''
 
'''
Find and Print
Hostname or Device Name
'''
import socket

name = socket.gethostname()
ip = socket.gethostbyname(name)
print(f"Device Ip address: {ip}")