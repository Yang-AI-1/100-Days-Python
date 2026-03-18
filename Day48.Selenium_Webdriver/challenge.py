from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#Set up the webdriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

upcoming_section = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
items = upcoming_section.find_elements(By.CSS_SELECTOR, "li")
events_dict = {}

for index, item in enumerate(items):
    date = item.find_element(By.CSS_SELECTOR, "time").text
    event = item.find_element(By.CSS_SELECTOR, "a").text
    events_dict[index] = {
        "date": date,
        "event": event
    }



driver.quit()

#TODO.Revisions:
# What does the enumerate function do?
# 1. It transforms each item in a list into a tuple of (index,item)
# 2. You mainly use it in for loops like; for index, item(any var name) in enumerate(*a-list*)
# In retrospect I should know and practice how to format dictionaries.
# .
# In the previous code version I would've formatted the dictionary like this:
#   for index in range(len(list-of-event-objects-)):
#       events_dictionary[index - represents key assignment] = {
#           "date": date-list[index],
#           "time: time-list[index]
#       }
