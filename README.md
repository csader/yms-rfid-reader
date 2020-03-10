# Summary

based on MintyBox from nomcon 2019

"yms-rfid.py" receives scanned badges, checks checks them against the contacts.json file (WIP) to see if a badge id is listed, then unlocks a lock for 3 seconds, then re-locks it

"WaCheck.py" hits the Wild Apricot, downloads a list of members with badges from Wild Apricot

## Install on Raspberry Pi
```
git clone https://github.com/csader/yms-rfid-reader.git
cd yms-rfid-reader
nano runatstartup.sh 
```

Replace CLIENT_ID=“XXXXXXXX”, CLIENT_SECRET=“XXXXXXXX”, and API_KEY=“XXXXXXXX” with your Wild Apricot integration details

CTRL+X to exit, Y to save changes

```
chmod +x killrfid.sh
chmod +x runatstartup.sh
crontab -e
```

Add the following to the bottom of the file:

```
@reboot sleep 10 && /home/pi/yms-rfid-reader/runatstartup.sh &
```

CTRL+X to exit, Y to save changes

```
sudo reboot
```
