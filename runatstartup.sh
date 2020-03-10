#! /bin/bash
export CLIENT_ID="XXXXXXXXX"
export CLIENT_SECRET="XXXXXXXXX"
export API_KEY="XXXXXXXXX"

cd /home/pi/yms-rfid-reader

while true
do
  python3 WaCheck.py
  sleep 5
  sh killrfid.sh
  sleep 1
  python yms-rfid.py &
  sleep 900
done
