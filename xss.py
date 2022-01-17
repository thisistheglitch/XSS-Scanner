from time import sleep
from colorama import Fore
from os import path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class XssScanner:
    def __init__(self, url, wordlist, methode):
        self.methode = methode
        self.wordlist = wordlist
        self.url = url
        print(Fore.GREEN +"Selenium start...")
        try:    
            sets = webdriver.FirefoxOptions()
            sets.add_argument('--headless')
            self.driver = webdriver.Firefox(executable_path="files/driver/geckodriver", options=sets)
            self.driver.get(self.driver.get(self.url))
            sleep(5)
        except:
            print(Fore.RED +"Error reply.")

    def run(self):
        self.data_result = []
        print(Fore.GREEN +'URL attack : '+self.url+'')
        if path.exists(self.wordlist) == True:
            print(Fore.GREEN +'Wordlist : '+self.wordlist)
        else:
            print(Fore.RED +'Wordlist does not exist : '+self.wordlist)
            quit()
        self.count = 0
        self.detect = 0
        with open(self.wordlist, 'r') as f:
            for i, line in enumerate(f):
                if self.methode == 'get' or self.methode == 'GET':
                    try:
                        self.driver.get(self.url+str(line))
                        sleep(1)

                    except:
                        print(Fore.RED +'URL ERROR.')
                        self.count = self.count - 1
                        pass
                    self.count = self.count +1

                    try:
                        WebDriverWait(self.driver, 0).until (EC.alert_is_present())
                        #WebDriverWait(driver, 5).until (EC.alert_is_present())
                        self.detect = self.detect +1
                        alert = self.driver.switch_to.alert
                        alert.accept()
                        print(Fore.GREEN + 'XSS exists in | '+self.url+str(line)+ 'URL receive --->'+self.driver.current_url+'\n')
                        self.data_result.extend([self.url+str(line)])
                    except TimeoutException:
                        print(Fore.RED + 'No XSS detected | '+self.url+str(line) + 'URL receive --->'+self.driver.current_url+'\n')
                elif self.methode == 'post' or self.methode == 'POST':
                    print('Construct')
                    quit()                    
                pass
        print("######SCAN_END####")
        if self.detect >= 1:
            print(Fore.GREEN +'DETECTED\n('+str(self.detect)+'/'+str(self.count)+')')
            for item in self.data_result:
                print(str(item))

        else:
            print(Fore.RED+'No detected.')


