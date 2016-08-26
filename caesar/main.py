import webapp2
import cgi

top = """
<!DOCTYPE html>
<html>
<head>
    <title>The Rotater</title>
</head>
<body>
<h1>Caesar Encryption</h1>
"""

bottom = """
</body>
</html>
"""

caesar = """
<form method="post">
    <label> Enter rotation amount.
        <input type="number" name="rot" value="0">
    </label>
    <br>
    <textarea rows="10" cols="50" type="text" name="message">
    %(entered)s
    </textarea>
    <br>
    <input type="submit"></form>
"""

from caesar import encrypt

class Home(webapp2.RequestHandler):

    def get(self):
        final = top + caesar + bottom
        self.response.write(final)

    def post(self):

        rot = self.request.get("rot")
        rot = int(rot)
        message = self.request.get("message")
        message = cgi.escape(message, quote=True)

        entered = {"entered": encrypt(message,rot)}

        new_caesar = caesar % entered

        encrypted_final = top + new_caesar + bottom

        self.response.write(encrypted_final)

app = webapp2.WSGIApplication([
    ('/', Home)
], debug=True)
