import sys
import json
import base64
import tamber

PYTHON_VERSION = sys.version_info[0]

if PYTHON_VERSION == 2:
    from urllib2 import urlopen, Request, HTTPError, URLError
    from urllib import urlencode
    b64encode = lambda s: base64.b64encode(s.encode('ascii'))
elif PYTHON_VERSION == 3:
    from urllib.request import urlopen, Request
    from urllib.error import HTTPError, URLError
    from urllib.parse import urlencode
    b64encode = lambda s: base64.b64encode(s.encode('ascii')).decode('ascii')

def call_api(method, url, api_url=None, project_key=None, engine_key=None, timeout=None, **params):
    if api_url is None:
        api_url = tamber.get_api_url()
    if project_key is None:
        project_key = tamber.get_project_key()
    if engine_key is None:
        engine_key = tamber.get_engine_key()
    if timeout is None:
        timeout = params.get('timeout') or tamber.get_timeout()

    url = api_url + url
    encoded_params = urlencode(params)
    data = None
    headers = dict()

    if method == 'POST':
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        data = encoded_params
        if PYTHON_VERSION == 3:
            data = data.encode("utf-8")
    elif method == 'GET':
        url += '?' + encoded_params

    api_version = tamber.get_api_version()
    if api_version != None:
        headers['Tamber-Version'] = api_version
    headers['User-Agent'] = 'Tamber/v1 PythonBindings/%s' % tamber.version_str()
    headers['Authorization'] = 'Basic %s' % b64encode(project_key+':'+engine_key)

    req = Request(url, data=data, headers=headers)

    try:
        resp = urlopen(req, timeout=timeout)
    except HTTPError as e:
        resp = e
    except URLError as e:
        raise tamber.error.TamberError(
            message="Unexpected timeout error. If this problem persists, let us know at support@tamber.com.", 
            is_timed_out_error=True
            )
    if PYTHON_VERSION < 3:
        data = json.load(resp)
    else:
        respDecoded = resp.read().decode('utf-8')
        try:
            data = json.loads(respDecoded)
        except Exception as e:
            print(data)
            raise e

    if data['success'] is False:
        raise tamber.error.TamberError(data['error'])
    return data['result']
