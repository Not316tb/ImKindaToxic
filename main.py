'''

If you steal my code your dumb

Made by (Not)316tb

'''



import os
import bs4
import time
import replit
import socket
import requests
import colorama
import platform
import webbrowser
import subprocess
import urllib.error
import urllib.parse
import urllib.request
import urllib.response
import urllib.robotparser
import sys
import time
import json
import random
from time import sleep
from random import randint
from subprocess import call
from bs4 import BeautifulSoup
from termcolor import colored
from requests.exceptions import ConnectionError

speed = 0.05

def genStr(words):
  for char in words:
    sleep(speed)
    sys.stdout.write(char)
    sys.stdout.flush()

colorama.init()
os.system('color')
colors = ["red", "yellow"]
txt = open("./stuff/splashes", "r")
helpList = [("\tipdox" + colored("\n\t   Syntax: ", "cyan") + colored("ipdox [ipv4 address]","white") + colored("\n\t   Description: ", "cyan") + colored("Gets geolocation of a given IPv4 address, along with ASN, ISP, and DNS.","white")) ]

version = "1.8.0"
vtype = "BETA"

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
                print(colored("Pinged ", "white") + host + colored(" with 56 bytes of data with a response time of ", "white") + colored(str(responseTime), responseColor) + colored("ms", "white"))
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
        page = requests.get(website)
        soup = BeautifulSoup(page.content, "html.parser")
    except:
        print(colored("\n An error has occured when trying to run 'scrape " +
                      location + " " + simp + "': \n\tError 404, Location not found.\n", "red"))
        return False

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
        print(colored('\n Title: ', "cyan"), colored('%s' % title, "white"))
        if description is None:
            print(colored(' Description: ', "blue"), colored('Failed', "white"))
        elif description is not None:
            print(colored(' Description: ', "blue"), colored(
                '%s' % description["content"], "white"))
        print()
        return True

    elif simp == "text":
        print(colored("\n " + text, "white"))
        print()
        return True

    elif simp == "raw":
        print(colored("\n " + str(soup), "white"))
        print()
        return True

def geolookup(addr):

    genStr("\nFetching...\n")

    request = json.loads(requests.get("https://tools.keycdn.com/geo.json?host=" + addr, headers={"User-Agent": "keycdn-tools:https://www.316tb.dev/"}).content)

    if (request["description"] == "Hostname did not resolve any IP."):
        return False

    returnData = request["data"]["geo"]
    dataColors = {"city": "green", "postal_code": "green","metro_code": "green","region": "green","country": "green","continent": "green","timezone": "green","asn": "green","isp": "green","dns": "green", "latitude": "blue","longitude": "cyan"}

    if (not returnData["postal_code"]):
        returnData["postal_code"] = "Failed"
        dataColors["postal_code"] = "red"

    if (not returnData["metro_code"]):
        returnData["metro_code"] = "Failed"
        dataColors["metro_code"] = "red"

    if (not returnData["region_name"]):
        returnData["region_name"] = "Failed"
        returnData["region_code"] = ""
        dataColors["region"] = "red"

    if (not returnData["country_name"]):
        returnData["country_name"] = "Failed"
        returnData["country_code"] = ""
        dataColors["country"] = "red"

    if (not returnData["continent_name"]):
        returnData["continent_name"] = "Failed"
        returnData["continent_code"] = ""
        dataColors["continent"] = "red"

    if (not returnData["timezone"]):
        returnData["timezone"] = "Failed"
        dataColors["timezone"] = "red"

    if (not returnData["latitude"]):
        returnData["latitude"] = "Failed"
        returnData["longitude"] = "Failed"
        dataColors["latitude"] = "red"
        dataColors["longitude"] = "red"

    if (not returnData["asn"]):
        returnData["asn"] = "Failed"
        dataColors["asn"] = "red"

    if (not returnData["isp"]):
        returnData["isp"] = "Failed"
        dataColors["isp"] = "red"

    if (not returnData["rdns"]):
        returnData["rdns"] = "Failed"
        dataColors["dns"] = "red"
    
    print ("\n ====================[316]====================")
    print ()
    print (colored(" Returned Geo-Data for host ", "white") + colored(returnData["host"], "cyan") + colored(".", "white"))
    print ()
    print (" ===================[I.K.T]===================")
    print (colored(" City: ", "white") + colored(returnData["city"], dataColors["city"]))
    print (colored(" Zip Code: ", "white") + colored(returnData["postal_code"], dataColors["postal_code"]))
    print (colored(" Metro Code: ", "white") + colored(returnData["metro_code"], dataColors["metro_code"]))
    print (colored(" Providence: ", "white") + colored(returnData["region_name"] + " (" + returnData["region_code"] + ") ", dataColors["region"]))
    print (colored(" Country: ", "white") + colored(returnData["country_name"] + " (" + returnData["country_code"] + ") ", dataColors["country"]))
    print (colored(" Continent: ", "white") + colored(returnData["continent_name"] + " (" + returnData["continent_code"] + ") ", dataColors["continent"]))
    print (colored(" Time-Zone: ", "white") + colored(returnData["timezone"].replace("_", " "), dataColors["timezone"]))
    print (colored(" Approx. Coords: ", "white") + colored(returnData["latitude"], dataColors["latitude"]) + colored(",", "white") + colored(returnData["longitude"], dataColors["longitude"]))
    print (" ====================[316]====================")
    print ()
    print (colored(" Returned Misc Data for host ", "white") + colored(returnData["host"], "cyan") + colored(".", "white"))
    print ()
    print (" ===================[I.K.T]===================")
    print (colored(" ASN: ", "white") + colored(returnData["asn"], dataColors["asn"]))
    print (colored(" ISP: ", "white") + colored(returnData["isp"], dataColors["isp"]))
    print (colored(" DNS: ", "white") + colored(returnData["rdns"], dataColors["dns"]))
    print (" ====================[316]====================")

    return True

def iplookup(addr):

    init()

    print(colored("\n Parameters ", "blue"))
    print(colored("\n     1) IP Address: ", "blue") + colored(addr, "yellow"))

    print(colored("\n     97) Execute", "blue"))
    print(colored("     98) Cancel", "blue"))
    print(colored("     99) Exit", "blue"))
    print("\n")

    print(colored(" ┌─[ ", "blue") + colored("ImKindaToxic", "red", attrs=["bold"]) + colored(" ]──[", "blue") + colored("~", "red", attrs=["bold"]) + colored("]─[", "blue") + colored("IP Lookup", "yellow", attrs=["bold"]) + colored(']', "blue"))

    param = int(input(colored(" └─────► ", "blue")))

    if (param == 1):
        init()
    
        print(colored("\n Parameters ", "blue"))
        print(colored("\n     1) IP Address: ", "blue") + colored(addr, "yellow") + colored("[ ", "blue") + colored("SELECTED", "cyan") + colored(" ]", "blue"))
        print(colored("\n     97) Execute", "grey"))
        print(colored("     98) Cancel", "grey"))
        print(colored("     99) Exit", "grey"))
        print("\n")

        print(colored(" ┌─[ ", "blue") + colored("ImKindaToxic", "red", attrs=["bold"]) + colored(" ]──[", "blue") + colored("~", "red", attrs=["bold"]) + colored("]─[", "blue") + colored("IP Address", "yellow", attrs=["bold"]) + colored(']', "blue"))

        param = str(input(colored(" └─────► ", "blue")))

        iplookup(param)
    
    elif (param == 97):
        if (addr == ""):
            replit.clear()
            print(colored("IP Address cannot be null.", "red"))
            time.sleep(2.25)
            iplookup("")
        
        else:
            if geolookup(addr) == True:
                input("Press enter to continue.")
                iplookup(addr)

            else:
                replit.clear()
                print(colored("Please enter a valid IP Address.", "red"))
                time.sleep(2.25)
                iplookup(addr)

    elif (param == 98):
        loadMenu("sniffing")
        main()
    
    elif (param == 99):
        exit()

def wbspider(url, simp):

    init()

    print(colored("\n Parameters ", "blue"))
    print(colored("\n     1) Url / Domain Name: ", "blue") + colored(url, "yellow"))
    print(colored("     2) Filtering: ", "blue") + colored(simp, "yellow"))

    print(colored("\n     97) Execute", "blue"))
    print(colored("     98) Cancel", "blue"))
    print(colored("     99) Exit", "blue"))
    print("\n")

    print(colored(" ┌─[ ", "blue") + colored("ImKindaToxic", "red", attrs=["bold"]) + colored(" ]──[", "blue") + colored("~", "red", attrs=["bold"]) + colored("]─[", "blue") + colored("IP Lookup", "yellow", attrs=["bold"]) + colored(']', "blue"))

    param = int(input(colored(" └─────► ", "blue")))

    if (param == 1):
        init()
    
        print(colored("\n Parameters ", "blue"))
        print(colored("\n     1) IP Address: ", "blue") + colored(url, "yellow") + colored("[ ", "blue") + colored("SELECTED", "cyan") + colored(" ]", "blue"))
        print(colored("\n     97) Execute", "grey"))
        print(colored("     98) Cancel", "grey"))
        print(colored("     99) Exit", "grey"))
        print("\n")

        print(colored(" ┌─[ ", "blue") + colored("ImKindaToxic", "red", attrs=["bold"]) + colored(" ]──[", "blue") + colored("~", "red", attrs=["bold"]) + colored("]─[", "blue") + colored("Url / Domain Name", "yellow", attrs=["bold"]) + colored(']', "blue"))

        param = str(input(colored(" └─────► ", "blue")))

        iplookup(param)

    if (param == 2):
        init()
    
        print(colored("\n Parameters ", "blue"))
        print(colored("\n     1) IP Address: ", "blue") + colored(url, "yellow"))
        print(colored("     2) Filtering: ", "blue") + colored(simp, "yellow") + colored("[ ", "blue") + colored("SELECTED", "cyan") + colored(" ]", "blue"))
        print(colored("\n     97) Execute", "grey"))
        print(colored("     98) Cancel", "grey"))
        print(colored("     99) Exit", "grey"))
        print("\n")

        print(colored(" ┌─[ ", "blue") + colored("ImKindaToxic", "red", attrs=["bold"]) + colored(" ]──[", "blue") + colored("~", "red", attrs=["bold"]) + colored("]─[", "blue") + colored("Filtering", "yellow", attrs=["bold"]) + colored(']', "blue"))

        param = str(input(colored(" └─────► ", "blue")))

        iplookup(param)
    
    elif (param == 97):
        if (url == ""):
            replit.clear()
            print(colored("IP Address cannot be null.", "red"))
            time.sleep(2.25)
            iplookup("")
        
        else:
            if geolookup(url) == True:
                input("Press enter to continue.")
                iplookup(url)

            else:
                replit.clear()
                print(colored("Please enter a valid IP Address.", "red"))
                time.sleep(2.25)
                iplookup(url)

    elif (param == 98):
        loadMenu("sniffing")
        main()
    
    elif (param == 99):
        exit()


def init():
    replit.clear()
    print("\n")
    print(colored(splashes[splash], colors[splash]))
    print("\n")
    print("\n")
    print(colored("[---]             ImKindaToxic Exploit (", "blue") + colored("IKTe", "yellow") + colored(")             [---]", "blue"))
    print(colored("[---]                Created by:  ", "blue") + colored("Not316tb", "yellow") + colored("                [---]", "blue"))
    print(colored("                    Version: ", "blue") + colored(version, "red") + colored(" (", "blue") + colored(vtype, "yellow") + colored(")", "blue")                    )
    print(colored("                       Codename: '", "blue") + colored("Agave", "yellow") + colored("'", "blue")                       )
    print(colored("[---]                  GitHub:  ", "blue") + colored("Not316tb", "magenta") + colored("                  [---]", "blue"))
    print(colored("[---]               Discord:  ", "blue") + colored("Not316tb#1727", "magenta") + colored("               [---]", "blue"))
    print(colored("[---]           Website: ", "blue") + colored("https://www.316tb.dev/", "magenta") + colored("           [---]", "blue"))
    print("\n")
    print(colored("                           [ = = = ]                           ", "blue"))
    print("\n")
    print(colored("          Welcome to the ImKindaToxic Exploit (IKTe).          ", "cyan"))
    print(colored("               'The last hack you'll ever need.'               ", "cyan"))
    print("\n")
    print(colored("            ImKindaToxic was developed by Not316tb             ", "cyan", attrs=["bold"]))
    print("\n")
    print(colored("             Visit https://www.316tb.dev/for more             \n", "cyan", attrs=["bold"]))

def loadTerminal(flags = [""]):

    try:

        if flags[0] == "ipdox":
            try:

                if len(flags) < 2:
                    print(colored("\nAn error has occured when running '" + ' '.join(flags) + "':", "red"))
                    print(colored("\tInvalid Syntax.\n", "red"))
                    loadTerminal()


                if geolookup(flags[1]) == False:
                    print(colored("\nAn error has occured when running '" + ' '.join(flags) + "':", "red"))
                    print(colored("\tPlease enter a valid IP Address.\n", "red")) 
                    loadTerminal()
                
                else:
                    print()
                    loadTerminal()

            except:
                print(colored("\nAn error has occured when running '" + ' '.join(flags) + "':", "red"))
                print(colored("\tError Unknown.\n", "red"))
                loadTerminal()

        elif flags[0] == "error":
            print("\n\t" + colored(flags[1], "red") + "\n")

        elif flags[0] == "clear":
            replit.clear()
            loadTerminal()

        elif flags[0] == "exit":
            
            ecode = 0

            if len(flags) > 2:
                ecode = flags[1];

            exit(ecode)

        elif flags[0] == "scrape":
            if scrape(flags[1], flags[2]) == True:
                loadTerminal()
            
            else:
                loadTerminal()
            
        elif flags[0] == "help":
            for cmd in helpList:
                print(helpList[cmd])

        #else:
        #    try:
        #        call(flags)
        #    except FileNotFoundError:
        #        print()                

        print(colored(" ┌─[ ", "blue") + colored("ImKindaToxic", "red", attrs=["bold"]) + colored(" ]──[", "blue") + colored("#", "green", attrs=["bold"]) + colored("]─[", "blue") + colored("console", "yellow", attrs=["bold"]) + colored(']', "blue"))

        task = input(colored(" └─────► ", "blue"))

        args = task.split(' ')
        
        if args[0] == "ipdox":
            try:

                if len(args) < 2:
                    print(colored("\nAn error has occured when running '" + ' '.join(args) + "':", "red"))
                    print(colored("\tInvalid Syntax.\n", "red"))
                    loadTerminal()

                if geolookup(args[1]) == False:
                    print(colored("\nAn error has occured when running '" + ' '.join(args) + "':", "red"))
                    print(colored("\tPlease enter a valid IP Address.\n", "red")) 
                    loadTerminal()
                
                else:
                    print()
                    loadTerminal()

            except Exception as err:
                print(colored("\nAn error has occured when running '" + ' '.join(args) + "':", "red"))
                print(colored("\tError Unknown.\n", "red"))
                loadTerminal()

        elif args[0] == "clear":
            replit.clear()
            loadTerminal()

        elif args[0] == "exit":
            
            ecode = 0

            if len(args) > 2:
                ecode = args[1];

            exit(ecode)

        elif args[0] == "scrape":
            try:
                if scrape(args[1], args[2]) == True:
                    loadTerminal()

                else:
                    loadTerminal()
            
            except IndexError:
                loadTerminal(["error", "Invalid Argument(s)"])

        elif args[0] == "help":
            for cmd in helpList:
                print(cmd)
                
            loadTerminal()

        elif args[0] == "leave":
            loadMenu("main")
            main()

        else:
            try:
                call(args)
            
            except FileNotFoundError:
                print(colored("\nAn error has occured when running '" + ' '.join(args) + "':", "red"))
                print(colored("\t                                  .\n", "red"))

    except KeyboardInterrupt:
        print(colored("\n\n\tPlease use ", "red") + colored("exit", "white") + colored(" to exit.", "red"))
        print(colored("\tAlternatively, use ", "red") + colored("leave", "white") + colored(" to return to GUI.\n", "red"))
        loadTerminal()



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
        print(colored("\n     98) Console Mode", "blue"))
        print(colored("     99) Exit", "blue"))
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
    
    elif (task == 98 and current == "main"):
        replit.clear()
        loadTerminal()

    elif (task > 4 and task < 98 and current == "main"):
        loadMenu(current)
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

    elif (task > 5 and task < 99 and current == "attacks"):
        loadMenu(current)
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
    
    elif (task > 5 and task < 99 and current == "defenses"):
        loadMenu(current)
        main()

    #-- Sniffing Menu --#

    elif (task == 1 and current == "sniffing"):
        wbspider("", "")
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
        iplookup("")
        return
    
    elif (task == 7 and current == "sniffing"):
        return

    elif (task == 8 and current == "sniffing"):
        loadMenu("main")
        main()

    elif (task > 4 and task < 99 and current == "sniffing"):
        loadMenu(current)
        main()

    #-- Exit --#

    elif (task == 99):
        exit()

runArgs = sys.argv.copy()

if "-t" in runArgs or "--start-terminal" in runArgs:
    init()
    loadTerminal()

if "-c" in runArgs or "--run-command" in runArgs:
    init()
    runArgs.pop(0)
    runArgs.pop(0)
    loadTerminal(runArgs)

loadMenu("main")
main()
