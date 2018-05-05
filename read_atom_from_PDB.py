#system/python3.6.5

import re
import sys

args=sys.argv

pdbfile=open(args[1],"r")

for line in pdbfile:
    if re.search('ATOM',line[0:4])!=None:
        if re.search('CA',line[13:])!=None:
                tmp=re.findall('\s+(\S+)\s+(\S+)\s+(\S+)',line[26:])
                print(tmp[0][0]+" "+tmp[0][1]+" "+tmp[0][2])
pdbfile.close()
