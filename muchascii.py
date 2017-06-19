"""
MuchAscii 0.1
Simple ASCII generator for Dogecoin

Note: This code is pretty redundant, I just didn't want
huge chunks of text in my code

Dylan Hamer 2017
"""

import click  # Needed for coloured text

def get(asciiFile):
    try:
        with open("ASCII/"+asciiFile+".txt") as file:
            ascii = file.read()
            file.close()
    except:
        click.secho("[Much Error!] Cannot find ASCII art for: "+asciiFile, fg="red")
        ascii = ""
    return ascii
           
