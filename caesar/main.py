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

big_title = """<h1>Caesar Encryption</h1>"""

def rot_custom(rot,message):
    final = ""
    message = str(message)
    for char in message:
        if char.isalpha() == False:
            final += char
        letter = (ord(char) + int(rot)) % 26
        letter = chr(letter)
        final += letter
    return final

class Home(webapp2.RequestHandler):

    def post(self):
        #This is all over the place
        #num = self.request.get("num")

        entered = ""

        caesar = """
        <form method="post" action="/">
            <label> Enter rotation amount.
                <input type="number" name="rot" value="0">
            </label>
            <br>
            <textarea rows="10" cols="50" type="text" name="message">
            %(entered)s
            </textarea>
            <br>
            <input type="submit">
        </form>
        """
        final = top + big_title + caesar + bottom
        #final = rot_custom(rot,message)

        self.response.write(final)

        rot = self.request.get("rot")
        rot = int(rot)
        message = self.request.get("message")
        message = cgi.escape(message, quote=True)

        encryption = rot_custom(rot,message)

        entered += encryption

        encrypted_final = top + str(encryption) + bottom

        self.response.write(encrypted_final)


app = webapp2.WSGIApplication([
    ('/', Home)
], debug=True)
