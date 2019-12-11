import socket
'''
Created on Oct 22, 2019
@author: Aparna Ganesh
'''

try:
    fp = open('addresses.txt')
    count = len(open('addresses.txt').readlines(  ))
    fp2 = open('output.txt', 'w')
    for i in range(count):
        line = fp.readline()
        strip_line = line.strip()
        IPaddress = socket.gethostbyname(strip_line)
        fp2.write(strip_line)
        fp2.write("  ->")
        fp2.write(IPaddress)
        fp2.write("\n")
finally:
    fp.close()
    fp2.close()


