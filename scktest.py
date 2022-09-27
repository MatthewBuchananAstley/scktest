#!/usr/bin/python3
#
# 2022 Matthew Buchanan Astley

import os,sys
import socket,time
import subprocess

a2 = [] 

url = sys.argv[1]

def print_mijndate():
    from time import gmtime,strftime
    date = strftime("%Y%m%d.%H%M%S")
    return(date)

def rprt():
    a =open("connection_t." + print_mijndate(), "w")
    return(a)

def popup(msg):
    #
    # desktop notification
    output=subprocess.check_output("/usr/bin/notify-send " + '-i scktest ' + "'" + str(msg) + "'", shell=True, stderr=-3)
    a = output.decode().strip(' \n')
    print(a)

cnt = 0

while True:
    cnt += 1
    a = socket.getaddrinfo(url, 80, proto=socket.IPPROTO_TCP)
    a1 = a[0][4][0]
    a2.append(a1)
    print(cnt,print_mijndate(), a2[0])

    if a1 != a2[0]:
        a3 = print_mijndate() + " IP CHANGE " + url + " " + a2[0] + a1 + "\n"
        print("JA",a3)
        #
        # for desktop notification when an IP changes
        popup(a3)

        a4 = rprt()
        a4.write(a3)
        a4.close()
        a2[0] = a1

    time.sleep(0.5)

