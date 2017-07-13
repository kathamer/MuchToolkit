#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MuchToolkit 0.5 Beta
A simple wrapper for a collection of Dogecoin tools
Dylan Hamer 2017
"""

import click                      # Make beautiful interfaces
import muchascii                  # ASCII art
import qrcode                     # Make QR Codes
import random                     # Random choices
from coinmarketcap import Market  # Get market info

"""Choose an ASCII art graphic and a color"""
graphic  = muchascii.randomChoice()
color = random.choice(["red", "green", "yellow", "blue"])

"""List of projects"""
class projects:
    list = """Dogecoin Socks for the homeless: Type \'project-socks\' to see more.
Doge 4 Family House: Type \'project-family\' to see more."""
    family = {"url":"https://www.reddit.com/r/dogecoin/comments/6es4op/start_up_a_fundraiser_for_families_dealing_with_a/"}
    socks = {"url":"https://www.reddit.com/r/dogecoin/comments/5b1lfw/dogecoin_socks_it_to_the_homeless/"}

"""Help text"""
help="""\nList of commands:
______________________________________________
licenses           | Show open source licenses
help               | Show this message
version            | Get current version
exit               | Exit the application
genqr              | Generate a QR code
blockchain         | Open dogechain.info
address <address>  | Explore an address
usd                | Get price in USD
gbp                | Get price in GBP
btc                | Get price in BTC
change             | Get change over time in %
rank               | Get rank
supply             | Get total supply
refresh            | Refresh Coinmarketcap data
projects           | View a list of community projects
reddit (beg/market)| Open Reddit to a the Dogecoin subreddit\n"""

"""Open source licenses"""
licenses="""\nOpen source licenses:
______________________________________________
Coinmarketcap:
Copyright 2014-2017 Martin Simon

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

QRCode:
Copyright (c) 2011, Lincoln Loop
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the package name nor the names of its contributors may be
      used to endorse or promote products derived from this software without
      specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

ASCII Art samples:
All ASCII art samples were taken from chris.com with the exception of dogecoin.txt
which is the property of felixphew on GitHub.
"""

"""Coinmarketcap wrapper"""
class coinMarketCap:
    def __init__(self):
        click.secho("[*] Getting Coinmarketcap data... ", nl=False)
        coinmarketcap = Market()
        dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="GBP")[0]
        self.usdprice = dogecoin["price_usd"]
        self.gbpprice = dogecoin["price_gbp"]
        self.btcprice = dogecoin["price_btc"]
        self.change1 = dogecoin["percent_change_1h"]
        self.change24 = dogecoin["percent_change_24h"]
        self.change7 = dogecoin["percent_change_7d"]
        self.rank = dogecoin["rank"]
        self.supply = dogecoin["total_supply"]
        click.secho("Done", fg="green")

"""QR code generator"""
def generateQR():
    address = input("Please enter your address: ")
    img = qrcode.make(address)
    click.secho("Saved to: QRCodes/"+address+".jpg", fg="green")
    try:
        img.save("QRCodes/"+address+".jpg")
    except:
        click.secho("[Much Error!] Failed to save file", fg="red")

"""ASCII art and text on startup"""
def greeting():
    click.clear()
    click.secho(graphic, fg=color)
    click.echo("MuchToolKit Release 5 by Dylan Hamer\n")
    click.secho("Donations Welcome:  ", nl=False)
    click.secho("DFUjFKtfRKCJGoo62jzzS6tUZnyTqxMHEV", fg="green")
    click.echo("Type \'projects\' to see a list of community projects'")
    click.echo()

def prompt():
    click.secho(">>> ", fg=color, nl=False)
    command = input()
    return command.lower()

"""Command handler"""
def commandHandler(command, coinmarketcap):
    if command == "help":
        click.echo(help)
    elif command == "version":
        click.secho("MuchToolKit Release 5", fg="green")
    elif command == "clear":
        click.clear()
        greeting()
    elif command == "genqr":
        generateQR()
    elif command == "blockchain":
        click.launch("http://www.dogechain.info")
    elif command == "address":
        address = input("Please enter a valid Dogecoin address: ")
        click.launch("http://www.dogechain.info/address/"+address)
    elif command == "usd":
        click.echo(click.style("$"+coinmarketcap.usdprice,fg="green"))
    elif command == "gbp":
        click.echo(click.style("£"+coinmarketcap.gbpprice,fg="green"))
    elif command == "btc":
        click.echo(click.style("BTC "+coinmarketcap.btcprice, fg="green"))
    elif command == "change":
        if coinmarketcap.change1 > '0':
            click.echo(click.style("+"+coinmarketcap.change1+"%"" in the last hour", fg="green"))
        else:
            click.echo(click.style(coinmarketcap.change1+"%"" in the last hour", fg="red"))
        if coinmarketcap.change7 > '0':
            click.echo(click.style("+"+coinmarketcap.change7+"%"" in the last 7 days", fg="green"))
        else:
            click.echo(click.style(coinmarketcap.change7+"%"" in the last 7 days", fg="red"))
        if coinmarketcap.change24 > '0':
            click.echo(click.style("+"+coinmarketcap.change24+"%"" in the last 24 hours", fg="green"))
        else:
            click.echo(click.style(coinmarketcap.change24+"%"" in the last 24 hours", fg="red"))
    elif command == "rank":
        click.echo("Cryptocurrency rank is: "+click.style("#"+coinmarketcap.rank, fg="green")+" according to Coinmarketcap")
    elif command == "supply":
        click.echo("Coins in circulation: "+click.style("Ð"+coinmarketcap.supply, fg="green"))
    elif command == "refresh":
        coinmarketcap = coinMarketCap()
    elif command == "licenses":
        click.echo(licenses)
    elif command == "projects":
        click.echo(projects.list)
    elif command == "project-family":
        click.secho("[Much Wow!] Opened Doge 4 Family House in your browser", fg="green")
        click.launch(projects.family["url"])
    elif command == "project-socks":
        click.secho("[Much Wow!] Opened Dogecoin Socks for the Homeless in your browser", fg="green")
        click.launch(projects.socks["url"])
    elif command == "reddit":
        click.secho("[Much Wow!] Opened /r/dogecoin in your browser", fg="green")
        click.launch("http://www.reddit.com/r/dogecoin")
    elif command == "reddit market":
        click.secho("[Much Wow!] Opened /r/dogemarket in your browser", fg="green")
        click.launch("http://www.reddit.com/r/dogemarket")
    elif command == "reddit beg":
        click.secho("[Much Wow!] Opened /r/dogecoinbeg in your browser", fg="green")
        click.launch("http://www.reddit.com/r/dogecoinbeg")
    elif command == "exit":
        click.secho("To the moon!", fg="green")
        exit(0)
    elif command == "":
        pass
    else:
        click.secho("[Much Error!] Command not found!", fg="red")

def main():
    coinmarketcap = coinMarketCap()
    greeting()
    click.secho("Welcome to MuchToolKit! (Release 5)")
    click.secho("Type help to see help information or license to see open source licenses")
    while True:
        commandHandler(prompt(), coinmarketcap)
if __name__ == "__main__":
    main()
