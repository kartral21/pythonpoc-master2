SUCCESS = 200
ACCEPTED = 202
ERROR = 400

HELLO_DATA = 'Hello ATF!'
EMAIL_DATA = {"json_list":[{"sample":"test"}],"html":"""<html></html>"""}

NOSE_ARGS = [
    '--with-coverage',
    '--cover-html',
    '--cover-package=flaskpoc',
    '--cover-html-dir=reports/cover',
    '--verbosity=2']