#! /usr/bin/python

import urllib2
import json
import cgi

import cgitb
cgitb.enable()

#Grabbing Real-Time Data
url = "http://citibikenyc.com/stations/json"
jsondata = urllib2.urlopen(url).read()
(true,false,null) = (True,False,None)
profiles = str(jsondata)
citidata = json.loads(jsondata)
##print citidata["executionTime"]

HTML_HEADER = 'Content-type: text/html\n\n'  #[5]

#[6]
Top_HTML = '''
<html>
<head>
<title>Sample Python Forms-responder</title>
</head>
<body>
<b>The Transmitted HTML input elements are...</b>
<p>
'''

Bottom_HTML = '</body></html>'

def ShowInputElements():
    elements = cgi.FieldStorage()  #[7]

    print HTML_HEADER + Top_HTML
    keys = elements.keys()  #[8]
    for akey in keys:
        print akey + ' = ' + elements[akey].value + '<br>'  #[9]
    print Bottom_HTML

ShowInputElements()  #[10]
