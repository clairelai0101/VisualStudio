import os
from subprocess import *
cmd = "vtysh -c 'show ip route 27.50.0.82'"
#os.system(cmd)
result = os.popen(cmd)
#result = os.system("vtysh -c 'show ip route 27.50.0.82'")
#print(result)
res = result.read()
for line in res.splitlines():
    if "*" in line:
        nh = line.split()[1]
        print(nh)ljhkjhkjh