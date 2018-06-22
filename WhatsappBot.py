from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

import threading
import time

driver = None

def whatsappWebConnection(chromeDriverPath):
	global driver

	chrome_options = Options() # Saving the last session
	chrome_options.add_argument("user-data-dir=selenium") 
	driver = webdriver.Chrome(chromeDriverPath, chrome_options=chrome_options)
	driver.get('https://web.whatsapp.com/')	

	while True:
		time.sleep(1)
		try:
			appLoad = driver.find_element_by_class_name("m6ZEb") # The class only exists after the QR login page
			if appLoad:
				return # The login was successful
		except NoSuchElementException:
			pass

def sendMessage(targetName, msg):
	global driver
	target = driver.find_element_by_xpath('//span[@title= "{}"]'.format(targetName))
	target.click()

	msg_box = driver.find_element_by_class_name('_2S1VP')
	msg_box.send_keys(msg)
	button = driver.find_element_by_class_name('_2lkdt')
	button.click()

def readAllMessages(targetName, textDirection):
	global driver
	target = driver.find_element_by_xpath('//span[@title= "{}"]'.format(targetName))
	target.click()

	messages = None
	lastMessage = None

	messages = driver.find_elements_by_class_name("_3zb-j")
	lastMessage = messages[-1].text
	lastMessage = lastMessage[::-1]

	while(1):
		try:
			messages = driver.find_elements_by_class_name("_3zb-j")
			if(textDirection == "rtl"):
				for i in range(len(messages)):
					messages[i] = messages[i][::-1]

			return messages
					
		except (NoSuchElementException, StaleElementReferenceException) as e:
			pass

def getLastMessage(targetName, textDirection):
	global driver
	target = driver.find_element_by_xpath('//span[@title= "{}"]'.format(targetName))
	target.click()

	messages = None

	while(1):
		try:
			messages = driver.find_elements_by_class_name("_3zb-j")
			newMessage = messages[-1].text
			if(textDirection == "rtl"):
				newMessage = newMessage[::-1]
			return newMessage

		except (NoSuchElementException, StaleElementReferenceException) as e:
			pass
	