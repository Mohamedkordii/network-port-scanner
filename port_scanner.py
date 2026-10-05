import socket

def scan_ports(target, start_port, end_port):
print(f"\nScanning {target}...")
print("-" * 40)

open_ports = []

for port in range(start_port, end_port + 1):
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.5)

result = sock.connect_ex((target, port))

if result == 0:
print(f"Port {port}: OPEN")
open_ports.append(port)

sock.close()

print("-" * 40)

if open_ports:
print("Open ports:", open_ports)
else:
print("No open ports found.")


target = input("Enter target IP address: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

scan_ports(target, start_port, end_port)
