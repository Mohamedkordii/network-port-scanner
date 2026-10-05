# Network Port Scanner

A simple Python-based TCP port scanner designed to identify open ports on an authorized host within a specified port range.

## Features

- Scans a user-defined range of TCP ports
- Identifies open ports
- Uses Python's built-in `socket` module
- Allows the user to specify the target IP address
- Displays discovered open ports
- Uses connection timeouts to avoid long delays

## How It Works

The program creates a TCP socket for each port in the selected range and attempts to connect to the target host.

It uses `connect_ex()` to determine whether the connection was successful.

- Result `0` means the port is open
- Other results indicate that a connection could not be established

Open ports are stored and displayed after the scan is completed.

## How to Run

Make sure Python 3 is installed.

Run:

```bash
python3 port_scanner.py
```

The program will ask for:

1. Target IP address
2. Starting port
3. Ending port

Example:

```text
Enter target IP address: 127.0.0.1
Enter starting port: 20
Enter ending port: 100

Scanning 127.0.0.1...
----------------------------------------
Port 80: OPEN
----------------------------------------
Open ports: [80]
```

## Technologies Used

- Python 3
- Socket Programming
- TCP/IP Networking

## What I Learned

Through this project, I practiced:

- Basic TCP/IP networking concepts
- Python socket programming
- Understanding ports and network services
- Using connection timeouts
- Writing a simple cybersecurity-related network utility

## Ethical Use

This project is intended for educational purposes and authorized security testing only. Only scan systems and networks that you own or have explicit permission to test.

## Author

Mohamed Kordi
Cybersecurity Engineering Student
University of Sharjah
