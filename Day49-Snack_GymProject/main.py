from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as ec
from datetime import datetime, timedelta
import os

ACCOUNT_EMAIL = "dylan@test.com"
ACCOUNT_PASSWORD = "1Ga8jh7gf5#"
GYM_URL = "https://appbrewery.github.io/gym/"
CLASSES_BOOKED = 0
WAITLISTS_JOINED = 0
ALREADY_BOOKED = 0
TOTAL_CLASSES = 0

#Chrome configuration.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(),"chrome_profile") #Directory path for storing user data
chrome_options.add_argument(f"--user-data-dir={user_data_dir}") #stores user data

#WebDriver setup.
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)
#Wait until the login button is clickable and click on it
join_button = wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="home-page"]/section[1]/div/div/a[1]/button')))
join_button.click()

#Fill in the login form email,password and submission.
email_input = wait.until(ec.presence_of_element_located((By.NAME,"email")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.NAME, "password")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

login_button = driver.find_element(By.CSS_SELECTOR, "#submit-button")
login_button.click()

#Tuesday and Thursday workout booking. Code due for refactor because It's basically hardcoded.
#Time processing to get the exact date for next Tuesday format %Y-%m-%d
today = datetime.now()
days_until_tuesday = (1 - today.weekday() + 7) % 7 or 7
next_tuesday = today + timedelta(days=days_until_tuesday)
tues_day = next_tuesday.strftime("%Y-%m-%d")

#Time processing to get the exact date for next Thursday.
days_until_thursday = (3 - today.weekday() + 7) % 7 or 7
next_thursday = today + timedelta(days=days_until_thursday)
thurs_day = next_thursday.strftime("%Y-%m-%d")

try:
    #Details for next Tuesday's workout
    tuesday_workout = wait.until(ec.presence_of_element_located((By.XPATH, f'//*[@id="class-card-spin-{tues_day}-1800"]')))
    book_btn_tues = tuesday_workout.find_element(By.TAG_NAME, "button")
    workout_name_tues = tuesday_workout.find_element(By.TAG_NAME, "h3").text
    workout_time_tues = tuesday_workout.find_element(By.XPATH, f'//*[@id="class-time-spin-{tues_day}-1800"]').text
    tuesday_state = book_btn_tues.text

    #Details for next Thursday's workout
    thursday_workout = wait.until(ec.presence_of_element_located((By.XPATH, f'//*[@id="class-card-spin-{thurs_day}-1800"]')))
    book_btn_thurs = thursday_workout.find_element(By.TAG_NAME, "button")
    workout_name_thurs = thursday_workout.find_element(By.TAG_NAME, "h3").text
    workout_time_thurs = thursday_workout.find_element(By.XPATH, f'//*[@id="class-time-spin-{thurs_day}-1800"]').text
    thursday_state = book_btn_thurs.text

    #Tuesday workout booking.
    if tuesday_state == "Booked":
        print(f"Already {tuesday_state} for Tuesday {workout_name_tues} on {tues_day} at {workout_time_tues}\n")
        ALREADY_BOOKED += 1
    elif tuesday_state == "Waitlisted":
        print(f"Already {tuesday_state} for Tuesday {workout_name_tues} on {thurs_day}\n")
        WAITLISTS_JOINED += 1
    else:
        book_btn_tues.click()
        print(f"Successful: {tuesday_state}: {workout_name_tues} Class on Tuesday {tues_day}\n")
        CLASSES_BOOKED += 1
    TOTAL_CLASSES += 1

    #Thursday workout booking.
    if thursday_state == "Booked":
        print(f"Already {thursday_state} for Tuesday {workout_name_thurs} on {thurs_day}\n")
        ALREADY_BOOKED += 1
    elif thursday_state == "Waitlisted":
        print(f"Already {thursday_state} for Tuesday {workout_name_thurs} on {thurs_day}\n")
        WAITLISTS_JOINED += 1
    else:
        book_btn_thurs.click()
        print(f"Successful: {thursday_state}: {workout_name_thurs} Class on Thursday {thurs_day}\n")
        CLASSES_BOOKED += 1
    TOTAL_CLASSES += 1

    #Checking my bookings to verify presence of booking.
    my_bookings_btn = driver.find_element(By.CSS_SELECTOR,"#my-bookings-link")
    my_bookings_btn.click()
    driver.implicitly_wait(2)
    bookings_section = driver.find_element(By.CSS_SELECTOR,"#confirmed-bookings-section > div")
    confirmed_bookings = bookings_section.find_elements(By.TAG_NAME, "div")
    booking_num = len(confirmed_bookings) / 2 #If your wondering what this is for, the Divs inside the booking class
                                            #have nested divs. So the number I want is always doubled.

    print(f"Total Current Confirmed Bookings:{booking_num}")

    print(f""" ----------- BOOKING SUMMARY ------------\n
        1. CLASSES BOOKED: {CLASSES_BOOKED}\n
        2. WAITLISTS JOINED: {WAITLISTS_JOINED}\n
        3. ALREADY BOOKED:{ALREADY_BOOKED}\n
        4. TOTAL TUESDAY AND THURSDAY CLASSES PROCESSED: {TOTAL_CLASSES}""")


except NoSuchElementException,StaleElementReferenceException:
    print("Stale element or No such element at all found for the tuesday spin booking/waitlist button.\n"
          "This could mean that there are:\n"
          "1.No classes on Tuesday or Thursday,or none at 6pm atleast.\n"
          "2.Booking buttons that have not been found.\n"
          "3.Issues and Bugs partaining X-Paths.")


#TODO.Revisions: SO I essentially gave up. I tried doing the last step but I stashed the change and I decided not to continue.
# On a project such a s this I couldn't drag on with my Naivete. This needed a structured logical flow. Algorithm writing-
# must be where the meat is especially if its web-driving on servers you can't control.
# The actual revisions:
# 1. My element identification was poor in this project. I used hard coded Id's, and although my time identification logic was clever(But stolen),
#    It didn't satisfy. Instead I should have used attribute selection. p[id^='class-card-']  <----- something like that.
# 2. I failed to write the retry function wrapper in case of Network errors which it handles gracefully with a number of retries
#    Ill just go ahead and paste the code here:
# def retry(func, retries=7, description=None):
#     for i in range(retries):
#         print(f"Trying {description}. Attempt: {i + 1}")
#         try:
#             return func()
#         except TimeoutException:
#             if i == retries - 1:
#                 raise
#             time.sleep(1)
# 3. My error handling is very week. Ive wrapped the entire thing in a try except block. Ill never know where anything went wrong lol.
#    Angela handles her errors sequentially. Exceptionally in the get bookings function she intentionally weaponises it incase
#    cards dont appear on the page. 2. She during the verification for loop she searches broadly for elements with a strong text of when
#    and passes a No such element exception proving that they arent verified cards. Thats pretty nice..
# 4. Oerall I tried really hard. Atleast Ive learned from my experience