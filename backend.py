from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import pickle as pk
import sys

class bot():
    def __init__(self) -> None:
        try:
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))                    #init driver
            print("Found path!")
            try:
                self.driver.get("https://www.instagram.com/")           #get site
                print("Capturing cookies...")
                try:
                    cookies = pk.load(open("cookies.pkl", "rb"))            #load cookies
                    for cookie in cookies:
                        self.driver.add_cookie(cookie)
                except:
                    print("ERROR: Couldn't capture cookies.")
            except:
                print(f'ERROR: Could not connect (instagram)')
        except:
            print(f'ERROR: Could not connect (Selenium).')

    def login(self) -> bool:
        self.username = str(input(f"\nUsername: "))                                #declare username
        self.password = str(input(f"Password: "))                                  #declare password
        try:
            wait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(str(self.username))  
            try:    
                wait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(str(self.password))                     #send creds
                print(f"\nSending credentials...")
                try:
                    wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'))).click()    #send creds
                    print("Login successful.")
                    try:
                        wait(self.driver, 10).until(EC.url_to_be("https://www.instagram.com/accounts/onetap/?next=%2F"))
                        if self.driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":
                            if str(input("Save login? (y/n): ")).upper() == "Y":
                                try:
                                    wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button'))).click()
                                    pk.dump(self.driver.get_cookies(), open("coockies.pkl", "wb"))
                                    print(f"Saving cookies...")
                                except:
                                    print(f"ERROR: Couldn't Click.")
                            else:
                                wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))).click()

                        try:
                            wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
                            if str(input("Enable notifications? (y/n): ")).upper() == "Y":
                                wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Turn On']"))).click()
                            else:
                                wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']"))).click()
                            return True
                        except:
                            print("ERROR: Action error (enable notifications)")
                    except:
                        print("ERROR: Action error (save login).")
                except:
                    print(f"ERROR: Couldn't click login.")
            except:
                print(f"ERROR: Couldn't send password.")
        except:
            print(f"ERROR: Couldnt't send username.")

    def get_your_followers(self):
        try:
            print("Loading followers...")
            self.driver.get(f"https://www.instagram.com/{self.username}/followers/")
            print("Scrolling...")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #problem here
        except:
            print(f"ERROR: Could not find.")

    def quit(self):
            print(f'Quiting...')
            self.driver.quit()
            sys.exit()