from time import sleep
from colorama import Fore
from os import path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import randint

class XssScanner:
    def __init__(self, url, wordlist, methode, proxy):
        if(proxy == False):
            print('No proxy')
        elif(proxy == "API"):
            print('API PROXY SELECTED')
            self.proxyon = True
            self.proxy = 'api'
        else:
            print('Proxy true')
            self.proxyon = True
            self.proxy = proxy

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

    def close_browser(self):
        print('Close Browser...')
        self.driver.close()
        quit()

    def save_result(self):
        filename = randint(1, 1000000)
        files = open('files/last_'+str(filename)+'_result.txt', "a")
        files.write(self.result)
        for item in self.data_result:
                files.write(str(item))
        print('File save in files/last_'+str(filename)+'_result.txt')
        files.close()
        self.close_browser()

    def run(self):
        self.data_result = []
        print(Fore.GREEN +'URL attack : '+self.url+'')
        if path.exists(self.wordlist) == True:
            print(Fore.GREEN +'Wordlist : '+self.wordlist)
        else:
            print(Fore.RED +'Wordlist does not exist : '+self.wordlist)
            self.close_browser()
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

                    #print(Fore.GREEN+'GET : '+self.url+str(line))
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
                    print('Method not supported')
                    self.close_browser()                 
                pass
        print("######SCAN_END####")
        if self.detect >= 1:
            print(Fore.GREEN +'DETECTED\n('+str(self.detect)+'/'+str(self.count)+')')
            self.result = 'URL DETECTED ('+str(self.detect)+'/'+str(self.count)+')\n'

            for item in self.data_result:
                print(str(item))
            #self.result = 'URL DETECTED\n '+ str(self.data_result) +'('+str(self.detect)+'/'+str(self.count)+')'
            save = input('Save scan result ?')
            if save == "yes" or save == "y":
                self.save_result()
            else:
                self.close_browser()
            #print(self.data_result)
        else:
            print(Fore.RED+'No XSS detected.')
            self.close_browser()


