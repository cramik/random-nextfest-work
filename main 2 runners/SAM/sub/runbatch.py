import subprocess
import os
import time
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from collections import Counter
append = []
runcount = 0

def getTasks(name):
    r = os.popen('tasklist /v /FI "WINDOWTITLE eq Steam"').read().strip().split('\n')
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            return r[i]
    return []

if __name__ == '__main__':
	driver = Chrome()

	with open("run.txt", "r") as run:
		with open("ran.txt","r") as ran:
			#result = list((Counter(ran) - Counter(run)).elements())
			for subid in run:
				if subid not in ran:
					driver.get(f'https://steamdb.info/sub/{subid}/apps/')
					WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.XPATH,"//div[@id='apps']/div/table/tbody/tr/td/a")))
					link = driver.find_element(By.XPATH, "//div[@id='apps']/div/table/tbody/tr/td/a")
					appid = link.get_attribute("text")
					print(appid)
					#while('Not Responding' in getTasks('steam.exe')): time.sleep(1)
					p = subprocess.Popen(['SAM.Game.exe', appid], stdout=subprocess.PIPE) 
					time.sleep(1)
					p.kill()
					runcount = runcount + 1
					append.append(subid)
	print(f'runcount = {runcount}')
	with open("ran.txt",'a') as ran:
		for subid in append:
			ran.write(subid.strip()+"\n")