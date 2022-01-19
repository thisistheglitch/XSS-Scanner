from time import sleep
from colorama import Fore
from os import path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import randint
import requests
class XssScanner:
    def __init__(self, url, wordlist, methode, proxy, data):
        if(proxy == False):
            print('No proxy')
        else:
            print('API PROXY SELECTED')

        self.payload = False
        self.methode = methode
        self.wordlist = wordlist
        self.url = url
        self.payloads = ''
        self.datasets = ''
        if self.methode == 'post':
            self.data = tuple(data.split('#'))
            
        print(Fore.GREEN +"Selenium start...")
        

    def close_browser(self):
        print('Close Browser...')
        try:
            self.driver.close()
        except:
            pass
        quit()

    def save_result(self):
        filename = randint(1, 1000000)
        files = open('files/save/'+str(filename)+'_result.txt', "a")
        if self.payloads != False:
            files.write('\nPayload ->'+self.payloads + '\nData ->'+self.datasets+'\n')


        files.write(self.result)
        if self.methode == 'get':
            files.write(str(self.data_result))
        else:
            files.write(str(self.data_result))
        print('File save in files/save/'+str(filename)+'_result.txt')
        files.close()
        self.close_browser()
    def scan(self):
        try:
            WebDriverWait(self.driver, 0).until (EC.alert_is_present())            
            self.detect = self.detect +1
            alert = self.driver.switch_to.alert
            alert.accept()
            if self.methode == 'post':
                print(Fore.GREEN + 'FAILLIBLE  ->'+self.url + '\n')
            else:
                print(Fore.GREEN + 'FAILLIBLE  ->'+self.links)
            if self.methode == 'post':
                if self.payload != False:
                    #print(Fore.GREEN + 'XSS exists in ->'+self.url+ '\n')

                    self.payloads = str(self.payloads) + str(self.payload) + '\n'
                    self.datasets = str(self.datasets) + str(self.dataset) + '\n'
                    #print('Payload ->'+self.payloads + 'Data ->'+self.datasets+'\n')
                    self.data_result.extend([self.url])
            else:
                self.data_result.extend([self.links])
        except TimeoutException:
            if self.methode == 'post':
                print(Fore.WHITE + 'TESTE ->'+self.url + '\n')
            else:
                print(Fore.WHITE+ 'TEST ->'+self.links)

    def lunchWebDriver(self):
        try:    
            sets = webdriver.FirefoxOptions()
            sets.add_argument('--headless')
            self.driver = webdriver.Firefox(executable_path="files/driver/geckodriver", options=sets)
            self.driver.get(self.driver.get(self.url))
            #sleep(4)
        except:
            print("Run")


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
        result = []
        self.lunchWebDriver()

        with open(self.wordlist, 'r') as f:
            for i, line in enumerate(f):
                if self.methode == 'get' or self.methode == 'GET':
                    self.links = self.url.replace('{{inject}}', str(line))
                    try:

                        self.driver.get(self.links)
                        sleep(1)

                    except:
                        print(Fore.RED +'URL ERROR.')
                        self.count = self.count - 1
                        pass
                    sleep(2)
                    self.scan()
                    self.count = self.count +1
                elif self.methode == 'post' or self.methode == 'POST':
                    injected = ''

                    c = 0

                    for o in self.data:
                        rq = tuple(o.split('='))


                        lst = list(rq)
                        self.dataset = lst[0]

                        lst[1] = lst[1].replace('{{inject}}', str(line))
                        self.payload = lst[1]
                        result.append(tuple(lst))                    
                    x = requests.post(self.url, data=result)
                    html_content = x.text 
                    self.driver.get("data:text/html;charset=utf-8,{html_content}".format(html_content=html_content))
                    sleep(2)
                    self.scan()
                    result = []
                    self.payload = False                 
                pass
        print("######SCAN_END####")
        if self.detect >= 1:
            print(Fore.GREEN +'DETECTED\n('+str(self.detect)+'/'+str(self.count)+')')
            self.result = 'URL DETECTED ('+str(self.detect)+'/'+str(self.count)+')\n'
            

            for item in self.data_result:
                print(str(item))
            save = input('Save scan result ?(y/yes)')
            if save == "yes" or save == "y":
                self.save_result()
            else:
                self.close_browser()
            #print(self.data_result)
        else:
            print(Fore.RED+'No XSS detected.')
            self.close_browser()


