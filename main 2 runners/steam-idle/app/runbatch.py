import subprocess
import os
import time

SW_HIDE = 0
info = subprocess.STARTUPINFO()
info.dwFlags = subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = SW_HIDE
total=0
i=1

with open("619.txt", "r") as run:
	total = len(run.readlines())

with open("619.txt", "r") as run:
	for appid in run:
		if (i>0):
			print(f'{appid[:-1]} - {i}/{total}')
			p = subprocess.Popen(['steam-idle.exe', appid], stdout=subprocess.PIPE,  startupinfo=info) 
			time.sleep(2)
			p.kill()
		i = i+1