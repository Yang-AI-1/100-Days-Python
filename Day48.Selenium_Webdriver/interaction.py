from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Configure options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#Driver set up.
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
#Element search
number_of_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
# number_of_articles.click() clicks on the element.

#Find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
#all_portals.click()

# Find the "Search" <input>
search = driver.find_element(By.NAME, value="search")

#Sending Keyboard input to Selenium via text.
search.send_keys("Python", Keys.ENTER) #So here the second argument allows us to type input from the keyboard to the website.
