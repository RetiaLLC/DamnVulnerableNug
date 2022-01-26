# DamnVulnerableNug
The Damn Vulnerable Nugget Webapp for any ESP32S2 board

This vulnerable web application is designed to let beginners first try brute-forcing valid usernames, 
and then brute force a user's password. 

This is designed to run on an S2 Wi-Fi Nugget, but it will run on any ESP32s2 board. The Nugget will just
react to POST requests with an animated face expressing anger on failed credentials and joy when you win.

<h1>To install:</h1>

Install the latest version of CircuitPython on your ESP32S2 device

Download the contents of this GitHub repositoy

Plug in your CircuitPython device, it should show up a USB device called CIRCUITPY.

Unzip the DamnVulnerableNug.ZIP file and copy the contents to your CIRCUITPY drive, overwriting the existing files.

Open the 'secrets.py' file and add your Wi-Fi network name and password, save the file.

The DamnVulnerableNugget will now connect to your Wi-Fi Network. You can access the serial terminal to see the IP address,
or scan for the Nugget on your network with Nmap, Fing, Arp-Scan or another network scanner.

<h1>To play:</h1>

When connected to your Wi-Fi, the DamnVulnerableNugget will fetch a username list and a password list from Github.
It will then pick a random username and password from the list, and start the webapp. 

You'll have to solve a new login pair each time!

<h1>To solve:</h1>

Navigate to the DamnVulnerable Nugget page. Attempt to log in.

In BurpSuite or another proxy, intercept the POST request and examine it.

Brute-force the username using the username list here: https://raw.githubusercontent.com/danielmiessler/SecLists/master/Usernames/top-usernames-shortlist.txt

Brute-force the password with the password list here: https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/darkweb2017-top100.txt

When you succeed, you'll be taken to one of my favorite websites.
