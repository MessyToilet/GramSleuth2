# Setting up Enviroment

After cloning the repo, install the python libaries required. Found in requirments.txt

# Setting up Chrome and Selenium

The ChromeWeb driver should not be needed, but if you are getting an error saying its missing; install the proper ChromeWeb driver for your Chrome version

# Proper Code Structure

Variable names should be in camelCase

# Selenium Crash Course

Basic get element methods
Elements can be grabbed by css selector, xpath, class name, name, etc

element = self.driver.find_element(By.CSS_SELECTOR, "CSS_HERE")

Use wait until to make selenium wait for elements to pop up or become aviable

wait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "NAME_HERE")))
