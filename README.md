# tcp-port-scanner
description : fast tool to do port scanning based on tcp connect scanning

### how to using my tool
* port scanning to only one port
```bash
python3 tcpportscanner.py -i example.com -p 80 
```
* port scanning to range of port
```bash
python3 tcpportscanner.py --host 127.0.0.1 -r 80-65535
```
