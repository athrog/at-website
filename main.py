import logging
import webapp2

class HomePageHandler(webapp2.RequestHandler):
    def get(self):
        file = open('index.html', 'r')
        self.response.out.write(file.read())

app = webapp2.WSGIApplication([('/', HomePageHandler)], debug=True)
