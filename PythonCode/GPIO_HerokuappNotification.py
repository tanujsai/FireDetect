import json
import urllib2
 
class RemoteAlert:
    def send(self, device_id, message ):
	data = { 'message' : message }
        url = 'http://remote-alert.herokuapp.com/post/' + device_id
        req = urllib2.Request( url )
        req.add_header('Content-Type', 'application/json')
        urllib2.urlopen(req, json.dumps(data))
        return 'OK'

ra = RemoteAlert()
dev_id = '#DeviceID'  # Get Device Id from Device Using Some Device Id
print ra.send(dev_id, 'Hellow Push Message World')
