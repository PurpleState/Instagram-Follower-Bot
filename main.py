from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# for executable_path has been deprecated, please pass in a Service object
# self.driver = webdriver.Chrome(ChromeDriverManager().install())
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
import time

from selenium.common.exceptions import ElementClickInterceptedException

# while installing it, in facing errors: pip install webdriver-manager
# taking help from this already installed project
SIMILAR_ACCOUNT = "INSTAGRAM ACCOUNT YOU WANT TO BECOME"
USERNAME = "YOUR INSTAGRAM EMAIL"
PASSWORD = "YOUR INSTAGRAM PASSWORD"

s=Service(ChromeDriverManager().install())

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=s)
        # uselss: driver = webdriver.Chrome(service=s)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        
        time.sleep(2)
        # can also try: followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        
        time.sleep(10)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            #In this case we're executing some Javascript, that's what the execute_script() method does.
            #The method can accept the script as well as a HTML element.
            #The modal in this case, becomes the arguments[0] in the script.
            #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
