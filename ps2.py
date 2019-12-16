#!/usr/bin/python

import os
import subprocess
import signal

proc = subprocess.Popen('top', stdout=subprocess.PIPE)
output = proc.stdout

for i in output:
	print(i)
pid=input("enter pid")

os.kill(pid,signal.SIGTERM)



