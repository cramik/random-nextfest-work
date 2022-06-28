import subprocess
import os
import time
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from collections import Counter

SW_HIDE = 0
info = subprocess.STARTUPINFO()
info.dwFlags = subprocess.STARTF_USESHOWWINDOW
info.wShowWindow = SW_HIDE
total=0
i=1


if __name__ == '__main__':
	driver = Chrome()
	with open("run.txt", "r") as run:
		total = len(run.readlines())
	
	with open("run.txt", "r") as run:
		for subid in run:
			driver.get(f'https://steamdb.info/sub/{subid}/apps/')
			WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.XPATH,"//div[@id='apps']/div/table/tbody/tr/td/a")))
			link = driver.find_element(By.XPATH, "//div[@id='apps']/div/table/tbody/tr/td/a")
			appid = link.get_attribute("text")
			print(f'{appid} - {i}/{total}')
			p = subprocess.Popen(['steam-idle.exe', appid], stdout=subprocess.PIPE,  startupinfo=info) 
			time.sleep(1)
			p.kill()
			i = i+1