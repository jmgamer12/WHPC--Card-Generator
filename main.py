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

            # Make empty variables for quotes within handlers about here

            quote = None
            quote1 = None
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = 'Happy Birthday ' + bdName + ',' + '<br>' + " <br>I can't believe you're " + bdAge + '! <br>' + '<br>' + bdYName
            elif textRand == 2:
                quote1 = bdName + ',' + '<br>' + "<br>Hey dude happy  birthday! " + "You're finally " + bdAge +  '!' + '<br><br>' + bdYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            self.response.write(template.render({'bdName': bdName, 'bdAge': bdAge, 'bdYName': bdYName, 'quote1': quote1, 'quote': quote,'gif_url': gif_url}))
        else:
            self.response.write('''<html><body><center><br><p> To Who? </p><br><img src="css/owl.jpg"> </img><center><br></body></html>''')



class AnniHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/anni-card.html')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        anniName = self.request.get('anniName')
        # Make empty variables for quotes within handlers about here
        quote = None
        quote1 = None
        if anniName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "marriage"
            anniYears = self.request.get('anniYears')
            anniYName = self.request.get('anniYName')
            # Make empty variables for quotes within handlers about here
            quote = None
            quote1 = None
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = "Happy anniversary, " + anniName + '! <br> <br>' + " I'm so proud of you both for reaching " + anniYears + ' years! <br> Hope you both can celebrate many more! <br> <br> <br>' + anniYName
            elif textRand == 2:
                quote1 = anniName + ", <br><br>Congratulations on reaching " + anniYears + ' years! <br><br><br>' + anniYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            self.response.write(template.render({'anniYears': anniYears, 'anniName': anniName, 'anniYName': anniYName, 'quote1': quote1, 'quote': quote,'gif_url': gif_url}))
        else:
            self.response.write('''<html><body><center><br><p> To Who? </p><br><img src="css/owl.jpg"> </img><center><br></body></html>''')


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
        # Make empty variables for quotes within handlers about here
        quote = None
        quote1 = None
        if birthName:
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                # Turn self.response.write into variables here
                quote = birthName + ", <br><br>Apparently you gave birth...<br><br>Enjoy the barf and diapers life!<br><br>" + birthYName
                #self.response.write('''<html><body><br></body></html>''')
            elif textRand == 2:
                # And here.
                quote1 = birthName + ",<br><br>Congrats on your new baby! <br> Remember, babies don't become cool till they become teenagers.<br><br><br>With love,<br><br>" + birthYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            # Add all variables to dictionary here. Also take a look at birth-card.html for more hep
            self.response.write(template.render({'birthName': birthName, 'quote1': quote1, 'birthYName': birthYName, 'quote': quote,'gif_url': gif_url}))
        else:
            self.response.write('''<html><body><center><br><p> To Who? </p><br><img src="css/owl.jpg"> </img><center><br></body></html>''')


class ConHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_environment.get_template('templates/congrats-card.html')
        conName = self.request.get('conName')
        conCongra = self.request.get('conCongra')
        conYName = self.request.get('conYName')
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=5"
        search_term = self.request.get('conName')
        # Make empty variables for quotes within handlers about here
        quote = None
        quote1 = None
        if conName:
            search_term = self.request.get('conCongra')
            search_term= search_term.replace(' ', '+')
            #search_term = "congradulations"
            conCongra = self.request.get('conCongra')
            conYName = self.request.get('conYName')
            # Make empty variables for quotes within handlers about here
            quote = None
            quote1 = None
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = 'Congratulations ' + conName + ", <br><br>Everyone is so proud of your " + conCongra + '! <br><br><br>Keep up the good work, <br>' + conYName
            elif textRand == 2:
                quote1 = conName + ", <br><br>Congratulations on " + conCongra + "! <br><br> I'm so proud of you, <br>" + conYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            self.response.write(template.render({'conName': conName, 'conCongra': conCongra, 'conYName': conYName, 'quote1': quote1, 'quote': quote,'gif_url': gif_url}))
        else:
            self.response.write('''<html><body><center><br><p> To Who? </p><br><img src="css/owl.jpg"> </img><center><br></body></html>''')


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
        # Make empty variables for quotes within handlers about here
        quote = None
        quote1 = None
        if gwName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "sick"
            gwYName = self.request.get('gwYName')
            # Make empty variables for quotes within handlers about here
            quote = None
            quote1 = None
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = 'Dear ' + gwName + ", <br><br>I know it feels suck-y right now, but it will get better, really.<br><br>Hope you get well soon!<br><br><br>" + gwYName
            elif textRand == 2:
                quote1 = gwName + ", <br><br>Being sick sucks, but you get lots of free stuff like this card!<br><br>Get better soon!<br><br><br>" + gwYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            self.response.write(template.render({'gwName': gwName, 'gwYName': gwYName, 'quote1': quote1, 'quote': quote,'gif_url': gif_url}))
        else:
            self.response.write('''<html><body><center><br><p> To Who? </p><br><img src="css/owl.jpg"> </img><center><br></body></html>''')

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
        # Make empty variables for quotes within handlers about here
        quote = None
        quote1 = None
        if gradName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "graduation"
            gradYear = self.request.get('gradYear')
            gradYName = self.request.get('gradYName')
            # Make empty variables for quotes within handlers about here
            quote = None
            quote1 = None
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = "Sooo, I heard you're graduating... Totally knew you could do it. <br><br>Congrats, " + gradName + "! Class of " + gradYear + "<br><br><br>From: " + gradYName
            elif textRand == 2:
                quote1 = 'Happy Graduation, ' + gradName + "! <br><br>It's now time to face the real world!<br><br><br>" + gradYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            self.response.write(template.render({'gradName': gradName, 'gradYName': gradYName, 'quote1': quote1, 'quote': quote,'gif_url': gif_url}))
        else:
            self.response.write('''<html><body><center><br><p> To Who? </p><br><img src="css/owl.jpg"> </img><center><br></body></html>''')


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
        # Make empty variables for quotes within handlers about here
        quote = None
        quote1 = None
        if xmasName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "chistmas"
            xmasYName = self.request.get('xmasYName')
            # Make empty variables for quotes within handlers about here
            quote = None
            quote1 = None
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = 'Dear' + xmasName + ", <br><br>Merry Christmas! May you and your family have a happy holidays and a prosperous New Year! <br><br><br>From: " + xmasYName
            elif textRand == 2:
                quote1 = 'Hey ' + xmasName + "!<br><br>Hoping that you are celebrating the season with lots of love and joy. <br><br> Merry Christmas!<br><br><br>" + xmasYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            self.response.write(template.render({'xmasName': xmasName, 'xmasYName': xmasYName, 'quote1': quote1, 'quote': quote,'gif_url': gif_url}))
        else:
            self.response.write('''<html><body><center><br><p> To Who? </p><br><img src="css/owl.jpg"> </img><center><br></body></html>''')

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
        # Make empty variables for quotes within handlers about here
        quote = None
        quote1 = None
        quote2 = None
        if valinName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "love"
            valinYName = self.request.get('valinYName')
            #creation of the random text
            textRand = random.randint(1, 3)
            if textRand == 1:
                quote = valinName + ",<br><br>Roses are red,<br>Violets are blue,<br>It's the time of the year,<br>When all I want is you!<br><br>Love,<br>" + valinYName
            elif textRand == 2:
                quote1 = valinName + ",<br><br> This may be cliche,<br>But will you be my bae?<br><br>Happy Valintines Day!<br><br><br>Love,<br> " + valinYName
            elif textRand == 3:
                quote2 = valinName + ",<br><br>Just speading the love this season.<br><br> Happy Valentine's Day!<br><br><br>Love,<br>" + valinYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            self.response.write(template.render({'valinYName': valinYName, 'quote2': quote2, 'quote1': quote1, 'quote': quote,'gif_url': gif_url}))
        else:
            self.response.write('''<html><body><center><br><p> To Who? </p><br><img src="css/owl.jpg"> </img><center><br></body></html>''')

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
        # Make empty variables for quotes within handlers about here
        holiType = self.request.get('holiType')
        holiYName = self.request.get('holiYName')
        quote = None
        quote1 = None
        if holiName:
            search_term = self.request.get('holiType')
            search_term= search_term.replace(' ', '+')
            #creation of the random text
            textRand = random.randint(1, 2)
            if textRand == 1:
                quote = 'Dear ' + holiName + ",<br><br>Happy " + holiType + "! <br> Enjoy the holidays while they last!<br><br>" + holiYName
            elif textRand == 2:
                quote1 = holiName + ",<br><br>May you have a happy " + holiType + "!<br><br> " + holiYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            self.response.write(template.render({'holiName': holiName, 'holiType': holiType, 'holiYName': holiYName, 'quote1': quote1, 'quote': quote,'gif_url': gif_url}))
        else:
            self.response.write('''<html><body><center><br><p> To Who? </p><br><img src="css/owl.jpg"> </img><center><br></body></html>''')


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
        # Make empty variables for quotes within handlers about here
        quote = None
        quote1 = None
        if randName:
            #search_term = self.request.get('bdName', 'bdAge')
            search_term = "random"
            randYName = self.request.get('randYName')
            # Make empty variables for quotes within handlers about here
            quote = None
            quote1 = None
            #creation of the random text
            textRand = random.randint(1, 2)

            if textRand == 1:
                quote = randName + ",<br><br>Dude, I'm not exactly sure why I am sending a card, but I do know you're important enough to get one!<br><br>" + randYName
            elif textRand == 2:
                quote1 = randName + ",<br><br>I love you so much I used a random card generator to make this for you...<br> <br>" + randYName
            # The thing above checks if string in birthday name input is empty.
            giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url)
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            x = len(parsed_giphy_dictionary['data'])
            gif_url = parsed_giphy_dictionary['data'][random.randint(0, x-1)]['images']['original']['url']
            self.response.write(template.render({'randName': randName, 'randYName': randYName, 'quote1': quote1, 'quote': quote,'gif_url': gif_url}))
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
