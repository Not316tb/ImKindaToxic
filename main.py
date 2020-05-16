import os
import bs4
import time
import replit
import socket
import requests
import colorama
import platform
import webbrowser
import pythonping
import urllib.error
import urllib.parse
import urllib.request
import urllib.response
import urllib.robotparser
import sys
import time
import random
from random import randint
from bs4 import BeautifulSoup
from termcolor import colored
from requests.exceptions import ConnectionError

colorama.init()
os.system('color')
colors = ["red", "yellow"]
txt = open("./stuff/splashes", "r")

splashes = txt.read().split("![{BREAK}]")
splash = randint(1, len(splashes)) - 1
current = "main"
task = None

global proxyList
socksList = open("./stuff/socks4.txt", "r")
proxyList = socksList.read().splitlines()

typing_speed = 0.05


def slPrint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(typing_speed)


def Average(lst):
    return sum(lst) / len(lst)


def rage():
    for i in range(100):
        print('A', end="A"),
        time.sleep(1)




def proxy(pType, url):
    global proxyList

    print("\nPinging server...")

    try:
        requests.get("https://www.google.com", proxies={pType: url})
        print(colored("Success!\n", "green"))
        proxyList.update({pType: url})
        time.sleep(0.01)
        print("Connected to proxy server "+pType+"://"+url)
        print()
        main()

    except:
        print(colored("Failed to connect to proxy.\n", "red"))
        main()
        return


def emulate(code, language="html"):
    tmp = open("./tmp/tmp." + language, "w+")

    tmp.write(code)
    tmp.close()
    webbrowser.open('file://tmp.' + language)


def pingServ(host, byteStr, bash):
    global proxyList

    reAver = []
    try:
        try:
            while True:
                if "https://" not in host:
                    host = ("https://%s" % host)
                response = requests.post(
                    host, proxies=proxyList, data=byteStr, timeout=500)
                responseTime = int(
                    round(response.elapsed.total_seconds(), 3) * 1000)

                if responseTime < 150 and not proxyList:
                    responseColor = "green"
                if responseTime >= 150 and not proxyList:
                    responseColor = "red"
                if responseTime < 425 and bool(proxyList):
                    responseColor = "green"
                if responseTime >= 425 and bool(proxyList):
                    responseColor = "red"
                print(colored("Pinged ", "white") + host + colored(" with 56 bytes of data with a response time of ",
                                                                   "white") + colored(str(responseTime), responseColor) + colored("ms", "white"))
                time.sleep(1)
                reAver.append(responseTime)

        except requests.exceptions.TooManyRedirects:
            print(colored("An error has occured when trying to run '" +
                          bash + "': \nError 408, Bad request.\n", "red"))
            main()
        except requests.exceptions.Timeout:
            print(colored("An error has occured when trying to run '" +
                          bash + "': \nError 408, Connection Timeout.\n", "red"))
            main()
        except requests.exceptions.HTTPError as e:
            print(colored("An error has occured when trying to run '" +
                          bash + "': \nError "+e+".\n", "red"))
            main()
        except requests.exceptions.RequestException as er:
            print(colored("Something went wrong when trying to run '" +
                          bash + "' (Double check the URL!) \n", "red"))
            main()

    except KeyboardInterrupt:
        try:
            if round(Average(reAver)) < 150:
                avResponseColor = "green"
            if round(Average(reAver)) >= 150:
                avResponseColor = "red"
            print(colored("\nAverage response time from ", "white") + host + colored(":", "white") +
                  colored(str(round(Average(reAver))), avResponseColor) + colored("ms", "white"))
            main()
        except:
            main()
            return


def respond(content):
    if content == "" or content is None:
        print(colored("Invalid syntax\n", "red"))
        main()
    print(colored(content, "white"))


def scrape(location, simp):
    global proxyList

    website = location
    if "https://" not in website:
        website = ("https://%s" % website)
    try:
        page = requests.get(website, proxies=proxyList)
        soup = BeautifulSoup(page.content, "html.parser")
    except:
        print(colored("An error has occured when trying to run 'scrape " +
                      location + " " + simp + "': \nError 404, Location not found.\n", "red"))
        main()

    title = soup.find("title").text
    description = soup.find(attrs={"name": "description"})
    for script in soup(["script", "style"]):
        script.decompose()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n\n'.join(chunk for chunk in chunks if chunk)
    if simp == "simp":
        print(colored('Title: ', "cyan"), colored('%s' % title, "white"))
        if description is None:
            print(colored('Description: ', "blue"), colored('N/A', "white"))
        elif description is not None:
            print(colored('Description: ', "blue"), colored(
                '%s' % description["content"], "white"))
        print()
        main()

    elif simp == "text":
        print(colored(text, "white"))
        print()
        main()

    elif simp == "raw":
        print(colored(soup, "white"))
        print()
        main()

def init():
    replit.clear()
    print("\n")
    print(colored(splashes[splash], colors[splash]))
    print("\n")
    print("\n")
    print(colored("[---]             ImKindaToxic Exploit (", "blue") + colored("IKTe", "yellow") + colored(")             [---]", "blue"))
    print(colored("[---]         Created by: Ronnie Sarrett  (", "blue") + colored("316tb", "yellow") + colored(")         [---]", "blue"))
    print(colored("                    Version: ", "blue") + colored("0.0.1", "red") + colored(" (", "blue") + colored("STABLE", "yellow") + colored(")", "blue")                    )
    print(colored("                       Codename: '", "blue") + colored("Agave", "yellow") + colored("'", "blue")                       )
    print(colored("[---]                   GitHub: ", "blue") + colored("r-S0316", "magenta") + colored("                   [---]", "blue"))
    print(colored("[---]             Discord: ", "blue") + colored("TheLonelyShoe#1727", "magenta") + colored("             [---]", "blue"))
    print(colored("[---]           Website: ", "blue") + colored("https://www.316tb.dev/", "magenta") + colored("           [---]", "blue"))
    print("\n")
    print(colored("                           [ = = = ]                           ", "blue"))
    print("\n")
    print(colored("          Welcome to the ImKindaToxic Exploit (IKTe).          ", "cyan"))
    print(colored("               'The last hack you'll ever need.'               ", "cyan"))
    print("\n")
    print(colored("         ImKindaToxic was developed by 316tb (r-S0316)         ", "cyan", attrs=["bold"]))
    print("\n")
    print(colored("             Visit https://www.316tb.net/ for more             \n", "cyan", attrs=["bold"]))

def loadMenu(menuName):
    init()

    global current

    if (menuName == "main"):
        current = "main"

        print("\n Select an option from the menu: ")
        print("\n     1) Attack Menu")
        print("     2) Defense Menu")
        print("     3) Sniffing Menu")
        print("     4) Config")
        print("\n     99) Exit")
        print("\n")

    elif (menuName == "attacks"):
        current = "attacks"

        print("\n Select an option from the menu: ")
        print("\n     1) " + colored("Denial Of Service (", "green") + colored("DoS", "yellow") + colored(")", "green"))
        print("     2) " + colored("Distributed Denial Of Service (", "green") + colored("DDoS", "yellow") + colored(")", "green"))
        print("     3) " + colored("Backdoor Payload (", "green") + colored("RAT", "yellow") + colored(")", "green"))
        print("     4) Generic Payloads")
        print("     5) Main Menu")
        print("\n     99) Exit")
        print("\n")

    elif (menuName == "defenses"):
        current = "defenses"

        print("\n Select an option from the menu: ")
        print("\n     1) " + colored("Scramble IP (", "green") + colored("Tor", "yellow") + colored(")", "green"))
        print("     2) " + colored("Hide IP (", "green") + colored("Proxy", "yellow") + colored(")", "green"))
        print("     3) " + colored("Change IP (", "green") + colored("LAN", "yellow") + colored(")", "green"))
        print("     4) Edit Proxy List")
        print("     5) Main Menu")
        print("\n     99) Exit")
        print("\n")

    elif (menuName == "sniffing"):
        current = "sniffing"

        print("\n Select an option from the menu: ")
        print("\n     1) " + colored("Web Spider (", "green") + colored("bs4", "yellow") + colored(")", "green"))
        print("     2) " + colored("Network Discovery (", "green") + colored("LAN", "yellow") + colored(")", "green"))
        print("     3) " + colored("WhoIs (", "green") + colored("WhoIs", "yellow") + colored(")", "green"))
        print("     4) " + colored("NsLookup (", "green") + colored("NsLookup", "yellow") + colored(")", "green"))
        print("     5) " + colored("Search (", "green") + colored("DuckDuckGo", "yellow") + colored(")", "green"))
        print("     6) Edit Proxy List")
        print("     7) Main Menu")
        print("\n     99) Exit")
        print("\n")

def main():
    global task
    task = int(input(colored("IKTe", "green", attrs=["underline"]) + "> "))

    if (task == 1 and current == "main"):
        loadMenu("attacks")
        main()

    elif (task == 2 and current == "main"):
        loadMenu("defenses")
        main()
    
    elif (task == 3 and current == "main"):
        loadMenu("sniffing")
        main()
    
    elif (task == 4 and current == "main"):
        loadMenu("config")
        main()

    #-- Attacks Menu --#

    elif (task == 1 and current == "attacks"):
        return

    elif (task == 2 and current == "attacks"):
        return

    elif (task == 3 and current == "attacks"):
        return

    elif (task == 4 and current == "attacks"):
        loadMenu("payloads")
        main()

    elif (task == 5 and current == "attacks"):
        loadMenu("main")
        main()

    #-- Defenses Menu

    elif (task == 1 and current == "defenses"):
        return

    elif (task == 2 and current == "defenses"):
        return

    elif (task == 3 and current == "defenses"):
        return

    elif (task == 4 and current == "defenses"):
        loadMenu("payloads")
        main()

    elif (task == 5 and current == "defenses"):
        loadMenu("main")
        main()

    #-- Exit --#

    elif (task == 99):
        exit()

loadMenu("main")
main()
