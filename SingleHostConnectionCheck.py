import os
os.system('cls')
ip=input("Enter Ip Address to check connectivity : ")
print("Checking connectivity with : ",ip)
print("*"*50)
os.system("ping -n 3 {}".format(ip))
print("*"*50)

