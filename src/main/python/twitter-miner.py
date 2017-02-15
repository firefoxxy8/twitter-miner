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

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Twitter Miner")
  parser.add_argument('--access_token', default="")
  parser.add_argument('--access_token_secret', default="")
  parser.add_argument('--consumer_key', default="")
  parser.add_argument('--consumer_secret', default="")

  args = parser.parse_args()
  print "access_token:",args.access_token
  print "access_token_secret:",args.access_token_secret
  print "consumer_key:",args.consumer_key
  print "consumer_secret:",args.consumer_secret



