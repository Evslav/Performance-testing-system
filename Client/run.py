from time import time
from subprocess import Popen
import json
import requests

cmd = "C:\ConsoleApplication8.exe"
t1 = time()
p = Popen(cmd)
p.wait()
t2 = time()
elapsedTime = t2 - t1
returnCode = p.returncode
data = {"cmd": cmd, "time": elapsedTime, "result": returnCode}
print (data)
data = json.dumps(data)
"""r = requests.get('https:\\127.0.0.1\getdata', data=data)
if r.status_code != 200:
    print("Fail")
else:
    print("Pass")
"""
