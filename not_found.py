import webapp2

class PageNotFoundHandler(webapp2.RequestHandler):
    def get(self):
        file = open('not_found.html', 'r')
        self.response.out.write(file.read())

app = webapp2.WSGIApplication([('/.*', PageNotFoundHandler)], debug=True)
