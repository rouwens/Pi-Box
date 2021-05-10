import os

#stat = os.system('echo 3 | systemctl status apache2 >/dev/null 2>&1')
#stat = os.system("systemctl status apache2")
#if stat == 0:
 #   print ("not running")

#else:
 #   print ("Running")
#print (stat)

check = os.path.isdir('/var/')
print (check)