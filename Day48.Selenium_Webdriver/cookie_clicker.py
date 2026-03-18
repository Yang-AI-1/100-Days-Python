from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time

#Configure options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#Driver set up.
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

driver.implicitly_wait(3)

english_select = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
english_select.click()

end_time = time.time() + 300 #This number doesn't change in the loop
check_store_time = time.time() + 4
check_upgrades_time = time.time() + 7
while time.time() < end_time:
    try:
        cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
        cookie.click()
    except StaleElementReferenceException:
        continue
    try:
        if time.time() > check_upgrades_time:
            upgrades = driver.find_element(By.CSS_SELECTOR, "#upgrades")
            selectable_upgrades = upgrades.find_elements(By.TAG_NAME, "div")
            selectable_upgrades[0].click()

            check_upgrades_time = time.time() + 7

        if time.time() > check_store_time:
            store_items = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
            store_items[-1].click()

            check_store_time = time.time() + 4

        if time.time() > end_time:
            cookiespersecond = driver.find_element(By.CSS_SELECTOR, "#cookiesPerSecond" )
            print(cookiespersecond.text)
    except StaleElementReferenceException:
        continue


