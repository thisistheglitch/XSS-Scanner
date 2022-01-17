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
            #sets.headless = True

            self.driver = webdriver.Firefox(executable_path="files/driver/geckodriver", options=sets)
            self.driver.get(self.driver.get(self.url))
            #driver.get(driver.get(self.url))
            sleep(5)
        except:
            print(Fore.RED +"Error reply.")

        #self.thread = thread
        #self.simpleTarget = "<script>alert('alert')</script>"cc bjhnk,l;m
        
        #self.detect = []
     
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
                #print(self.url+str(line))
                if self.methode == 'get' or self.methode == 'GET':
                    #Ont vas utilisé Selenium du coup, je veux pouvoir testé la totalité des XSS
                    #Une fois Selenium mis faut rajouter des proxy
                    #url = get(self.url+str(line)).text
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
                    print('Construct')
                    quit()                    
                pass
        print("######SCAN_END####")
        if self.detect >= 1:
            print(Fore.GREEN +'DETECTED\n('+str(self.detect)+'/'+str(self.count)+')')
            for item in self.data_result:
                print(str(item))

            #print(self.data_result)
        else:
            print(Fore.RED+'No detected.')


