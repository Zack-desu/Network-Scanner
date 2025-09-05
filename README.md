# 

### Network Scanner

A lightweight Python tool designed to scan local networks and identify active devices using ICMP ping protocols. Developed as a practical application of network security fundamentals.

## 

#### Features

* IP Range Scanning: Automatically scans a specified range of IP addresses.
* Device Discovery: Identifies active devices responding to ICMP requests.
* Cross-Platform: Works on Windows, macOS, and Linux systems.
* Simple CLI Interface: Easy to use with immediate results.

## 

### Usage

##### Basic Installation

1. Clone this repository:
   git clone https://github.com/Zack-desu/Network-Scanner-.git
3. Navigate to the project directory:

cd network-scanner

1. Run the scanner (default settings):

python network\_scanner.py
Advanced Usage

Modify the target network range in the script:

network = "192.168.0"  # Change to your network segment
  

**Requirements**

· Python 3.6+
· Network connectivity
· Administrator privileges (for some systems)

&nbsp; Technical Details



**This implementation uses:**

· ICMP Ping Protocol for device discovery
· Subnet scanning (/24 range)
· Cross-platform compatibility through Python's os and platform modules

&nbsp; Notes

·   Firewall settings may affect detection accuracy
·   Scanning 254 addresses takes approximately 2-5 minutes
· Results may vary based on network configuration and device responses

&nbsp; Project Purpose





**This project demonstrates:**

· Practical application of network programming concepts
· Understanding of fundamental cybersecurity reconnaissance techniques
· Python development skills for network utilities

&nbsp; License

MIT License - feel free to use and modify for educational purposes.





