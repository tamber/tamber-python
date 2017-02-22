import sys
import json
import base64
import tamber


PYTHON_VERSION = sys.version_info[0]

if PYTHON_VERSION == 2:
	from urllib2 import urlopen
	from urllib2 import Request
	from urllib import urlencode
	b64encode = lambda s: base64.b64encode(s.encode('ascii'))
elif PYTHON_VERSION == 3:
	from urllib.request import urlopen
	from urllib.request import Request
	from urllib.parse import urlencode
	b64encode = lambda s: base64.b64encode(s.encode('ascii')).decode('ascii')

def call_api(method, url, args):
	args = (args or {})
	encoded_params = urlencode(args)
	data = None
	headers = dict()
	if method == 'POST':
		headers['Content-Type'] = 'application/x-www-form-urlencoded'
		data = encoded_params
		if PYTHON_VERSION == 3:
			data = data.encode("utf-8")
	elif method == 'GET':
		url += '?' + encoded_params
	headers['User-Agent'] = 'Tamber/Python/%s' % tamber.version_str()
	headers['Authorization'] = 'Basic %s' % base64.b64encode(tamber.get_project_key()+':'+tamber.get_engine_key())
	req = Request(url, data=data, headers=headers)

	resp = urlopen(req)
	if PYTHON_VERSION < 3:
		data = json.load(resp)
	else:
		respDecoded = resp.readall().decode('utf-8')
		try:
			data = json.loads(respDecoded)
		except Exception as e:
			print(data)
			raise e

	if data['success'] is False:
		raise tamber.error.TamberError(data['error'])
	return data['result']
