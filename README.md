## XSS-Scanner
Simple XSS HTTP/S scanner without proxy, it can scan dom or any other script. <br>I used Selenium to develop this software, it launches a browser in the background and returns the result to you, the script is waiting to receive an alert(). <br>So you can use any wordlist for AngularJS, Electron etc.<br><br>

<br>
> Setting: 
If you are using Windows you need to change the webdriver : <br>
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/<br>
You must change the direction of the file in xss.py<br>

     ```py
    self.driver = webdriver.Firefox(executable_path="files/driver/geckodriver", options=sets)
    ```
You must also change the url and link of the word list in main.xss<br>
      ```py
    url = 'http://localhost/xsstest.php?q=' 
    wordlist = "wordlist/low.txt"
    ```
<br><br>
Simple XSS Scanner HTTP/HTTPS with Selenium, actualy just GET methode.<br><br>

> Xss Simple Detected
<a href='https://postimg.cc/PPSTvjzg' target='_blank'><img src='https://i.postimg.cc/6pX3S67p/Capture-d-cran-2022-01-17-17-30-15.png' border='0' alt=''/></a><br><br>

> Xss Dom Detected
<a href='https://postimg.cc/wtq61jSY' target='_blank'><img src='https://i.postimg.cc/bvbdFGgr/xssssssss.png' border='0' alt='xssssssss'/></a>

<br><br>
