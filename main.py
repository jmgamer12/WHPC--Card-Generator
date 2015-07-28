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
import logging

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/bday-card.html')
        bdName = self.request.get('bdName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = self.request.get('bdName')

        if bdName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "birthday"
            bdAge = self.request.get('bdAge')
            bdYName = self.request.get('bdYName')
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = 'Happy Birthday ' + bdName + ", <br>I can't believe you're " + bdAge + '! <br>' + bdYName
            elif textRand == 2:
                quote1 = bdName + ",<br>Hey dude happy " + bdAge + ' Birthday! <br>' + bdYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
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
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = 'Happy ' + anniYears + ", anniversary! I'm so happy for you, " + anniName + ' and hope you can celebrate many more! <br>' + anniYName
            elif textRand == 2:
                quote1 = anniName + ", <br>Congradulations on your " + anniYears + ' anniversary! <br>' + anniYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
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
        birthYName = self.request.get('birthYName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = "baby"
        # Make emptty variables for quotes within handlers about here
        quote = None
        quote1 = None
        if birthName:
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                # Turn self.response.write into variables here
                quote = birthName + ", <br>Apparently you gave birth...<br>Enjoy the barf and diapers life!<br>" + birthYName
                #self.response.write('''<html><body><br></body></html>''')
            elif textRand == 2:
                # And here.
                quote1 = birthName + ",<br>Congrats on your new baby! Remember, babies don't become cool till they become teenagers.<br>With love,<br>" + birthYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            # Add all variables to dictionary here. Also take a look at birth-card.html for more hep
            self.response.write(template.render({'quote1': quote1, 'birthYName': birthYName, 'quote': quote,'gif_url': gif_url}))
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
            search_term = self.request.get('conCongra')
            #search_term = "congradulations"
            conCongra = self.request.get('conCongra')
            conYName = self.request.get('conYName')
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = 'Congradulations ' + conName + ", <br>Everyone is so proud of your " + conCongra + '! <br>Keep up the good work, <br>' + conYName
            elif textRand == 2:
                quote1 = conName + ", <br>Congradulations on " + conCongra + "! I'm so proud of you, <br>" + conYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
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
            search_term = "sick"
            gwYName = self.request.get('gwYName')
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = 'Dear ' + gwName + ", <br>I know it feels suck-y right now, but it will get better, really.<br>Hope you get well soon:<br>" + gwYName
            elif textRand == 2:
                quote1 = gwName + ", <br>Being sick sucks, but you get lots of free stuff like this card!<br>Get better soon!<br>" + gwYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
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
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = "Sooo, I heard you're graduating... Totally knew you could do it. <br>Congrats" + gradName + " Class of " + gradYear + "<br>From: " + gradYName
            elif textRand == 2:
                quote1 = 'Happy Graduation' + gradName + "! <br>It's now time to face the real world!<br>" + gradYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
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
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = 'Dear' + xmasName + ", <br>Merry Christmas! may you and your family have a happy holiday and a prosperous New Year! <br>From: " + xmasYName
            elif textRand == 2:
                quote1 = 'Hey ' + xmasName + "!<br>Hoping that you are celebrating the season with lots of love and joy. Merry Christmas!<br>" + xmasYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
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
            search_term = "love"
            valinYName = self.request.get('valinYName')
            #creation of the random text
            textRand = random.randint(1, 3)
            if textRand == 1:
                quote = valinName + ",<br>Roses are red,<br>Violets are blue,<br>It's the time of the year,<br>When all I want is you!<br>Love,<br>" + valinYName
            elif textRand == 2:
                quote1 = valinName + ", This may be cliche,<br>But will you be my bae?<br>Happy Valintines Day!<br>Love,<br> " + valinYName
            elif textRand == 3:
                quote2 = valinName + ",<br>Just speading the love this season. Happy V day!<br>Love,<br>" + valinYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
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
            search_term = "party"
            holiType = self.request.get('holiType')
            holiYName = self.request.get('holiYName')
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = 'Dear ' + holiName + ",<br>Happy" + holiType + "! Enjoy the holidays while they last!<br>" + holiYName
            elif textRand == 2:
                quote1 = holiName + ",<br>May you have a happy" + holiType + "!<br> " + valinYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
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
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = randName + ",<br>Dude I'm not exactly sure why I am sending a card, but I do know you're important enough to get one!<br>" + randYName
            elif textRand == 2:
                quote1 = randName + ",<br>I love you so much I used a random card generator to make this for you...<br> " + randYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            self.response.write(template.render({'gif_url': gif_url}))
        else:
            self.response.write('''<html><body><center><br><p> To Who? </p><br><img src="css/owl.jpg"> </img><center><br></body></html>''')

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
