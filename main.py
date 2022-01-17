#Main
from threading import Thread
from xss import XssScanner
def __main():
    url = 'http://localhost/xsstest.php?q=' 
    wordlist = "wordlist/low.txt"
    methode = 'get'
    thread = 2
    lunch = XssScanner(url, wordlist, methode)
    lunch.run()
print(" _   _     _       _       _   _                  _ _       _     \n| |_| |__ (_)___  (_)___  | |_| |__   ___    __ _(_| |_ ___| |__  \n| __| '_ \| / __| | / __| | __| '_ \ / _ \  / _` | | __/ __| '_ \ \n| |_| | | | \__ \ | \__ \ | |_| | | |  __/ | (_| | | || (__| | | |\n \__|_| |_|_|___/ |_|___/  \__|_| |_|\___|  \__, |_|\__\___|_| |_|\n                                            |___/                 \n")
__main()