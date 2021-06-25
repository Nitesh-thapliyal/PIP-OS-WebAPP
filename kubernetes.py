#!/usr/bin/python3

import cgi
import subprocess as sp
import time

print("context-type: text/html")
print()
#print("let's build something new Nitesh")#here now if now I change anything it will change in page without refreshing

#time.sleep(10) #this holds program for 10 seconds and then run the prog auto
f=cgi.FieldStorage()
#print(cmd)
#cmd = f.getvalue("x")

#o = subprocess.getoutput(cmd + " --kubeconfig admin.conf")

#print(o)

query = f.getvalue("x")

if "show pods" in query:
    cmd = "kubectl get pods --kubeconfig admin.conf"
    o=sp.getoutput(cmd)
    print(o)

elif "show deployment" in query:
    cmd = "kubectl get deployments --kubeconfig admin.conf"
    o = sp.getoutput(cmd)
    print(o)

elif "httpd" in query:
    cmd = "kubectl create deployment web --image=httpd --kubeconfig admin.conf"
    o = sp.getoutput(cmd)
    print(o)

elif "delete deployment" in query:
    cmd ="kubectl delete deployment web --kubeconfig admin.conf "
    o = sp.getoutput(cmd)
    print(o)

elif "show nodes" in query:
    cmd = "kubectl get nodes --kubeconfig admin.conf "
    o = sp.getoutput(cmd)
    print(o)

elif "describe deployment" in query:
    cmd = "kubectl describe deployment --kubeconfig admin.conf "
    o = sp.getoutput(cmd)
    print(o)

elif "show service" in query:
    cmd = "kubectl get svc --kubeconfig admin.conf "
    o = sp.getoutput(cmd)
    print(o)

