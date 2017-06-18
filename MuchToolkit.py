#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MuchToolkit 0.2
Dogecoin Toolkit
Dylan Hamer 2017
"""

import sys
import click                      # Make beautiful interfaces
from coinmarketcap import Market  # Get market info

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
price             | Get price
usdprice          | Get price in USD
btcprice          | Get price in BTC
rank              | Get rank
supply            | Get total supply
refresh           | Refresh Coinmarketcap data
exit              | Exit MuchToolkit\n"""

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
    click.echo("MuchToolkit 0.2 by Dylan Hamer\n")
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
            if len(actualCommand) == 1:
                address = input("Please enter a valid Dogecoin address: ")
            else:
                address = actualCommand[1]
            click.launch("http://www.dogechain.info/address/"+address)
        elif command == "price":
            click.echo("Price is: Ð1 = "+click.style("Ð1",fg="green"))
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
            sys.exit()
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
