#!/usr/bin/python
#
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Allow control of output devices such as Motors, Servos, LEDs, and Relays
from gpiozero import Motor, Servo, LED, Energenie, OutputDevice

import sys
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import Database
import json

from authbox.api import *
from authbox.config import Config
from authbox.timer import Timer


#from neopixel import *
import argparse

# Useful CONSTANTS to allow quick update of software, when hardware changes
RELAY_RL1_MAKER_SPACE_AUTH_BOARD_J12 = 6        # Physical Pin 31 / BCM-6
#PWR_12V = "J12-1"
#GND = "BOARD6"

with open('contacts.json', 'r') as myfile:
    data=json.loads(myfile.read())
    id_list = []
    for keys in data.viewkeys():
        badgeIDs = data.get(keys).get("badgeId")
        for word in badgeIDs.split(','):
            word = word.strip()
            try:
                word=int(word,16)
                id_list.append(word)
            except:
                pass

DEVNULL = open('/dev/null', 'r+')
class Dispatcher(BaseDispatcher):
  def __init__(self, config):
    super(Dispatcher, self).__init__(config)
    self.load_config_object('badge_reader', on_scan=self.badge_scan)

  def badge_scan(self, badge_id):
    lock = OutputDevice(RELAY_RL1_MAKER_SPACE_AUTH_BOARD_J12) # BCM-6

    badge_int = int(badge_id, 16)
    print "Badge str", str(badge_int)
    print "var type", type(str(badge_int))
    print "Badge hex", badge_id

    temp_list = id_list

    if badge_int in temp_list:
        time.sleep(0.5)
        print("Unlocking with badge:")
        print badge_id
        lock.on()       #Unlock
        time.sleep(2.0) #Pause 3.0 seconds = 1500 milliseconds
        lock.off()      #lock
        print("Lock")

    else:
        print("Badge not found in member database.")

def main(args):
  config_filename = 'yms-rfid.ini'
  config = Config(config_filename)
  Dispatcher(config).run_loop()


if __name__ == '__main__':
  # Process arguments

  parser = argparse.ArgumentParser()
  parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
  args = parser.parse_args()

  print ('Press Ctrl-C to quit.')
  if not args.clear:
    pass

  main(sys.argv[1:])
