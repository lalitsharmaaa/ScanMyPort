# ScanMyPort
ScanMyPort is a simple Python Tool designed to look for OPEN common network ports on a target machine. 

# What it actually does?
For a given target (it can be even your own machine, or anything you have permission to test on), it checks out for the 18 well-known ports like the SSH(22),HTTP(80) ,HTTPS(443) ,MySQL(3306) and tell us which of them are OPEN. <br>
A port is OPEN when we have someone as a reciever on the other end. It doesn't try to guess but in fact, it actually tries to connect to each port in the same way our browser does to connect to a particular service or network over the internet. 

# Why only 18 ports, and not all 65535?
Connecting and Scanning every port, one at a time would take hours and mostly return nothing useful. The 18 ports scanned here are the well-known ports assigned to real, common services so that the scan stays fast and results in something meaningful, instead of a large number of closed doors. 

# How to run it?
Download the .py file and open it in your desired terminal through this code:
```bash
python3 port_scanner.py
```
But this is not the full needed code. You will have to mention the IP of the target device. We mostly use the IP Address 127.0.0.1 ( localhost ) which helps us to scan our own machine. <br>
New Code:
```bash
python3 port_scanner.py 127.0.0.1
```
or 
```bash
python3 port_scanner.py localhost
```
# What will it detect?
Mostly ( not always ) it will return with closed ports.
```bash
Scanning 192.168.1.20 (192.168.1.20)
Started at 14:33:41
--------------------------------------------------
--------------------------------------------------
Scan complete — no open ports found out of 18 checked.
```
But you can run a temporary test server in a different terminal tab using the code:
```bash
python3 -m http.server 8080
```
The Output then appears as:
```bash
Scanning 192.168.1.10 (192.168.1.10)
Started at 14:36:52
--------------------------------------------------
  [OPEN]   port 8080    HTTP (alternate / dev servers)
--------------------------------------------------
Scan complete — 1 open port(s) found out of 18 checked.
```
This is how OPENING and CLOSING of Ports work. It is as simple as recieving a call and does't require high level cybersecurity skills. It is all based on Computer Networking System.

# Thank You For Reading.
## Author- Lalit Sharma 
