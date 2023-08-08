import requests
from bs4 import BeautifulSoup

class bot():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        try:
            response = requests.get("https://www.instagram.com/")
            old = response.text
            if response.status_code == 200:
                print("Website accessed successfully.")
            else:
                print(f"Request failed with status code: {response.status_code}")
            try:
                input_data = {
                    "username": self.username,
                    "password": self.password
                }
                requests.post("https://www.instagram.com/login/", data=input_data)
                response = requests.get("https://www.instagram.com/login/")

            except:
                print(f"Login_error")
        except:
            print(f"Connection_error")

    def get_your_followers(self):
        try:
            response = requests.post(f"https://www.instagram.com/{self.username}/followers/")
        except:
            print(f"Navigation_error")