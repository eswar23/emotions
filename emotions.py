from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

from random import randint
from nric import NRICValidator

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
    def processRequest(req):
    if req.get("result").get("action") != "AnimalJoker":
        return {}
    
    res = makeWebhookResult(req)
    return res

    def makeWebhookResult(req):
    
    result = req.get("result")
    parameters = result.get("parameters")
    emotion = parameters.get("Emotions")
    
    
    if sad:
        speech = "Why suddenly sad?"
    else:
        speech = "I'm happy that you are happy"

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "AnimalJoker"
    }
    if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')