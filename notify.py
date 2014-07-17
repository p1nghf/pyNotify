__author__ = "p1ng"
__credits__ = ["Yuni"]
__version__ = "0.0.1"
__maintainer__ = "p1ng"
__status__ = "Pre-Alpha"

import urllib2, sys

key = raw_input("What is your API Key?\n")

def _sendMessage():
    message = raw_input("What is your message?\n")
    if(message == "exit"):
        sys.exit(0)
    message = message.replace(" ", "%20")
    message = message.replace("//", "%0A")
    url = "http://soulsplitbot.us/notifier/api.php?key=" + key + "&msg=" + message
    open = urllib2.urlopen(url)
    status = open.read()
    if(status == "SUCCES"):
        print ("Message Sent!")
        _sendMessage()
    else:
        print status
        _sendMessage()

_sendMessage()