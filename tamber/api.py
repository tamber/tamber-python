import sys
from tamber import version_str, api_key

PYTHON_VERSION = sys.version_info[0]

if PYTHON_VERSION == 2:
	from urllib2 import urlopen
	from urllib2 import Request
	from urllib import urlencode
elif PYTHON_VERSION == 3:
	from urllib.request import urlopen
	from urllib.request import Request
	from urllib.parse import urlencode

def call_api(method, url, args):
	args = (args or {})
	args['key'] = api_key
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
	headers['User-Agent'] = 'Tamber/Python/%s' % version_str()
	req = Request(url, data=data, headers=headers)
	resp = urlopen(req)
	if PYTHON_VERSION < 3:
		return json.load(resp)
	data = resp.readall().decode('utf-8')
	try:
		return json.loads(data)
	except Exception as e:
		print(data)
		raise e