#Headless browser imports
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
#Interval imports
import time
import datetime
#Email imports
import smtplib, ssl

def email_usr(URL): #Email with python
    port = 465  # For SSL
    password = "PLACEHOLDER"
    # Create a secure SSL context
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("throwawayAmarok@gmail.com", password)
        server.sendmail("PLACEHOLDER", "PLACEHOLDER","""\
Subject: Stock Available for Nike Air Force 1's EU 44.5

Stock available now on Nike.com .\n"""+URL)

def get_stock(URL,productname): #Get stock of Air forces from nike.com
    ser = Service("C:/Users/anton/OneDrive/Desktop/Πανεπιστημιο/Personal Projects/Python/Nike Stock - Track And Email/chromedriver") # Druver as service obj
    chrome_options=Options()
    chrome_options.add_argument('--log-level=3') # Suppress non-fatal errors/warnings/info
    chrome_options.add_argument("--headless") # Run in background
    driver = webdriver.Chrome(service=ser,options=chrome_options) # Create driver
    with driver as driver:
        wait=WebDriverWait(driver,10) #Wait for load
        time.sleep(5)
        driver.get(URL)
        parent_element=driver.find_element(By.XPATH,'//div[@class="mt2-sm css-12whm6j"]') #get parent element of each stock
        div_content=parent_element.get_attribute("innerHTML") # get inner code of parent
        order=div_content.split('</div>') # split sizes
        for size in order:
            if not "disabled=""" in size: # disabled keyword means no stock
                if "EU 44.5" in size:
                    email_usr(URL)
                    print("\nStock detected for "+productname+". User has been notified by email")
                    time.sleep(15)
                    quit()
        print("\nSize for "+productname+" not found at: "+datetime.datetime.now().strftime("%c"))

while(True):
    #get_stock('https://www.nike.com/gr/t/%CE%B1%CE%BD%CE%B4%CF%81%CE%B9%CE%BA%CE%BF-%CF%80%CE%B1%CF%80%CE%BF%CF%85%CF%84%CF%83%CE%B9-air-force-1-07-lKPQ6q/CW2288-111','Air Force 1 White')
    #get_stock('https://www.nike.com/gr/t/%CE%B1%CE%BD%CE%B4%CF%81%CE%B9%CE%BA%CE%BF-%CF%80%CE%B1%CF%80%CE%BF%CF%85%CF%84%CF%83%CE%B9-air-force-1-07-pXTXQ8/CT2302-100','Air Force 1 White-Black Swoosh')
    get_stock('https://www.nike.com/gr/t/%CE%B1%CE%BD%CE%B4%CF%81%CE%B9%CE%BA%CE%B1-%CF%80%CE%B1%CF%80%CE%BF%CF%85%CF%84%CF%83%CE%B9%CE%B1-air-force-1-46WdMJ/DO6394-100','Air Force 1 White-Black-Orange Swoosh')
    time.sleep(300)
