from socket import *
import os
os.system('cls')
port=[1,2,3]
ip=input("enter ip address : ")
os.system("ping -n 6 {}".format(ip))
ns=socket()
for p in port:
    res=ns.connect_ex((ip,p))
    if res==0:
        print("port",p,"open on",ip)
    else:
        print("port",p,"close on",ip)
