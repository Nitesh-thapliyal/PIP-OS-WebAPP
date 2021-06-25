#!/usr/bin/python3

import cgi
import subprocess
import time 

print("context-type: text/html")
print()
#print("let's build something new Nitesh")#here now if now I change anything it will change in page without refreshing

#time.sleep(10) #this holds program for 10 seconds and then run the prog auto
f=cgi.FieldStorage()
cmd=f.getvalue("x")
#print(cmd)

o = subprocess.getoutput("sudo " +cmd)

print(o)
