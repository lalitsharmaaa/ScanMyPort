"""
Welcome to ScanMyPort by Lalit Sharma, a simple tool to look over commonly known OPEN ports across a target system. """

import socket
import sys
from datetime import datetime

COMMON_PORTS = {
    20: "FTP (data transfer)",
    21: "FTP (control)",
    22: "SSH (remote login)",
    23: "Telnet",
    25: "SMTP (email sending)",
    53: "DNS",
    80: "HTTP (web)",
    110: "POP3 (email)",
    139: "NetBIOS",
    143: "IMAP (email)",
    443: "HTTPS (secure web)",
    445: "SMB (file sharing)",
    993: "IMAPS",
    995: "POP3S",
    3306: "MySQL",
    3389: "RDP (remote desktop)",
    5432: "PostgreSQL",
    8080: "HTTP (alternate / dev servers)",
}


def scan_port(target_ip, port, timeout=0.5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((target_ip, port))
        # connect_ex returns 0 specifically when the connection succeeds
        return result == 0
    except socket.error:
        return False
    finally:
        sock.close()


def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        return None


def run_scan(target):
    ip = resolve_target(target)
    if ip is None:
        print(f"\nCouldn't resolve '{target}' — check the address and try again.\n")
        return

    print(f"\nScanning {target} ({ip})")
    print(f"Started at {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 50)

    open_ports = []
    for port, description in COMMON_PORTS.items():
        if scan_port(ip, port):
            open_ports.append((port, description))
            print(f"  [OPEN]   port {port:<6} {description}")

    print("-" * 50)
    if open_ports:
        print(f"Scan complete — {len(open_ports)} open port(s) found out of {len(COMMON_PORTS)} checked.\n")
    else:
        print(f"Scan complete — no open ports found out of {len(COMMON_PORTS)} checked.\n")


def main():
    if len(sys.argv) > 1:
        run_scan(sys.argv[1])
    else:
        print("Simple TCP port scanner. Type 'quit' to exit.")
        while True:
            target = input("\nEnter a target to scan (e.g. localhost, 127.0.0.1): ").strip()
            if target.lower() in ("quit", "exit", "q"):
                break
            if not target:
                continue
            run_scan(target)


if __name__ == "__main__":
    main()
