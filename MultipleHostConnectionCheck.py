import os
os.system('cls')
file=open("c:\\users\\rizwan\\desktop\\clients.txt","r")
allip=file.read()
print(allip)
alladd=allip.splitlines()
for ip in alladd:
    print("Checking connectivity with : ",ip)
    print("*"*50)
    os.system("ping -n 3 {}".format(ip))
    print("*"*50)
'''
print("Checking connectivity with : ",ip)
print("*"*50)
os.system("ping -n 3 {}".format(ip))
print("*"*50)'''
