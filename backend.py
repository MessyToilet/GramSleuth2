import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import pickle as pk

class bot():
    def __init__(self, username, password, path):
        try:
            self.driver = webdriver.Chrome(path)                    #init driver
            self.username = username                                #declare username
            self.password = password                                #declare password
            self.driver.get("https://www.instagram.com/login")      #get site
            cookies = pk.load(open("cookies.pkl", "rb"))            #load cookies
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        except:
            print(f'Error: Could not connect (Selenium).')

    def login(self):
        try:
            self.driver.find_element(By.NAME, "username").send_keys(str(self.username))                         #send creds
            try:    
                self.driver.find_element(By.NAME, "password").send_keys(str(self.password))                     #send creds
                try:
                    self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()    #send creds
                    if self.driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F" and str(input("Save login? (y/n): ")).upper() == "Y":
                        try:
                            self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button').click()
                        except:
                            print(f"ERROR: Couldn't Click.")
                    else:
                        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
                except:
                    print(f"ERROR: Couldn't click.")
            except:
                print(f"ERROR: Couldn't send password.")
        except:
            print(f"ERROR: Couldnt't send username.")

    def get_your_followers(self):
        try:
            response = requests.post(f"https://www.instagram.com/{self.username}/followers/")
        except:
            print(f"Navigation_error")