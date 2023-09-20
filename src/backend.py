from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

from frontend import systemBoarder

import pickle as pk
import sys

class bot():
    def __init__(self) -> None: 
        try:
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))                    #init driver
            systemBoarder(sys='SYSTEM', msg='Found Path!')
        except:
            systemBoarder(sys="ERROR", msg="Could not connect (Selenium)")
       
        try:
            self.driver.get("https://www.instagram.com/")                           #get site
            systemBoarder(sys='SYSTEM', msg='Connecting (Instagram)')
        except:
            systemBoarder(sys="ERROR", msg="Could not connect (Instagram)")
        
        try:
            systemBoarder(sys="SYSTEM", msg="Loading cookies...")
            cookies = pk.load(open("..\\reasources\\cookies.pkl", "rb"))                            #load cookies
            for cookie in cookies:
                self.driver.add_cookie(cookie)
        except:
            systemBoarder(sys="ERROR", msg="Could not load cookies")                #edge case

    def login(self) -> bool:
        self.username = str(input(f"\nUsername: "))                                 #declare username
        self.password = str(input(f"Password: "))                                   #declare password
        print()
        
        try:    #USERNAME 
            systemBoarder(sys="system", msg="Finding username element...")
            wait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(str(self.username))  
            systemBoarder(sys="system", msg="Sending credentials...")
        except:
            systemBoarder(sys="error",msg="Could not find username element")        #or send keys or bad args?
        
        try:    #PASSWORD
            systemBoarder(sys="system", msg="Finding password element...")  
            wait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(str(self.password))                     #send creds
            systemBoarder(sys="system",msg="Sending credentials...")
        except:
            systemBoarder(sys="error", msg="Could not find password element")       #or send keys or bad creds
        
        try:    #LOG IN
            systemBoarder(sys="system",msg="Finding login element")
            wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'))).click()    #send creds
            systemBoarder(sys="system", msg="Login sucessfull")
        except:
            systemBoarder(sys="ERROR", msg="Could not login")
        
        try:    #handling save login
            systemBoarder(sys="system", msg='Scanning for element...')
            wait(self.driver, 10).until(EC.url_to_be("https://www.instagram.com/accounts/onetap/?next=%2F"))
            if self.driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":
                if str(input("\nSave login? (y/n): ")).upper() == "Y":
                    try:
                        systemBoarder(sys="system", msg="Saving cookies...")
                        wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button'))).click()
                        pk.dump(self.driver.get_cookies(), open("coockies.pkl", "wb"))
                    except:
                        systemBoarder(sys="error", msg="Could not click")
                else:
                    wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))).click()            
                print()
        except:
            systemBoarder(sys='error', msg="Could not perform save login action")

        try:    #handling notifications
            systemBoarder(sys="system", msg='Scanning for element...')
            wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
            if str(input("\nEnable notifications? (y/n): ")).upper() == "Y":
                systemBoarder(sys="system", msg='\nEnabling notifications...')
                wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Turn On']"))).click()
            else:
                systemBoarder(sys="system", msg='Not enabling notifications...')
                wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']"))).click()            
            print()
            return True 
        except:
            systemBoarder(sys='error', msg="Could not perform notifications action")
    
### USER ACTOINS ###

    def get_your_info(self):
        try:
            systemBoarder(sys='SYSTEM', msg='Loading followers...')
            self.driver.get(f"https://www.instagram.com/{self.username}/")
        except:
            print(systemBoarder(sys='ERROR', msg='Could not load profile'))

        systemBoarder(sys='SYSTEM', msg='Collecting data...')

        try:
            systemBoarder(sys='SYSTEM', msg='Collecting post count...')
            postCount = wait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mount_0_0_nI > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > ul > li:nth-child(1) > span > span"))).text
            print(f'Num Posts: {postCount}')
        except:
            systemBoarder(sys="error", msg="Could not find post count")

        try:
            systemBoarder(sys='SYSTEM', msg='Collecting follower count...')
            followerCount = wait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mount_0_0_nI > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > ul > li:nth-child(2) > a > span > span"))).text
            print(f'Followers: {followerCount}')
        except:
            systemBoarder(sys="error", msg="Could not find follower count")

        try:    
            systemBoarder(sys='SYSTEM', msg='Collecting following count...')
            followingCount = wait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#mount_0_0_nI > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > ul > li:nth-child(3) > a > span > span"))).text
            print(f'Following: {followingCount}')
        except:
            systemBoarder(sys='error', msg='Could not find following count')

        try:
            systemBoarder(sys='system', msg='Collecting bio...')
            bio = self.driver.find_element(By.XPATH('/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/div[1]')).text()
        except:
            systemBoarder(sys='error', msg='Could not collet bio')


    def get_your_followers(self):
        try:
            systemBoarder(sys='SYSTEM', msg='Loading followers...')
            self.driver.get(f"https://www.instagram.com/{self.username}/followers/")
            
            systemBoarder(sys='SYSTEM', msg='Waiting...')
            wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Remove']")))
            
            systemBoarder(sys='SYSTEM', msg='Scrolling...')
            numScrolls = 20
            for _ in range(numScrolls):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
            
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #problem here
        except:
            systemBoarder(sys='ERROR', msg='Could not find')
          

    def get_your_following(self):
        return
    
### TARGET ACTIONS ###  

    def get_target_info(self, target):
        print("Loading target...")
        self.driver.get(f"https://www.instagram.com/{target}/")        
        return
    
    def get_target_followers(self, target):
        print("Loading target...")
        self.driver.get(f"https://www.instagram.com/{target}/followers")        
        return
    
    def get_target_following(self, target):
        print("Loading target...")
        self.driver.get(f"https://www.instagram.com/{target}/followering") 
        return
    




    def quit(self):
            try:
                systemBoarder(sys='system', msg='Saving cookies...')
                cookies = self.driver.get_cookies()                         #save cookies
            except:
                systemBoarder(sys='error', msg='Could not save cookies')

            try:
                systemBoarder(sys='SYSTEM',msg='Quiting selenium...')
                self.driver.quit()                                          #quit selenium     
            except:
                systemBoarder(sys='error', msg='Could not quit selenium')                

            try:
                systemBoarder(sys='system', msg='Stuffing cookies...')
                with open('..\\reasources\\cookies.pkl', 'wb') as file:                     #open cookie file
                    pk.dump(cookies, file)                                  #dump cookies
                systemBoarder(sys='system', msg='Cookies stuffed...')
            except:
                systemBoarder(sys='error', msg='Could not save cookies')

            systemBoarder(sys='SYSTEM',msg='Quiting...')
            sys.exit()

def getTitle(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    span_element = soup.find('span', {'title': True})
    title = span_element['title']
    return title