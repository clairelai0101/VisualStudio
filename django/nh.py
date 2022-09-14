import os
from subprocess import *

def input1_ip(x):
     cmd = "vtysh -c 'show ip route {}'".format(x)
     result = os.popen(cmd)
     res = result.read()
     for line in res.splitlines():
         if "*" in line:
             nh1 = line.split()[1]
             return(nh1)