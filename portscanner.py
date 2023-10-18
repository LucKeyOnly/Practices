import socket

def scan(targets, ports):
    print('\n' + ' Starting Scanning ' + str(targets))
    for port in range(1, ports + 1):
        scan_port(targets, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Menetapkan timeout koneksi
        result = sock.connect_ex((ipaddress, port))

        if result == 0:
            print(f"[+] Port {port} is Open")
        sock.close()
    except socket.error:
        pass

targets = input("[*] Enter Targets To Scan (split them by (,)): ")
ports = int(input("[*] Enter How Many Ports To Scan: "))

if ',' in targets:
    print("[*] Scanning multiple targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(), ports)
else:
    scan(targets, ports)
