#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MuchToolkit 0.4 Beta
Dogecoin Toolkit
Dylan Hamer 2017
Felix Zactor 2017
"""

import click                      # Make beautiful interfaces
import muchascii                  # ASCII art
import random                     # Random choices
from coinmarketcap import Market  # Get market info
import pyqrcode                   # Make QR Codes
import os                         # Checks to see if files exists

"""Choose an ASCII art graphic and a color"""
graphic  = muchascii.get(random.choice(["moon", "rocket", "doge"]))
color = random.choice(["red", "green", "yellow", "blue"])

"""Help text"""
help="""\nList of commands:
______________________________________________
licenses          | Show open source licenses
help              | Show this message
version           | Get current version
exit              | Exit the application
genqr             | Generate a QR code
blockchain        | Open dogechain.info
address <address> | Explore an address
usdprice          | Get price in USD
btcprice          | Get price in BTC
rank              | Get rank
supply            | Get total supply
refresh           | Refresh Coinmarketcap data
reddit            | Open the offical Dogecoin reddit\n"""

"""Open source licenses"""
licenses="""\nOpen source licenses:
______________________________________________
Coinmarketcap:
Copyright 2014-2017 Martin Simon

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   https://www.apache.org/licenses/LICENSE-2.0

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
"""

"""Coinmarketcap wrapper"""
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

"""QR code generator: will implement this in the next version"""
def generateQR(data):
    qrcode = pyqrcode.create(data)
    if os.path.isfile("QRcode.svg") == True:
        click.secho("[Much Error!]", nl=False, fg="red", blink=True)
        click.secho("Please move the existing QR code!", bold=True)
    else:
        qrcode.svg("QRCode.svg", scale=8)
        click.secho("QRCode created as ", nl=False)
        click.secho("QRCode.svg", blink=True)

"""ASCII art and text on startup"""
def greeting():
    click.clear()
    click.secho(graphic, fg=color, bold=True)
    click.echo("MuchToolkit 0.4 Beta by Dylan Hamer and Felix Zactor\n")
    click.secho("Donations Welcome: ")
    click.secho("Dylan Hamer:  ", nl=False)
    click.secho("DFUjFKtfRKCJGoo62jzzS6tUZnyTqxMHEV", fg="green")
    click.secho("Felix Zactor: ", nl=False)
    click.secho("DJZjvKAjT838eLo4jTtuCLWm63yLx2Z3x2", fg="green")
    click.secho("Socks for the homeless: ", nl=False)
    click.secho("9vnaTWu71XWimFCW3hctSxryQgYg7rRZ7y", fg="blue")
    click.secho("Dogecoin Reddit:")
    click.secho("https://reddit.com/r/dogecoin", fg="yellow")
    click.echo()

"""Command menu"""
def menu(coinmarketcap):
    click.echo("Type a command or \'help\' for more information")
    while True:
        click.secho(">>> ", fg=color, nl=False, blink=True) 
        command=input()
        actualCommand = command
        command = command.lower()
        if command == "help":
            click.echo(help)
        elif command == "version":
            click.secho("MuchToolkit 0.4", fg="green")
        elif command == "clear":
            click.clear()
            greeting()
        elif command[0:5] == "genqr":
            data = command[6:len(command)]
            generateQR(data)
        elif command == "blockchain":
            click.launch("https://www.dogechain.info")
        elif "address" in command:
            actualCommand = actualCommand.split(" ")
            if len(actualCommand) == 1:
                address = input("Please enter a valid Dogecoin address: ")
            else:
                address = actualCommand[1]
            click.launch("https://www.dogechain.info/address/"+address)
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
        elif command == "licenses":
            click.echo(licenses)
        elif command == "reddit":
            click.launch("https://www.reddit.com/r/dogecoin")
        elif command == "exit":
            click.clear()
            click.secho("Very exit!", fg="green")
            exit(0)
        elif command == "":
            pass    
        else:
            click.secho("[Much Error!] Command not found!", fg="red", blink=True)


def main():  
    coinmarketcap = coinMarketCap()
    greeting()
    menu(coinmarketcap)

if __name__ == "__main__": 
    main()
