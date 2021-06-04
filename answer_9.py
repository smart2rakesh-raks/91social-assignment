import sys
import os
import platform
import subprocess

File = open("E:/assigment/91social/file.txt", "r")
lines = File.readlines()
for ip in lines:
    ip = ip.strip( )
    ping=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
        stdout=File, stderr=File).wait()
    if ping:
        print(ip," inactive")
    else:
        print(ip," active")
  

Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a = str(Data)
  
# try block
try:
    
    # arrange the string
    for i in range(len(a)):
        print(a.split("\\r\\r\\n")[6:][i])
  
except IndexError as e:
    print("All Done")
