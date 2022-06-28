import time
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

options = ChromeOptions()
options.headless=True
options.add_argument('--headless')

if __name__ == '__main__':
	driver = Chrome(options=options)
	driver.get("https://store.steampowered.com/sale/nextfest")
	
	def scrape():
		driver.execute_script("function setDisplay(className, displayValue) {var items = document.getElementsByClassName(className);for (var i=0; i < items.length; i++) {items[i].style.display = displayValue;}}setDisplay('demobutton_DemoButton_1GAs9', 'block');") #by default, the install buttons are hidden until hovered over. this changes the CSS that causes this to solve that
		installbuttons = driver.find_elements(By.CSS_SELECTOR,".demobutton_DemoButton_1GAs9")
		for installbutton in installbuttons:
			WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CSS_SELECTOR,".demobutton_DemoButton_1GAs9")))
			ActionChains(driver).move_to_element(installbutton).perform()
			installbutton.click()
			WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.XPATH,"//*/text()[normalize-space(.)='Yes, Steam is installed']/parent::*")))
			runbutton = driver.find_element(By.XPATH, "//*/text()[normalize-space(.)='Yes, Steam is installed']/parent::*")
			link = runbutton.find_element(By.XPATH,"./..").get_attribute("href")
			print(link[-7:]) #removes the steam://run/ from the link and prints
			WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.XPATH,"(.//*[normalize-space(text()) and normalize-space(.)='Steam desktop application'])[1]/preceding::*[name()='svg'][1]")))
			close = driver.find_element(By.XPATH, "(.//*[normalize-space(text()) and normalize-space(.)='Steam desktop application'])[1]/preceding::*[name()='svg'][1]")
			close.click()
	
	def load():
		try: 
			while(WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CSS_SELECTOR,"button.saleitembrowser_ShowContentsButton_3d9cK.Focusable")))): #While loop with try except so it will break on error, there's probably a better way to check if the button is still available but I'm not sure
				more = driver.find_element(By.CSS_SELECTOR, "button.saleitembrowser_ShowContentsButton_3d9cK.Focusable")
				more.click()
				WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CSS_SELECTOR,"button.saleitembrowser_ShowContentsButton_3d9cK.Focusable")))
		except Exception as e: pass
		
	
	driver.execute_script("window.scrollTo(0, 2500)") #Scroll to games
	time.sleep(2) #if the page loads to slow, the next two commands will fail
	WebDriverWait(driver, 60).until(ec.presence_of_element_located((By.CSS_SELECTOR,"polygon")))
	driver.find_element(By.CSS_SELECTOR, "polygon").click() # Close video stream (saves resources + prevents from getting in the way of buttons)
	print("Loading all entries, please wait")
	load()
	scrape()