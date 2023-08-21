from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import pickle as pk

class bot():
    def __init__(self, username: str, password: str, path: str) -> None:
        try:
            self.driver = webdriver.Chrome("GramSleuth2\\requirments\\chromedriver.exe")                    #init driver
            print("Found path!")
            self.username = username                                #declare username
            self.password = password                                #declare password
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
            print(f'Error: Could not connect (Selenium).')

    def login(self):
        try:
            wait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(str(self.username))  
            try:    
                wait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(str(self.password))                     #send creds
                print(f"Sending credentials...")
                try:
                    wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'))).click()    #send creds
                    print("Login successful.")
                    try:
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
                            try:
                                wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
                                if str(input("Enable notifications? (y/n): ")).upper() == "Y":
                                    wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Turn On']"))).click()
                                else:
                                    wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']"))).click()
                            except:
                                print("ERROR: Action error (enable notifications)")
                        except:
                            pass
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