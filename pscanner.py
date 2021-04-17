#!/bin/python3

 
import sys
import socket
from datetime import datetime


name = """\u001b[35m
______                                    
| ___ \                                   
| |_/ /__  ___ __ _ _ __  _ __   ___ _ __ 
|  __/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|
| |  \__ \ (_| (_| | | | | | | |  __/ |   
\_|  |___/\___\__,_|_| |_|_| |_|\___|_|   
                               \u001b[0m 
           
               \u001b[32m -  small port scanner by <CyborJ                        
     """


print(name)

#Define our target



if len(sys.argv) == 2:
      target = socket.gethostbyname(sys.argv[1])
      
else:
      print("Invalid amount of arguments.")
      print("syntax: python3 scanner.py <ip>")

#Add banner
print("-" * 50)
print("Scanning Target " + target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
       for port in range(1,65535):
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               socket.setdefaulttimeout(1)
               result = s.connect_ex((target,port)) #rror indicator
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
       print("Couldn't connect to server.")
       sys.exit()
