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

bottom = """
</body>
</html>
"""
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
        num = self.request.get("num")
        big_title = """<h1>Caeser Encryption</h1>"""
        rotation = """
        <form method="post">
            <label> Enter rotation amount.
                <input type="number" name="rot" value="0">
                <input type="submit">
            </label>
        </form>
        """

        message = """
        <form method="post">
            <textarea rows="10" cols="50" name="message">
                Enter message.
            </textarea>
        </form>
        """


        final = top + big_title + rotation + message + bottom

        self.response.write(final) #I really don't understand this command


class Encrypted(webapp2.RequestHandler):

    def post(self):

        rot_amount = self.request.get("rot")
        mess = self.request.get("message")

        new_body = """
        <textarea>
            rot_custom(rot_amount,cgi.escape(mess))
        </textarea>
        """

        encrypted_final = top + big_title + new_body + bottom

        self.response.write(encrypted_final)


    #Make an input field for the rot value in rot_custom
        #Make an input field for the message value, probably some text box
        #Display the encrypted and escaped text at the bottom of the page
        #HELP




app = webapp2.WSGIApplication([
    ('/', Home)
], debug=True)
