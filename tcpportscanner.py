import socket
import argparse

init = argparse.ArgumentParser()
init.add_argument("--host","-i",type=str)
init.add_argument("--port","-p",type=int)
init.add_argument("--range","-r",type=str)
args = init.parse_args()
if args.range :
	getRange = args.range.split("-")
	for i in range(int(getRange[0]),int(getRange[1])):
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	    s.settimeout(1)
	    portscan = s.connect_ex((args.host,i))
	    if portscan == 0:
		    print(f"port {i} is open")
	    else:
		    print(f"port {i} is closed")

	
else:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(1)
	portscan = s.connect_ex((args.host,args.port))
	if portscan == 0:
		print(f" port {args.port} is open")
	else:
		print(f"port {args.port} is closed")
	

	
