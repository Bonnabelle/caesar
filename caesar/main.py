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
import cgi

top = """
<!DOCTYPE html>
<html>
<head>
    <title>The Rotater</title>
</head>
<body>
"""

bottom = ""
</body>
</html>
"""

big_title = """<h1>Caesar Encryption</h1>"""

def rot_custom(rot,message):
    final = ""
    message = str(message)
    for char in message:
        if char.isalpha() == False:
            final = final + char
        letter = ord(char) + int(rot) % 26
        letter = chr(letter)
        final= final + letter
    return final

class Home(webapp2.RequestHandler):

    def get(self):
        #This is all over the place
        #num = self.request.get("num")
        caesar = """
        <form method="post" action="/encrypt">
            <label> Enter rotation amount.
                <input type="number" name="rot" value="0">
            </label>
            <textarea rows="10" cols="50" type="text" name="message">
                Enter message.
            </textarea>
            <input type="submit">
        </form>
        """


        final = top + big_title + caesar + bottom
        #final = rot_custom(rot,message)

        self.response.write(final)


class Encrypted(webapp2.RequestHandler):

    def post(self):

        rot = self.request.get("rot")
        rot = int(rot)
        message = self.request.get("message")
        message = cgi.escape(message, quote=True)

        encryption = rot_custom(rot,message)

        encrypted_final = top + big_title + encryption + bottom

        self.response.write(encrypted_final)


    #Make an input field for the rot value in rot_custom
        #Make an input field for the message value, probably some text box
        #Display the encrypted and escaped text at the bottom of the page
        #HELP




app = webapp2.WSGIApplication([
    ('/', Home),
    ('/encrypt',Encrypted)
], debug=True)
