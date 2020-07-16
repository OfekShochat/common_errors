import subprocess
import json
from fuzzywuzzy import fuzz

filename = input("filename: ")
errors = open("./common_errors.txt", "r").read().splitlines()

try:
    subprocess.check_output("py " + filename,shell=True,stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    you_are_a_loser = str(e.output)[2:-1]
    for ip in errors:
        if fuzz.ratio(ip[:ip.find(">") - 1], you_are_a_loser) > 40:
            print(ip[ip.find(">") + 2:] + " in" + you_are_a_loser.split(',')[1].split('\\r')[0])
            print(fuzz.ratio(ip[:ip.find(">") - 1], you_are_a_loser))