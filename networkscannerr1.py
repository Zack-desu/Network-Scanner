import os
import platform

def ping_host(ip):
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    command = f"ping {param} {ip}"
    response = os.system(command)
    return response == 0 and "unreachable" not in os.popen(command).read()

def scan_network(ip_range):
    active_hosts = []
    for i in range(1, 255):
        target_ip = f"{ip_range}.{i}"
        if ping_host(target_ip):
            active_hosts.append(target_ip)
            print(f"[+] {target_ip} is online")
    return active_hosts

if __name__ == "__main__":
    network = "192.168.0"
    print(f"Scanning {network}.0/24...")
    active_devices = scan_network(network)
    print(f"\nFound {len(active_devices)} active devices.")
