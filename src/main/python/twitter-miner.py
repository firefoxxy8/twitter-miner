#!/usr/bin/env python

# Copyright KOLIBERO under one or more contributor license agreements.  
# KOLIBERO licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import uuid
import argparse
from datetime import datetime

# Twitter libs
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#

class StdOutListener(StreamListener):
    def on_data(self, data):
      try:
          message = json.loads(data)
          if args.show_raw=="yes":
            print message
          text = message.get("text").encode("utf8")
          screen_name = message.get("user").get("screen_name")
          source = message.get("source")
          id = message.get("id")
          created_at = message.get("created_at")
          location = message.get("user").get("location")
          print "Text:\n",text
          print "Screen Name:",screen_name
          print "Source:",source
          print "ID:",id
          print "Created At:",created_at
          print "Location:",location
          print "-----------------------"
      except Exception, Argument:
          print "Unexpected Error!", Argument
          print(data)
      return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Twitter Miner")
  parser.add_argument('--access_token', default="")
  parser.add_argument('--access_token_secret', default="")
  parser.add_argument('--consumer_key', default="")
  parser.add_argument('--consumer_secret', default="")
  parser.add_argument('--filter', default="good food")
  parser.add_argument('--show_raw', default="no")

  args = parser.parse_args()
  print "access_token:",args.access_token
  print "access_token_secret:",args.access_token_secret
  print "consumer_key:",args.consumer_key
  print "consumer_secret:",args.consumer_secret
  print "filter:",args.filter
  print "show_raw:",args.show_raw

  print "Starting listening to Twitter..."

  l = StdOutListener()
  auth = OAuthHandler(args.consumer_key, args.consumer_secret)
  auth.set_access_token(args.access_token, args.access_token_secret)
  stream = Stream(auth, l)

  stream.filter(track=[args.filter])



