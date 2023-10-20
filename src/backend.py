from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

from frontend import systemBoarder

import pickle as pk     #cookie files
import time
import sys  

class bot():
    def __init__(self) -> None: 
        try:
            systemBoarder(sys='system', msg='Looking for path...')
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))                    #init driver
            systemBoarder(sys='SYSTEM', msg='Found Path!')
        except:
            systemBoarder(sys="ERROR", msg="Could not connect (Selenium)")
       
        try:
            self.driver.get("https://www.instagram.com/")                           #get site
            systemBoarder(sys='SYSTEM', msg='Connecting (Instagram)')               #print connecting
        except:
            systemBoarder(sys="ERROR", msg="Could not connect (Instagram)")
        
        try:
            systemBoarder(sys="SYSTEM", msg="Loading cookies...")
            cookies = pk.load(open("..\\reasources\\cookies.pkl", "rb"))            #load cookies
            for cookie in cookies:                                                  #open cookies file
                self.driver.add_cookie(cookie)                                      #dump cookies with selenium
        except:
            systemBoarder(sys="ERROR", msg="Could not load cookies")                #edge case

    def login(self) -> bool:

        #START WHILE LOOP FOR FAILED LOGIN
        while True:                                                                                 #until login successful
            userInput = str(input(f'\nUse a saved login? (y/n/q): '))
            userInput = userInput.upper()
            if userInput == 'Y':                                                                    #Ask to use saved login
                print()
                try:
                    systemBoarder(sys='system', msg='Checking for saved logins...')                 #print
                    logins = []                                                                     #put logins into array
                    with open('..\\reasources\\savedLogins.txt', 'r') as file:                      #open login file
                        for line in file:                                                           #iterate through file
                            logins.append(line.strip("\n"))                                         #Append login, strip new line

                    systemBoarder(sys='systeam', msg=f'Found {len(logins)} logins...')              #print success and how many logins
                    
                    print()
                    for count, login in enumerate(logins):                                          #for num of logins 
                        print(count, login)                                                         #print the number and login
                    print()

                    choice = int(input(f'Pick your login: '))                                       #Ask user to pick (HANDLE CONDITION LOGIN NO LONGER WORKS AND FAILED LOGIN IN GENERAL)
                    print()

                    self.username = logins[choice].split()[0]                                        #Choose username
                    self.password = logins[choice].split()[1]                                        #Choose password
                    systemBoarder(sys='system', msg=f'Using {self.username} {self.password}')       #Print user and pass
                
                except:
                    systemBoarder(sys='error', msg='Could not find login files')                #If login file could not be found
                    self.username = str(input(f"\nUsername: "))                                 #declare username
                    self.password = str(input(f"Password: "))
                    print()                                   #declare password
            
            elif userInput == "Q":
                systemBoarder(sys='system', msg='Quiting')
                quit()

            else:       
                self.username = str(input(f"\nUsername: "))                                     #ask for username
                self.password = str(input(f"Password: "))                                       #Ask for password
                print()

            try:                                                                                                                        #USERNAME 
                systemBoarder(sys="system", msg="Finding username element...")                                                          #Start username login sequence
                usernameBox = wait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))                         #find username element (wait)
                systemBoarder(sys='system', msg='Clicking into text box...')
                usernameBox.click()
                systemBoarder(sys='system', msg='Clearing text box...')
                self.driver.execute_script("arguments[0].value = '';", usernameBox)                                                     #clear text box
                systemBoarder(sys='system', msg='Sending keys...')
                usernameBox.send_keys(str(self.username))                                                                               #send keys (username)
                systemBoarder(sys="system", msg="Sending credentials...")                                                               #print success
            except:
                systemBoarder(sys="error",msg="Could not find username element")                                                        #print username failed (could not find)
            
            try:                                                                                                                        #PASSWORD
                systemBoarder(sys="system", msg="Finding password element...")                                                          #Start password login sequence
                passwordBox = wait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))                         #Find password element (wait)
                systemBoarder(sys='system', msg='Clicking into text box...')
                passwordBox.click()
                systemBoarder(sys='system', msg='Clearing text box...')
                self.driver.execute_script("arguments[0].value = '';", passwordBox)                                                     #clear text box
                systemBoarder(sys='system', msg='Sending keys...')
                passwordBox.send_keys(str(self.password))                                                                               #send keys (password)
                systemBoarder(sys="system",msg="Sending credentials...")                                                                #Print success
            except:                 
                systemBoarder(sys="error", msg="Could not find password element")                                                       #print password failed (could not find)
            
            try:                                                                                                                                #LOG IN
                systemBoarder(sys="system",msg="Finding login element")                                                                         #start click login sequence
                wait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'))).click()    #Find login button element (wait) and click
                systemBoarder(sys="system", msg="Sending keys...")                                                                              #Print success
            except:
                systemBoarder(sys="ERROR", msg="Could not find login or creds do not suffice")                                                                               #Print click failed (could not find or bad creds)

            try:#Find icon that only appears when logged in to confirm login
                wait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)")))
                systemBoarder(sys='system', msg='LOGIN SEQUENCE SUCCESSFUL!')       #print login successful
                break                                                               #break from loop
            except:
                systemBoarder(sys='error', msg='FAILED LOGIN SEQUENCE')             #print login failed

        #END LOOP FOR FAILED LOGIN - Find way to clear previous input

        try:                                                                                                        #handling save login
            systemBoarder(sys="system", msg='Scanning for element...')                                              #print waiting
            wait(self.driver, 5).until(EC.url_to_be("https://www.instagram.com/accounts/onetap/?next=%2F"))        #wait for url to change (indicats instagram is asking to add 2 factor)
            if self.driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":                    #if instagram is asking
                if str(input("\nSave login for Instagram? (y/n): ")).upper() == "Y":                                #and if user says 'y' (yes) to save login
                    try:
                        systemBoarder(sys="system", msg="Saving cookies...")                                                                                                                                                    #print save cookies
                        wait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button'))).click()        #find button for yes and click
                        pk.dump(self.driver.get_cookies(), open("coockies.pkl", "wb"))                                                                                                                                          #save cookies
                    except:
                        systemBoarder(sys="error", msg="Could not click")                                                                                                                                                       #if failed print error
                else:                                                                                                                                                                                                           #if user doesn't pick yes
                    wait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div'))).click()                       #wait and click no
                print()
        except:
            systemBoarder(sys='error', msg="Could not perform save login action")                                                   #if save login fails print

        try:                                                                                                                        #handling notifications
            systemBoarder(sys="system", msg='Scanning for element...')                                                              #print waiting
            wait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))                   #if notification button found
            if str(input("\nEnable notifications? (y/n): ")).upper() == "Y":                                                        #if user picks to endable notifications
                systemBoarder(sys="system", msg='\nEnabling notifications...')                                                      #print endabling notifs
                wait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Turn On']"))).click()       #find and click yes button
            else:                                                                                                                   #if user picks not to
                systemBoarder(sys="system", msg='Not enabling notifications...')                                                    #print confirmation
                wait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']"))).click()       #find and click no button
            print()
            return True                                                                                                             #return success flag for login method
        except:
            systemBoarder(sys='error', msg="Could not perform notifications action")                                                #if failed print 
    
### USER ACTOINS ###

    def get_your_info(self):
    
        try:
            systemBoarder(sys='SYSTEM', msg='Loading profile...')                  #print 
            self.driver.get(f"https://www.instagram.com/{self.username}/")           #try loading url of username
            time.sleep(5)
        except:
            systemBoarder(sys='ERROR', msg='Could not load profile')                 #if failed print

        systemBoarder(sys='SYSTEM', msg='Collecting data...')                        #print start sequence

        
        try:
            systemBoarder(sys='SYSTEM', msg='Collecting post count...')
            postCount = self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > section:nth-child(1) > main:nth-child(1) > div:nth-child(1) > header:nth-child(1) > section:nth-child(2) > ul:nth-child(3) > li:nth-child(1) > span:nth-child(1) > span:nth-child(1)").text
            #print(f'Num Posts: {postCount}') #error here
        except:
            systemBoarder(sys="error", msg="Could not find post count")

        try:
            systemBoarder(sys='SYSTEM', msg='Collecting follower count...')
            followerCount = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[2]/a[1]/span[1]/span[1]").text
            #followerCount = wait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mount_0_0_0l > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > header > section > ul > li:nth-child(2) > a > span"))).title
            #print(f'Followers: {followerCount}')
        except:
            systemBoarder(sys="error", msg="Could not find follower count")

        try:    
            systemBoarder(sys='SYSTEM', msg='Collecting following count...')
            followingCount = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) a:nth-child(1) span:nth-child(1) span:nth-child(1)").text
            #followingCount = wait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#mount_0_0_0l > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > header > section > ul > li:nth-child(3) > a > span > span"))).text
            #print(f'Following: {followingCount}')
        except:
            systemBoarder(sys='error', msg='Could not find following count')

        try:
            systemBoarder(sys='system', msg='Collecting bio...')            
            bio = self.driver.find_element(By.CLASS_NAME, "_aacl").text     #Get bio, must parse (contains new line chars)
            bio = bio.split('\n')
        except:
            systemBoarder(sys='error', msg='Could not collet bio')

        try:
            systemBoarder(sys='system', msg='Collecting Name...')
            name = self.driver.find_element(By.XPATH, "//span[@class='x1lliihq x1plvlek xryxfnj x1n2onr6 x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp x1s688f x5n08af x10wh9bi x1wdrske x8viiok x18hxmgj']").text
        except:
            systemBoarder(sys='error', msg='Could not collect name')
        
        try:
            systemBoarder(sys='system', msg='Getting profile picture...')
            imageUrl = self.driver.find_element(By.XPATH, '//img[@class="_aadp"]').get_attribute('src')
        except:
            systemBoarder(sys='error', msg='Could not get image url')


        try:
            print(f'\n\n\t Username     Posts    Flwrs    Flwng')
            print(f'\n\t{self.username}\t{postCount}\t{followerCount}\t{followingCount}')
            print(f'Name\t{name}')
            print(f'Bio', end='')
            for line in bio:
                print(f'\t{line}')
            print(f'\nProfile pic url')
            print(f'\n{imageUrl}')
        except:
            pass

    def get_your_followers(self):
        try:
            systemBoarder(sys='SYSTEM', msg='Loading followers...')
            self.driver.get(f"https://www.instagram.com/{self.username}/followers/")
            
            systemBoarder(sys='SYSTEM', msg='Waiting...')
            wait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Remove']")))
            
            systemBoarder(sys='SYSTEM', msg='Scrolling...')
            numScrolls = 20
            for _ in range(numScrolls):     #Not in frame!!!
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                
            
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #problem here
        except:
            systemBoarder(sys='ERROR', msg='Could not find')
          

    def get_your_following(self):
        return
    
### TARGET ACTIONS ###  

    def get_target_info(self, target):
        systemBoarder(sys='system', msg='Loading target...')        #handle user not found
        try:
            systemBoarder(sys='SYSTEM', msg='Loading followers...')                  #print 
            self.driver.get(f"https://www.instagram.com/{target}/")           #try loading url of username
            time.sleep(5)
        except:
            systemBoarder(sys='ERROR', msg='Could not load profile')                 #if failed print
          
        
        systemBoarder(sys='SYSTEM', msg='Collecting data...')                        #print start sequence

        
        try:
            systemBoarder(sys='SYSTEM', msg='Collecting post count...')
            postCount = self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > section:nth-child(1) > main:nth-child(1) > div:nth-child(1) > header:nth-child(1) > section:nth-child(2) > ul:nth-child(3) > li:nth-child(1) > span:nth-child(1) > span:nth-child(1)").text
            #print(f'Num Posts: {postCount}') #error here
        except:
            systemBoarder(sys="error", msg="Could not find post count")

        try:
            systemBoarder(sys='SYSTEM', msg='Collecting follower count...')
            followerCount = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[2]/a[1]/span[1]/span[1]").text
            #followerCount = wait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#mount_0_0_0l > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > header > section > ul > li:nth-child(2) > a > span"))).title
            #print(f'Followers: {followerCount}')
        except:
            systemBoarder(sys="error", msg="Could not find follower count")

        try:    
            systemBoarder(sys='SYSTEM', msg='Collecting following count...')
            followingCount = self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(3) a:nth-child(1) span:nth-child(1) span:nth-child(1)").text
            #followingCount = wait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#mount_0_0_0l > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > div:nth-child(2) > section > main > div > header > section > ul > li:nth-child(3) > a > span > span"))).text
            #print(f'Following: {followingCount}')
        except:
            systemBoarder(sys='error', msg='Could not find following count')

        try:
            systemBoarder(sys='system', msg='Collecting bio...')            
            bio = self.driver.find_element(By.CSS_SELECTOR, "._aacl._aaco._aacu._aacx._aad6._aade").text     #Get bio, must parse (contains new line chars)
            bio = bio.split('\n')
        except:
            systemBoarder(sys='error', msg='Could not collet bio')

        try:
            systemBoarder(sys='system', msg='Collecting Name...')
            name = self.driver.find_element(By.CSS_SELECTOR, "").text
        except:
            systemBoarder(sys='error', msg='Could not collect name')
        
        try:
            systemBoarder(sys='system', msg='Getting profile picture...')
            imageUrl = self.driver.find_element(By.XPATH, '//img').get_attribute('src')
            #//img        
        except:
            systemBoarder(sys='error', msg='Could not get image url')


        try:
            systemBoarder(sys='system',msg='Getting profile link...')
            profileUrl = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[3]/div[3]/a/span/span").get_attribute('src')
        except:
            systemBoarder(sys="error", msg="Could not get profile link")


        #OUT PUT
        try:
            print(f'\n\n\t Username     Posts    Flwrs    Flwng')
            print(f'\n\t{target}\t{postCount}\t{followerCount}\t{followingCount}')
        except:
            print(f'null') 
        
        try:                            #if user does not have username
            print(f'Name\t{name}')
        except:
            print(f'Name\tnull')

        try:
            print(f'Bio', end='')
            for line in bio:
                print(f'\t{line}')
        except:
            pass 

        try:
            print(f'\nProfile link')
            print(f'\n{profileUrl}')
        except:
            print(f'null')

        try:
            print(f'\nProfile pic url')
            print(f'\n{imageUrl}')
        except:
            print(f'null')

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
                systemBoarder(sys='system', msg='Saving cookies...')        #print
                cookies = self.driver.get_cookies()                         #save cookies
            except:
                systemBoarder(sys='error', msg='Could not save cookies')    #print

            try:
                systemBoarder(sys='SYSTEM',msg='Quiting selenium...')       #print
                self.driver.quit()                                          #quit selenium     
            except: 
                systemBoarder(sys='error', msg='Could not quit selenium')   #Print error

            try:
                systemBoarder(sys='system', msg='Stuffing cookies...')
                with open('..\\reasources\\cookies.pkl', 'wb') as file:                     #open cookie file
                    pk.dump(cookies, file)                                                  #dump cookies
                systemBoarder(sys='system', msg='Cookies stuffed...')
            except:
                systemBoarder(sys='error', msg='Could not save cookies')


            print() #Begin save login sequence
            if str(input(f'Save login locally? (y/n): ')).upper() == 'Y':                   #Ask save login
                print()
                try:
                    systemBoarder(sys='system', msg='Looking for savedLogins.txt...')          #Begin save sequence
                    logins = []
                    with open('..\\reasources\\savedLogins.txt', 'r' ) as file:             #Collect already saved logins (Better way to do this?)
                        for line in file:
                            systemBoarder(sys='system', msg='Found savedLogins.txt!')
                
                            logins.append(line.strip("\n"))                                       #Save saves                                              
                    
                    systemBoarder(sys='system', msg='creating concatonating login...')
                    full = self.username + " " + self.password
                    
                    systemBoarder(sys='system', msg='Checking if login exists...')
                    loginExists = False
                    for login in logins:
                        if login == full:
                            loginExists = True
                            break 

                    if loginExists == False:
                        systemBoarder(sys='system', msg='opening savedLogins.txt...')
                        with open('..\\reasources\\savedLogins.txt', 'a') as file:
                            systemBoarder(sys='system', msg='adding to savedLogins.txt...')
                            file.write('\n')
                            file.write(f'{self.username} {self.password}')
                
                except:
                    systemBoarder(sys='error', msg='savedLogins.txt not found')             #Print Error could not find login file
                    systemBoarder(sys='system', msg='Creating savedLogins.txt...')

                    with open('..\\reasources\\savedLogins.txt', 'w') as file:              #Create new login file
                        file.write(f'{self.username} {self.password}')
                    systemBoarder(sys='system', msg='Saved login')        
            print()
            systemBoarder(sys='SYSTEM',msg='Quiting...')
            sys.exit()

def getTitle(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    span_element = soup.find('span', {'title': True})
    title = span_element['title']
    return title