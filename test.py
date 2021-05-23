import os
import socket

cms = "wordpress"
location = "test"
cmd = "./test.bash %s %s"%(cms, location)
os.system(cmd)