# Copyright 2012 Digital Inspiration


import os
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import mail

class MainHandler(webapp2.RequestHandler):
  def get (self, q):
    if q is None:
      q = 'index.html'


    path = os.path.join (os.path.dirname (__file__), q)
    self.response.headers ['Content-Type'] = 'text/html'
    self.response.out.write (template.render (path, {}))

class SendEmail(webapp2.RequestHandler):
  def post(self):
    name = self.request.get('name', '')
    email = self.request.get('email', '')
    phone = self.request.get('phone', '')
    msg = self.request.get('message', '')
    qa = self.request.get('qa', '')

    if '3' != qa or email == '':
      self.response.out.write("Error: You did not answer the question correctly.")   
    else:
      _subject = "Message from: " + name + ", Re: enquiry"
      msg += "\n\nI can be reached at "
      msg += email
      msg += "\n\nMy phone is "
      msg += phone

      message = mail.EmailMessage(sender = "goodhealthacupuncturewgtn@gmail.com", to = "hairui@xtra.co.nz")
      message.subject = _subject
      message.body = msg
      message.send()
      self.redirect('/confirm-email.html')

app = webapp2.WSGIApplication([('/email', SendEmail), ('/(.*html)?', MainHandler)], debug=True)
