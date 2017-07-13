"""
MuchAscii 0.1
Simple ASCII generator for Dogecoin

Note: This code is pretty redundant, I just didn't want
huge chunks of text in my code

Dylan Hamer 2017
"""

import click  # Needed for coloured text
import random # Needed for random choice
import os     # Needed for getting files

def randomChoice():
    files = []

    for dirname, dirnames, filenames in os.walk('ASCII'):
        for filename in filenames:
            files.append(filename)
    graphic = random.choice(files)
    return get("ASCII/"+graphic)

def get(asciiFile):
    try:
        with open(asciiFile) as file:
            ascii = file.read()
            file.close()
    except:
        click.secho("[Much Error!] Cannot find ASCII art for: "+asciiFile, fg="red")
        ascii = ""
    return ascii
           
