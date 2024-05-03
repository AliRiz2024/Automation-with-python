import os
from socket import *
os.system('cls')
port=[0,20,21,22,23,25,53,67,68,69,80,110,123,443,993,995]
ip=input("Enter ip address of victim : ")
print("Checking Connectivity First with the Victim : ",ip)
print("*"*50)
os.system("ping -n 3 {}".format(ip))
print("*"*50)
print("\nScanning port of : ",ip)
print("*"*50)
ns=socket()
for p in port:
    res=ns.connect_ex((ip,p))
    if res==0:
        print("Port",p,"is OPEN on",ip)
    else :
        print("port",p,"is CLOSE on",ip)

