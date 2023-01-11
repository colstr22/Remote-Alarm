import sys
if len(sys.argv) == 1:
    print("To use this tool, you need to pass in the filepath of the target and the IP address of the caller.")
    sys.exit() 
ip = sys.argv[0]
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9999
s.connect((ip, port))
s.sendall(b'1')
s.close()
