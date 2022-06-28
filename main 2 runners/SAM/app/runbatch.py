import subprocess
import os
import time


with open("run.txt", "r") as run:
	for appid in run:
		print(appid)
		p = subprocess.Popen(['SAM.Game.exe', appid], stdout=subprocess.PIPE) 
		time.sleep(5)
		p.kill()