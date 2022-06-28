import subprocess
import os
import time
import sys
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from collections import Counter

if __name__ == '__main__':
	driver = Chrome()
	
	homeurl = "https://store.steampowered.com/demos/#p=0&tab=NewReleases"
	driver.get(homeurl)
	WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.XPATH,"//span[@id='NewReleases_links']/span")))
	pages = driver.find_elements(By.XPATH, "//span[@id='NewReleases_links']/span")
	
	lastpage = pages[-1]
	lastpage_index = int(pages[-1].text)
	left_side = homeurl.find("#p=0")
	right_side = homeurl.find("&", left_side)

	for i in range(lastpage_index-1):
		driver.get("chrome://newtab")
		inc_url = homeurl[:left_side] + "#p=" + str(i) + homeurl[right_side:]
		driver.get(inc_url)
		apps = driver.find_elements(By.XPATH, "//div[@id='NewReleasesRows']/a")
		for app in apps:
			try: print(app.get_attribute("data-ds-appid"))
			except: pass