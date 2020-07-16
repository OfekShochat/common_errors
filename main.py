import subprocess
import json
from fuzzywuzzy import fuzz

filename = input("filename: ")
errors = open("./common_errors.txt", "r").readlines()

try:
    subprocess.check_output("py " + filename,shell=True,stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    you_are_a_loser = str(e.output)[2:-1]
    for ip in errors:
        if fuzz.ratio(ip, you_are_a_loser) > 30:
            print(ip[ip.find(">") + 2:] + " in " + you_are_a_loser.split(',')[1].split('\\r')[0])