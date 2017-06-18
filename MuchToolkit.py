#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MuchToolkit 0.1
Dogecoin Toolkit
Dylan Hamer 2017
"""

import click  # Make beautiful interfaces

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

help="""\nMuch Help
--------------------------
List of commands:
_______________________________________
help              | Show this message
version           | Get current version
genQR             | Generate a QR code
blockchain        | Open dogechain.info
address <address> | Explore an address\n"""

def greeting():
    click.clear()    
    click.secho(doge, fg="yellow")
    click.echo("MuchToolkit0.1 by Dylan Hamer\n")
    click.secho("Donations Welcome:  ", nl=False)
    click.secho("DFUjFKtfRKCJGoo62jzzS6tUZnyTqxMHEV", fg="green")
    click.secho("Socks for the homeless: ", nl=False)
    click.secho("9vnaTWu71XWimFCW3hctSxryQgYg7rRZ7y", fg="blue")
    click.echo()

def menu():
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
        elif command == "":
            pass    
        else:
            click.secho("[Much Error!] Command not found!", fg="red")

def main():
    greeting()
    menu()

if __name__ == "__main__": 
    main()
