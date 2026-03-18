from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Configure options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#Driver set up.
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
#Element search.
f_name = driver.find_element(By.NAME, "fName")
l_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
sign_button = driver.find_element(By.CSS_SELECTOR, "button")
#Form fill in:
f_name.send_keys("Dylan")
l_name.send_keys("Sprounce")
email.send_keys("lalaland@crycry.org")
sign_button.click()

#TODO.REMEMBER: The code always executes sequentially.