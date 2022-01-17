#Main
from threading import Thread
from xss import XssScanner
import argparse

def _run(url, wordlist):

    methode = 'get'
    thread = 2
    proxy = False
    lunch = XssScanner(url, wordlist, methode, proxy)
    lunch.run()

def __main():
    parser = argparse.ArgumentParser()
    parser.add_argument("link", help='URL type is https://link.com/?data=')
    parser.add_argument("wordlist", help='Choose a correct WordList link')
    
    #parser.add_argument("-w", "--wordlist", help='Payload list to look for XSS vulnerabilities')
    args = parser.parse_args()
    if not args.link:
        sleep(0.5)
        parser.error("Please use --help for more information")
    elif not args.wordlist:
        sleep(0.5)
        parser.error("Please use --help for more information")
    return args


print(" _   _     _       _       _   _                  _ _       _     \n| |_| |__ (_)___  (_)___  | |_| |__   ___    __ _(_| |_ ___| |__  \n| __| '_ \| / __| | / __| | __| '_ \ / _ \  / _` | | __/ __| '_ \ \n| |_| | | | \__ \ | \__ \ | |_| | | |  __/ | (_| | | || (__| | | |\n \__|_| |_|_|___/ |_|___/  \__|_| |_|\___|  \__, |_|\__\___|_| |_|\n                                            |___/                 \n")
if __name__ == '__main__':
    print('With run use\n\npython3 ./main.py http://yoururl.com/&url?= files/wordlist/xss.txt\n')

    parse = __main()
    _run(parse.link, parse.wordlist)
    
