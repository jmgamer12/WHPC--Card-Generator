#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
from google.appengine.api import urlfetch
import random
import urllib
import json

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))



class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/card.html')
        bdName = self.request.get('bdName')
        anniName = self.request.get('anniName')
        gwName = self.request.get('gwName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=10"
        search_term = self.request.get('bdName')
        if not bdName:
            search_term = self.request.get('bdName', 'bdAge')
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][random.randint(0,10)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write("Enter the birthday person please")



# class ImgSearchHandler(webapp2.RequestHandler):
#     def post(self):
#         template = jinja_environment.get_template()
#         base_url = "http://api.giphy.com/v1/gifs/search?q="
#         api_key_url = "&api_key=dc6zaTOxFJmzC&limit=10"
#         giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
#         giphy_json_content = giphy_data_source.content
#         parsed_giphy_dictionary = json.loads(giphy_json_content)
#         gif_url = parsed_giphy_dictionary['data'][random.randint(0,20)]['images']['original']['url']
#         self.response.write(template.render({'gif_url': gif_url}))


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/card', MainHandler)
], debug=True)
