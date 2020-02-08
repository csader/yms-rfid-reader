# Summary

based on MintyBox from nomcon 2019

"yms-rfid.py" is the latest working code that currently checks the "authorized.txt" file to see if a badge id is listed, then unlocks a lock for 3 seconds, then re-locks it

"WaCheck.py" is the code Andrew wrote that hits the Wild Apricot, downloads a list of members with badges from Wild Apricot

ToDos:
1. WaCheck.py needs to also pull the badge id that's in Wild Apricot into the json file
2. yms-rfid.py needs to be modified to check for the badge id recognized on the RFID reader, to see if it exists in the json file instead of authorized.txt
3. a cronjob needs to be written to run WaCheck.py every 5 minutes
4. yms-rfid.py needs to be run at boot
