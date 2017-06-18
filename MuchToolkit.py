#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MuchToolkit 0.3
Dogecoin Toolkit
Dylan Hamer 2017
Felix Zactor 2017
"""

import click                      # Make beautiful interfaces
from coinmarketcap import Market  # Get market info
import os                         # Give commands to the system
doge="""░░░░░░░░░▄░░░░░░░░░░░░░░▄░░░░ 
░░░░░░░░▌▒█░░░░░░░░░░░▄▀▒▌░░░
░░░░░░░░▌▒▒█░░░░░░░░▄▀▒▒▒▐░░░ 
░░░░░░░▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐░░░
░░░░░▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐░░░
░░░▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌░░░ 
░░▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌░░
░░▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐░░
░▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌░
░▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌░
▀▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐░ 
▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐░
░▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌░
░▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐░░
░░▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌░░
░░░░▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀░░░
░░░░░░▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀░░░░░
░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▀▀░░░░░░░░"""

help="""\nList of commands:
_______________________________________
help              | Show this message
version           | Get current version
genqr             | Generate a QR code
blockchain        | Open dogechain.info
address <address> | Explore an address
usdprice          | Get price in USD
btcprice          | Get price in BTC
rank              | Get rank
supply            | Get total supply
refresh           | Refresh Coinmarketcap data
exit              | Exits MuchToolkit
tousd             | Converts Dogecoin to USD
tobtc             | Converts Dogecoin to BTC\n"""

class coinMarketCap:
    def __init__(self):
        click.secho("[*] Getting Coinmarketcap data... ", nl=False)
        coinmarketcap = Market()
        dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="USD")[0]
        self.usdprice = dogecoin["price_usd"]
        self.btcprice = dogecoin["price_btc"]
        self.rank = dogecoin["rank"]
        self.supply = dogecoin["total_supply"]
        click.secho("Done", fg="green")

def generateQR():
    click.secho("[Much Error!] ", fg="red", nl=False)
    click.echo("I haven't finished this yet ¯\_(ツ)_/¯")
    
def greeting():
    click.clear()    
    click.secho(doge, fg="yellow")
    click.echo("MuchToolkit 0.3 by Dylan Hamer and Felix Zactor\n")
    click.secho("Donations Welcome:  ", nl=False)
    click.secho("DFUjFKtfRKCJGoo62jzzS6tUZnyTqxMHEV", fg="green")
    click.secho("Socks for the homeless: ", nl=False)
    click.secho("9vnaTWu71XWimFCW3hctSxryQgYg7rRZ7y", fg="blue")
    click.echo()

def menu(coinmarketcap):
    click.echo("Type a command or \'help\' for more information")
    while True:
        click.secho("[>] ", fg="yellow", nl=False) 
        command=input()
        actualCommand = command
        command = command.lower()
        if command == "help":
            click.echo(help)
        elif command == "version":
            click.secho("MuchToolkit 0.1", fg="green")
        elif command == "clear":
            click.clear()
            greeting()
        elif command == "genqr":
            generateQR()
        elif command == "blockchain":
            click.launch("http://www.dogechain.info")
        elif "address" in command:
            actualCommand = actualCommand.split(" ")
            if len(actualCommand) != 34 or actualCommand[0] != "A" or "9" or "D":
                address = input("Please enter a valid Dogecoin address: ")
            else:
                address = actualCommand[1]
            click.launch("http://www.dogechain.info/address/"+address)
        elif command == "usdprice":
            click.echo("Price in USD is: "+click.style("$"+coinmarketcap.usdprice,fg="green"))
        elif command == "btcprice":
            click.echo("Price in BTC is: "+click.style("BTC "+coinmarketcap.btcprice, fg="green"))
        elif command == "rank":
            click.echo("Cryptocurrency rank is: "+click.style("#"+coinmarketcap.rank, fg="green")+" according to Coinmarketcap")
        elif command == "supply":
            click.echo("Coins in circulation: "+click.style("Ð"+coinmarketcap.supply, fg="green"))
        elif command == "refresh":
            coinmarketcap = coinMarketCap()
        elif command == "exit":
            os.system("cls" if os.name == 'nt' else "clear")
            exit()
        elif command[0:6] == "tousd ":
            doge = int(command[7:len(command) - 1])
            amount = doge * coinmarketcap.usdprice
            click.echo("$" + amount, fg="green")
        elif command[0:6] == "tobtc ":
            doge = int(command[7:len(command) - 1])
            amount = doge * coinmarketcap.btcprice
            click.echo("BTC " + amount)
        elif command == "":
            pass    
        else:
            click.secho("[Much Error!] Command not found!", fg="red")


def main():
    coinmarketcap = coinMarketCap()
    greeting()
    menu(coinmarketcap)

if __name__ == "__main__": 
    main()
