#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MuchUnofficalToolkit 0.6 Beta
A simple wrapper for a collection of Dogecoin tools
Dylan Hamer and Felix Zactor 2017
"""
import click                      # Make beautiful interfaces
import muchascii                  # ASCII art
import qrcode                     # Make QR Codes
import random                     # Random choices
from coinmarketcap import Market  # Get market info
doge = ["0"] #Replace the 0 with your address(es).
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
if doge[0] != "0":
    balance(doge)
    verify = True
"""Generate colored text"""
def rainbow(text):
    for i in list(text):
      click.secho(i, fg=random.choice(["red", "green", "yellow", "blue"]), nl=False, bold=True)
    print("")
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
price   <currency> | Price of doge in the curreny of your choice
rank               | Get rank
supply             | Get total supply
refresh            | Refresh Coinmarketcap data
reddit (beg/market)| Open Reddit to a the Dogecoin subreddit
value  <currency>  | See the value of your dogecoins
projects           | View a list of community projects
rainbow <text>     | Displays colored text
donate             | Donation Address to Felix Zactor\n"""

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
        rainbow("[*] Getting Coinmarketcap data... ")
        coinmarketcap = Market()
        dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="USD")[0]
        self.usdprice = dogecoin["price_usd"]
        self.btcprice = dogecoin["price_btc"]
        dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="EUR")[0]
        self.usdprice = dogecoin["price_eur"]
        dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="GBP")[0]
        self.usdprice = dogecoin["price_gbp"]
        dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="AUD")[0]
        self.audprice = dogecoin["price_aud"]
        dogecoin = coinmarketcap.ticker("Dogecoin", limit=3, convert="CAD")[0]
        self.cadprice = dogecoin["price_cad"]
        self.rank = dogecoin["rank"]
        self.supply = dogecoin["total_supply"]
        click.secho("Done", fg="green")

"""QR code generator: will implement this in the next version"""
def generateQR(codeFormat):
    address = input("Please enter your address: ")
    if codeFormat == "jpg" or "raster" or True:
        img = qrcode.make(address)
        click.secho("Saved to: QRCodes/"+address+".jpg", fg="green")
        try:
            img.save("QRCodes/"+address+".jpg")
        except:
            click.secho("[Much Error!] Failed to save file", fg="red")
    elif codeFormat == "svg" or "vector":
        code = pyqrcode.create(address)
        code.svg('QRCodes/'+address+".svg", scale=8)
        click.secho("Saved to: QRCodes/"+address+".svg", fg="green")

"""ASCII art and text on startup"""
def greeting():
    click.clear()
    click.secho(graphic, fg=color, bold=True)
    click.echo("MuchUnofficalToolKit Release 6 by Dylan Hamer amd Felix Zactor\n")
    click.secho("Donations Welcome:  ", nl=False)
    rainbow("DFUjFKtfRKCJGoo62jzzS6tUZnyTqxMHEV")
    click.echo("Type \'projects\' to see a list of community projects'")
    click.echo()
    rainbow("Welcome to MuchUnofficalToolKit! (Release 6)")
    click.secho("Type help to see help information or license to see open source licenses")
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
        click.secho("MuchToolKit Release 6", fg="green")
    elif command == "clear":
        greeting()
    elif command[0:5] == "genqr":
        if command == "genqr":
            generateQR(True)
        else:
            generateQR(command[6:len(command)])
    elif command == "blockchain":
        click.launch("http://www.dogechain.info")
    elif command == "address":
        address = input("Please enter a valid Dogecoin address: ")
        click.launch("http://www.dogechain.info/address/"+address)
    if command == "price btc":
            click.echo("Price in BTC is: "+click.style("BTC "+coinmarketcap.btcprice,fg="green"))
    elif command == "price usd":
            click.echo("Price in USD is: "+click.style("$"+coinmarketcap.usdprice,fg="green"))
    elif command == "price gbp":
            click.echo("Price in GBP is: "+click.style("£"+coinmarketcap.gbpprice,fg="green"))
    elif command == "price eur":
            click.echo("Price in EUR is: "+click.style("€"+coinmarketcap.eurprice,fg="green"))
    elif command == "price aud":
            click.echo("Price in AUD is: "+click.style("$"+coinmarketcap.audprice,fg="green"))
    elif command == "price cad":
            click.echo("Price in CAD is: "+click.style("$"+coinmarketcap.cadprice,fg="green"))
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
                elif command == "gbp":
                    click.echo("You have "+click.style("£"+str(float(coinmarketcap.gbpprice) * float(balance)))+" in Ðogecoin!")
                elif command == "eur":
                    click.echo("You have "+click.style("€"+str(float(coinmarketcap.eurprice) * float(balance)))+" in Ðogecoin!")
                elif command == "aud":
                    click.echo("You have "+click.style("$"+str(float(coinmarketcap.audprice) * float(balance)))+" in Ðogecoin!")
                elif command == "cad":
                    click.echo("You have "+click.style("$"+str(float(coinmarketcap.cadprice) * float(balance)))+" in Ðogecoin!")
                else:
                    click.secho("[such error] Coin not supported!", fg="red", blink=True)
    elif command[0:7] == "rainbow":
        rainbow(command[8:])
    elif command == "donate":
        rainbow("Donate to Felix Zactor: DT2X7SeX8P3gzjfHjAnkUs6LYcAduEcy2")
    elif command == "exit":
        click.clear()
        rainbow("To the moon!")
        exit(0)
    elif command == "":
        pass
    else:
        if command == "clear":
            pass
        else:
            click.secho("[Much Error!] Command not found!", fg="red")

def main():
    coinmarketcap = coinMarketCap()
    greeting()
    while True:
        commandHandler(prompt(), coinmarketcap)
if __name__ == "__main__":
    main()
