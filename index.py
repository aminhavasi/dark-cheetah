#!/usr/bin/env python

import sys
import socket
import os
import time
from banner import banner
from utils import cloudflare

try:
    from colorama import Fore
except:
    os.system("clear")
    print(
        Fore.RED
        + """\n Please Install colorama\n
    pip3 install colorama
        """
    )

# ---------------------------

try:
    import requests
except:
    os.system("clear")
    print(
        Fore.RED
        + """\n Please Install requests\n
    pip3 install requests
        """
    )

# ---------------------------


try:
    import ipapi
except:
    os.system("clear")
    print(
        Fore.RED
        + """\n Please Install ipapi\n
    pip3 install ipapi
        """
    )

# ---------------------------


try:
    import builtwith
except:
    os.system("clear")
    print(
        Fore.RED
        + """\n Please Install builtwith\n
    pip3 install builtwith
        """
    )

# ---------------------------
while True:
    try:
        banner.Banner()
        banner.infolist1()
    

        number = input(
            Fore.RED
            + "***"
            + Fore.LIGHTGREEN_EX
            + "Dark Cheetah"
            + Fore.BLUE
            + "~"
            + Fore.WHITE
            + "@HOME"
            + Fore.RED
            + "***"
            + Fore.WHITE
            + ">>:"
        ).lower()

    except:
        print("\n good by!")
        sys.exit()
    if number == "0":
        print("goodby!")
        sys.exit()
    elif number == "":
        print(Fore.RED+" [!]"+Fore.BLUE+" Please Enter Number :))))")
        input("")
    elif number=="1":
        cloudflare.__start__()
        
