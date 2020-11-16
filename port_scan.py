#!/bin/python3

import sys
import socket
from datetime import datetime


# Define our tarjet
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # Translate host name to IPv4
else:
	print("Invalid amount of arguments")
	print("SYNTAX: python3 port_scan.py <ip>")
	
# Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(1, 5000):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port)) # returns an error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("couldn't connect to server")
	sys.exit()

