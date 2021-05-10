import os
import socket

#stat = os.system('echo 3 | systemctl status apache2 >/dev/null 2>&1')
#stat = os.system("systemctl status apache2")
#if stat == 0:
 #   print ("not running")

#else:
 #   print ("Running")
#print (stat)

ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

print (ip)