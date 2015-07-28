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
        template = jinja_environment.get_template('templates/bday-card.html')

        bdName = self.request.get('bdName')
        # anniName = self.request.get('anniName')
        # gwName = self.request.get('gwName')
        # conName = self.request.get('conName')
        # gradName = self.request.get('gradName')
        # birthName = self.request.get('birthName')
        # xmasName = self.request.get('xmasName')
        # valinName = self.request.get('valinName')
        # holiName = self.request.get('holiName')
        # randName = self.request.get('randName')

        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = self.request.get('bdName')

        if bdName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "birthday"
            bdAge = self.request.get('bdAge')
            bdYName = self.request.get('bdYName')
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))

        # elif anniName:
        #     #search_term = self.request.get('bdName', 'bdAge')
        #     search_term = "anniversary"
        #     anniYears = self.request.get('anniYears')
        #     anniYName = self.request.get('anniYName')
        #     # The thing above checks if string in birthday name input is empty.
        #     giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
        #     giphy_json_content = giphy_data_source.content
        #     parsed_giphy_dictionary = json.loads(giphy_json_content)
        #     gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
        #     self.response.write(template.render({'gif_url': gif_url}))
        #
        # elif gwName:
        #     #search_term = self.request.get('bdName', 'bdAge')
        #     search_term = "get well"
        #     bdName = self.request.get('gwYName')
        #     # The thing above checks if string in birthday name input is empty.
        #     giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
        #     giphy_json_content = giphy_data_source.content
        #     parsed_giphy_dictionary = json.loads(giphy_json_content)
        #     gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
        #     self.response.write(template.render({'gif_url': gif_url}))

        # elif conName:
        #     #search_term = self.request.get('bdName', 'bdAge')
        #     search_term = "congradulations"
        #     conCongra = self.request.get('conCongra')
        #     conYName = self.request.get('conYName')
        #     # The thing above checks if string in birthday name input is empty.
        #     giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
        #     giphy_json_content = giphy_data_source.content
        #     parsed_giphy_dictionary = json.loads(giphy_json_content)
        #     gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
        #     self.response.write(template.render({'gif_url': gif_url}))
        #
        # elif gradName:
        #     #search_term = self.request.get('bdName', 'bdAge')
        #     search_term = "graduation"
        #     gradYear = self.request.get('gradYear')
        #     gradYName = self.request.get('gradYName')
        #     # The thing above checks if string in birthday name input is empty.
        #     giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
        #     giphy_json_content = giphy_data_source.content
        #     parsed_giphy_dictionary = json.loads(giphy_json_content)
        #     gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
        #     self.response.write(template.render({'gif_url': gif_url}))

        # elif birthName:
        #     #search_term = self.request.get('bdName', 'bdAge')
        #     search_term = "birth"
        #     birthGender = self.request.get('birthGender')
        #     birthYName = self.request.get('birthYName')
        #     # The thing above checks if string in birthday name input is empty.
        #     giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
        #     giphy_json_content = giphy_data_source.content
        #     parsed_giphy_dictionary = json.loads(giphy_json_content)
        #     gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
        #     self.response.write(template.render({'gif_url': gif_url}))

        # elif xmasName:
        #     #search_term = self.request.get('bdName', 'bdAge')
        #     search_term = "chistmas"
        #     xmasYName = self.request.get('xmasYName')
        #     # The thing above checks if string in birthday name input is empty.
        #     giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
        #     giphy_json_content = giphy_data_source.content
        #     parsed_giphy_dictionary = json.loads(giphy_json_content)
        #     gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
        #     self.response.write(template.render({'gif_url': gif_url}))

        # elif valinName:
        #     #search_term = self.request.get('bdName', 'bdAge')
        #     search_term = "valintines"
        #     valinYName = self.request.get('valinYName')
        #     # The thing above checks if string in birthday name input is empty.
        #     giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
        #     giphy_json_content = giphy_data_source.content
        #     parsed_giphy_dictionary = json.loads(giphy_json_content)
        #     gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
        #     self.response.write(template.render({'gif_url': gif_url}))

        # elif holiName:
        #     #search_term = self.request.get('bdName', 'bdAge')
        #     search_term = "holidays"
        #     holiType = self.request.get('holiType')
        #     holiYName = self.request.get('holiYName')
        #     # The thing above checks if string in birthday name input is empty.
        #     giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
        #     giphy_json_content = giphy_data_source.content
        #     parsed_giphy_dictionary = json.loads(giphy_json_content)
        #     gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
        #     self.response.write(template.render({'gif_url': gif_url}))

        # elif randName:
        #     #search_term = self.request.get('bdName', 'bdAge')
        #     search_term = "random"
        #     randYName = self.request.get('randYName')
        #     # The thing above checks if string in birthday name input is empty.
        #     giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
        #     giphy_json_content = giphy_data_source.content
        #     parsed_giphy_dictionary = json.loads(giphy_json_content)
        #     gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
        #     self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write("To Who?")
            self.response.write('''<html><body><img src="css/owl.jpg"></img></body></html>''')


class AnniHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/anni-card.html')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        anniName = self.request.get('anniName')
        if anniName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "anniversary"
            anniYears = self.request.get('anniYears')
            anniYName = self.request.get('anniYName')
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write("To Who?")
            self.response.write('''<html><body><img src="css/owl.jpg"></img></body></html>''')

class BirthHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/birth-card.html')
        birthName = self.request.get('birthName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = self.request.get('birthName')
        if birthName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "birth"
            birthGender = self.request.get('birthGender')
            birthYName = self.request.get('birthYName')
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write("To Who?")
            self.response.write('''<html><body><img src="css/owl.jpg"></img></body></html>''')

class ConHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/congrats-card.html')
        conName = self.request.get('conName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = self.request.get('conName')
        if conName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "congradulations"
            conCongra = self.request.get('conCongra')
            conYName = self.request.get('conYName')
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write("To Who?")
            self.response.write('''<html><body><img src="css/owl.jpg"></img></body></html>''')

class WellHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/getwell-card.html')
        gwName = self.request.get('gwName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = self.request.get('gwName')
        if gwName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "get well"
            bdName = self.request.get('gwYName')
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write("To Who?")
            self.response.write('''<html><body><img src="css/owl.jpg"></img></body></html>''')
class GradHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/grad-card.html')
        gradName = self.request.get('gradName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = self.request.get('gradName')
        if gradName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "graduation"
            gradYear = self.request.get('gradYear')
            gradYName = self.request.get('gradYName')
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write("To Who?")
            self.response.write('''<html><body><img src="css/owl.jpg"></img></body></html>''')

class XmasHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/xmas-card.html')
        xmasName = self.request.get('xmasName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = self.request.get('xmasName')
        if xmasName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "chistmas"
            xmasYName = self.request.get('xmasYName')
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write("To Who?")
            self.response.write('''<html><body><img src="css/owl.jpg"></img></body></html>''')
class ValinHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/valin-card.html')
        valinName = self.request.get('valinName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = self.request.get('valinName')
        if valinName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "valintines"
            valinYName = self.request.get('valinYName')
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write("To Who?")
            self.response.write('''<html><body><img src="css/owl.jpg"></img></body></html>''')
class HolidaysHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/holidays-card.html')
        holiName = self.request.get('holiName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = self.request.get('holiName')
        if holiName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "holidays"
            holiType = self.request.get('holiType')
            holiYName = self.request.get('holiYName')
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write("To Who?")
            self.response.write('''<html><body><img src="css/owl.jpg"></img></body></html>''')

class RandomHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/random-card.html')
        randName = self.request.get('randName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = self.request.get('randName')
        if randName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "random"
            randYName = self.request.get('randYName')
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url = parsed_giphy_dictionary['data'][random.randint(0,5)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write('''
<html>
    <body>
        <center>
        <br>
        <p> To Who? </p>
        <br>
        <img src="css/owl.jpg"> </img>
        <center>
        <br>
    </body>
</html>
''')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/bday-card', MainHandler),
    ('/anni-card', AnniHandler),
    ('/birth-card', BirthHandler),
    ('/congrats-card', ConHandler),
    ('/getwell-card', WellHandler),
    ('/grad-card', GradHandler),
    ('/xmas-card', XmasHandler),
    ('/valin-card', ValinHandler),
    ('/holidays-card', HolidaysHandler),
    ('/random-card', RandomHandler),
], debug=True)
