import os
import bs4
import time
import replit
import socket
import requests
import colorama
import platform
import webbrowser
import urllib.error
import urllib.parse
import urllib.request
import urllib.response
import urllib.robotparser
import sys
import time
import json
import random
from random import randint
from bs4 import BeautifulSoup
from termcolor import colored
from requests.exceptions import ConnectionError

colorama.init()
os.system('color')
colors = ["red", "yellow"]
txt = open("./stuff/splashes", "r")

version = "1.4.3"

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

def geolookup(addr):
    request = json.loads(requests.get("https://tools.keycdn.com/geo.json?host=69.14.220.130").content)
    returnData = request["data"]["geo"]

    print (colored("Returned Geo-Data for host ", "white") + colored(returnData["host"], "cyan") + colored(".", "white"))
    print ()
    print ("===================[I.K.T]===================")
    print (colored("City: ", "white") + colored(returnData["city"], "green"))
    print (colored("Zip Code: ", "white") + colored(returnData["postal_code"], "green"))
    print (colored("Metro Code: ", "white") + colored(returnData["metro_code"], "green"))
    print (colored("Providence: ", "white") + colored(returnData["region_name"] + " (" + returnData["region_code"] + ") ", "green"))
    print (colored("Country: ", "white") + colored(returnData["country_name"] + " (" + returnData["country_code"] + ") ", "green"))
    print (colored("Continent: ", "white") + colored(returnData["continent_name"] + " (" + returnData["continent_code"] + ") ", "green"))
    print (colored("Time-Zone: ", "white") + colored(returnData["timezone"].replace("_", " "), "green"))
    print (colored("Coordinates: ", "white") + colored(returnData["latitude"], "blue") + colored(",", "white") + colored(returnData["longitude"], "cyan"))
    print ("====================[316]====================")
    print ()
    print (colored("Returned Misc Data for host ", "white") + colored(returnData["host"], "cyan") + colored(".", "white"))
    print ()
    print ("===================[I.K.T]===================")
    print (colored("ASN: ", "white") + colored(returnData["asn"], "green"))
    print (colored("ISP: ", "white") + colored(returnData["isp"], "green"))
    print (colored("DNS: ", "white") + colored(returnData["rdns"], "green"))
    print ("====================[316]====================")

def iplookup():
    init()
    
    print(colored(" ┌─[ ", "blue") + colored("ImKindaToxic", "red", attrs=["bold"]) + colored(" ]──[", "blue") + colored("~", "red", attrs=["bold"]) + colored("]─[", "blue") + colored(current, "yellow", attrs=["bold"]) + colored(']', "blue"))

    task = int(input(colored(" └─────► ", "blue")))

def init():
    replit.clear()
    print("\n")
    print(colored(splashes[splash], colors[splash]))
    print("\n")
    print("\n")
    print(colored("[---]             ImKindaToxic Exploit (", "blue") + colored("IKTe", "yellow") + colored(")             [---]", "blue"))
    print(colored("[---]         Created by: Ronnie Sarrett  (", "blue") + colored("316tb", "yellow") + colored(")         [---]", "blue"))
    print(colored("                    Version: ", "blue") + colored(version, "red") + colored(" (", "blue") + colored("STABLE", "yellow") + colored(")", "blue")                    )
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

        print(colored("\n Select an option from the menu: ", "blue"))
        print(colored("\n     1) Attack Menu", "blue"))
        print(colored("     2) Defense Menu", "blue"))
        print(colored("     3) Sniffing Menu", "blue"))
        print(colored("     4) Config", "blue"))
        print(colored("\n     99) Exit", "blue"))
        print("\n")

    elif (menuName == "attacks"):
        current = "attacks"

        print(colored("\n Select an option from the menu: ", "blue"))
        print(colored("\n     1) ", "blue") + colored("Denial Of Service (", "cyan") + colored("DoS", "yellow") + colored(")", "cyan"))
        print(colored("     2) ", "blue") + colored("Distributed Denial Of Service (", "cyan") + colored("DDoS", "yellow") + colored(")", "cyan"))
        print(colored("     3) ", "blue") + colored("Backdoor Payload (", "cyan") + colored("RAT", "yellow") + colored(")", "cyan"))
        print(colored("     4) Generic Payloads", "blue"))
        print(colored("     5) Main Menu", "blue"))
        print(colored("\n     99) Exit", "blue"))
        print("\n")

    elif (menuName == "defenses"):
        current = "defenses"

        print(colored("\n Select an option from the menu: ", "blue"))
        print(colored("\n     1) ", "blue") + colored("Scramble IP (", "cyan") + colored("Tor", "yellow") + colored(")", "cyan"))
        print(colored("     2) ", "blue") + colored("Hide IP (", "cyan") + colored("Proxy", "yellow") + colored(")", "cyan"))
        print(colored("     3) ", "blue") + colored("Change IP (", "cyan") + colored("LAN", "yellow") + colored(")", "cyan"))
        print(colored("     4) Edit Proxy List", "blue"))
        print(colored("     5) Main Menu", "blue"))
        print(colored("\n     99) Exit", "blue"))
        print("\n")

    elif (menuName == "sniffing"):
        current = "sniffing"

        print(colored("\n Select an option from the menu: ", "blue"))
        print(colored("\n     1) ", "blue") + colored("Web Spider (", "cyan") + colored("bs4", "yellow") + colored(")", "cyan"))
        print(colored("     2) ", "blue") + colored("Network Discovery (", "cyan") + colored("LAN", "yellow") + colored(")", "cyan"))
        print(colored("     3) ", "blue") + colored("WhoIs (", "cyan") + colored("WhoIs", "yellow") + colored(")", "cyan"))
        print(colored("     4) ", "blue") + colored("NsLookup (", "cyan") + colored("NsLookup", "yellow") + colored(")", "cyan"))
        print(colored("     5) ", "blue") + colored("Search (", "cyan") + colored("DuckDuckGo", "yellow") + colored(")", "cyan"))
        print(colored("     6) ", "blue") + colored("Ip-Lookup (", "cyan") + colored("GEO", "yellow") + colored(")", "cyan"))
        print(colored("     7) Edit Proxy List", "blue"))
        print(colored("     8) Main Menu", "blue"))
        print(colored("\n     99) Exit", "blue"))
        print("\n")

def main():
    global task
    global current

    print(colored(" ┌─[ ", "blue") + colored("ImKindaToxic", "red", attrs=["bold"]) + colored(" ]──[", "blue") + colored("~", "red", attrs=["bold"]) + colored("]─[", "blue") + colored(current, "yellow", attrs=["bold"]) + colored(']', "blue"))

    task = int(input(colored(" └─────► ", "blue")))

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

    #-- Defenses Menu --#

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

    #-- Sniffing Menu --#

    elif (task == 1 and current == "sniffing"):
        return

    elif (task == 2 and current == "sniffing"):
        return

    elif (task == 3 and current == "sniffing"):
        return

    elif (task == 4 and current == "sniffing"):
        return

    elif (task == 5 and current == "sniffing"):
        return

    elif (task == 6 and current == "sniffing"):
        iplookup()
        return
    
    elif (task == 7 and current == "sniffing"):
        return

    elif (task == 8 and current == "sniffing"):
        loadMenu("main")
        main()

    #-- Exit --#

    elif (task == 99):
        exit()

loadMenu("main")
main()
