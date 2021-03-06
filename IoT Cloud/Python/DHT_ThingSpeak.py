import time
import sys  
import httplib, urllib

sys.path.insert(0, '/usr/lib/python2.7/bridge/') 
from bridgeclient import BridgeClient as bridgeclient

value = bridgeclient()

# **************************************************************************************************************************
# Ref: https://www.mathworks.com/help/thingspeak/update-channel-feed.html
#
# POST https://api.thingspeak.com/update.json
# api_key = R4P5W2047WSYO8S8
# field1 = 19
#
# https://thingspeak.com/apps/plugins/141502
# **************************************************************************************************************************

ApiKey = "QBII1VEG5VZ5WB7N"

def post_to_thingspeak(payload):
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("api.thingspeak.com:80")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/update", payload, headers)
    response = conn.getresponse()
    print( response.status, response.reason, payload, time.strftime("%c"))
    data = response.read()
    conn.close()

while True:
    h0 = value.get("h")
    t0 = value.get("t")
    params = urllib.urlencode({'field1': t0, 'field2': h0, 'key': ApiKey})
    post_to_thingspeak(params)
    time.sleep(10)