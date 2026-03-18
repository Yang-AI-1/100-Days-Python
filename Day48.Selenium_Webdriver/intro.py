from selenium import webdriver
#We start by installing selenium as a package
from selenium.webdriver.common.by import By

#configure our webdriver.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True) #Ensures that the page stays open

driver = webdriver.Chrome(options=chrome_options) #We create a webdriver object and select the website we want to drive.
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1") #The driver makes the request itself

price_shilling = driver.find_element(By.CLASS_NAME,value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME,value="a-price-fraction")
print(f"The price is {price_shilling.text}.{price_cents.text}")


# driver.close() This line closes tabs.
driver.quit() #This line quits the entire process at runtime.

#TODO.Selenium is basically beautiful soup abstraction.It does the requests for us and now we can just crape and automate the data.
# You can search an element by Name,Class_name,Css_selector. It returns a selenium object which you can access its attributes.

#Searching for a particular element using the X-path
bug_link = driver.find_element(By.XPATH,value='//*[@id="twotabsearchtextbox"]')