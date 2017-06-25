#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MuchToolkit 0.5 Beta
Dogecoin Toolkit
Dylan Hamer 2017
"""
doge = [0] #Replace the zero and put the addresses in quotes. Make it look like this:
# addresses = ["DFUjFKtfRKCJGoo62jzzS6tUZnyTqxMHEV", "DJZjvKAjT838eLo4jTtuCLWm63yLx2Z3x2", "9vnaTWu71XWimFCW3hctSxryQgYg7rRZ7y"]
import click                      # Make beautiful interfaces
import muchascii                  # ASCII art
import qrcode                     # Make QR Codes
import random                     # Random choices
from coinmarketcap import Market  # Get market info
import requests                   # For the address script
import json                       # For the address script

# I would like to thank /u/peoplma for this function
def balance(addresses):
    balance = []
    for i in addresses:
        get_address_info = requests.get('https://api.blockcypher.com/v1/doge/main/addrs/'+i+'/full?limit=99999')
        address_info = get_address_info.text
        j_address_info = json.loads(address_info)
        balance.append(j_address_info['balance'])
        return sum(balance)/100000000

"""Tells the program if you can use balance and value commands"""
valid = False
"""Modify this line to change your prompt"""
promptType = ">>> "

"""Choose an ASCII art graphic and a color"""
graphic  = muchascii.randomChoice()
color = random.choice(["red", "green", "yellow", "blue"])

"""Gets your balance"""
if doge[0] != 0:
    dogeBalance = balance(doge)
    valid = True

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
usdprice           | Get price in USD
btcprice           | Get price in BTC
rank               | Get rank
supply             | Get total supply
refresh            | Refresh Coinmarketcap data
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
        dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="USD")[0]
        self.usdprice = dogecoin["price_usd"]
        self.btcprice = dogecoin["price_btc"]
        self.rank = dogecoin["rank"]
        self.supply = dogecoin["total_supply"]
        click.secho("Done", fg="green")

"""QR code generator: will implement this in the next version"""
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
    click.secho("Socks for the homeless: ", nl=False)
    click.secho("9vnaTWu71XWimFCW3hctSxryQgYg7rRZ7y", fg="blue")
    click.secho("Dogecoin QT Developers: ", nl=False)
    click.secho("9x9zSN9vx3Kf9B4ofwzEfWgiqxwBieCNEb", fg="yellow")
    click.echo()

def prompt():
    click.secho(promptType, fg=color, nl=False)
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
        click.secho("[Much Wow!] Opened /r/dogecoin in your browser", fg="green")
        click.launch("http://www.reddit.com/r/dogecoin")
    elif command == "reddit market":
        click.secho("[Much Wow!] Opened /r/dogemarket in your browser", fg="green")
        click.launch("http://www.reddit.com/r/dogemarket")
    elif command == "reddit beg":
        click.secho("[Much Wow!] Opened /r/dogecoinbeg in your browser", fg="green")
        click.launch("http://www.reddit.com/r/dogecoinbeg")
    elif command == "balance":
            if valid:
                click.echo("You have: "+click.style("Ð"+str(balance), fg="green"))
            elif valid == False:
                click.secho("Please add your address(es) to this program!", fg="red", bold=True, blink=True)
    elif command[0:5] == "value":
            command = command[6:len(command)]
            if valid == False:
                click.secho("Please add your address(es) to this program!", fg="red", bold=True, blink=True)
            elif valid:
                if command == "btc":
                    click.echo("You have "+click.style("BTC "+str(float(coinmarketcap.btcprice) * float(balance)))+" in Ðogecoin!")
                elif command == "usd":
                    click.echo("You have "+click.style("$"+str(float(coinmarketcap.usdprice) * float(balance)))+" in Ðogecoin!")
                elif command == "life":
                    click.secho("[such error] You don't have one!", fg="red", blink=True)
                else:
                    click.secho("[such error] Coin not supported!", fg="red", blink=True)
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
    click.secho("Welcome to MuchToolKit! (Release 4)")
    click.secho("Type help to see help information or license to see open source licenses")
    while True:
        commandHandler(prompt(), coinmarketcap)
if __name__ == "__main__":
    main()
