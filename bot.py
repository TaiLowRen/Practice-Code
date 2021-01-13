from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# import python package

PATH = "C:\Program Files (x86)\msedgedriver.exe"
BC = "C:\Program Files (x86)\IEDriverServer"
#adding our download to path

#dynamic variable name LINK
LINKa = 'https://direct.playstation.com/en-us/consoles/console/playstation5-digital-edition-console.3005817'
#link to website 'https://www.walmart.com
htmlids = [ "add-on-atc-container","ProductPrimaryCTA-cta_add_to_cart_button"]
classes = ["button spin-button prod-ProductCTA--primary button--primary"]

driver = webdriver.Edge(PATH)
# we want to use Edge

#driver.get('https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815?irgwc=1&sourceid=imp_1aG0bM2rexyLU-hwUx0Mo3YmUkEzPmSFy1CfXk0&veh=aff&wmlspartner=imp_1943169&clickid=1aG0bM2rexyLU-hwUx0Mo3YmUkEzPmSFy1CfXk0&sharedid=&ad_id=565706&campaign_id=9383')
print(driver.title)



driver.get('https://www.walmart.com/ip/Sony-PlayStation-4-1TB-Slim-Gaming-Console/101507200')

#add = driver.find_element_by_class_name("prod-product-cta-add-to-cart display-inline-block")
#driver.find_element_by_class_name("button spin-button prod-ProductCTA--primary button--primary")



try: 
    add = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "prod-product-cta-add-to-cart display-inline-block"))
    )
    add.send_keys(Keys.ENTER)
except:
    driver.quit()




 #print(driver.page_source) hf-cart


#time.sleep(5)

#driver.quit()