from tamber import api_url, api
import json

class TamberObject():
	def __init__(self, *args, **kwargs):
		super(TamberObject, self).__init__(*args, **kwargs)

class TamberJSONEncoder(json.JSONEncoder):
	def default(self, obj):
		if not isinstance(obj, TamberObject):
			return super(TamberJSONEncoder, self).default(obj)
		return obj.__dict__

class APIResource():
	@staticmethod
	def _get_url_path(resource, command):
		return "/%s/%s" % (resource, command)

	@classmethod
	def _url_path(cls, method):
		return cls._get_url_path(cls.name, method)

	@classmethod
	def _flatten_args(cls, keys=None, **params):
		for k in params:
			if isinstance(params[k], dict) or isinstance(params[k], list):
				params[k] = json.dumps(params[k], cls=TamberJSONEncoder)
		if keys:
			reserved = {'api_url', 'project_key', 'engine_key'}
			return dict((k, params[k]) for k in params if k in keys or k in reserved)
		return params

	@classmethod
	def _call_api(cls, method, url, keys=None, **params):
		args = cls._flatten_args(keys, **params)
		return api.call_api(method, url, **args)

# item, user, behavior
class CreateableAPIResource(APIResource):
	@classmethod
	def create(cls, **params):
		url = cls._url_path('create') 
		return cls._call_api('POST', url, **params)

	@classmethod
	def retrieve(cls, **params):
		url = cls._url_path('retrieve') 
		return cls._call_api('GET', url, **params)

# item, user
class UpdatableAPIResource(APIResource):
	@classmethod
	def update(cls, **params):
		url = cls._url_path('update') 
		return cls._call_api('POST', url, **params)

# item
class RemovableAPIResource(APIResource):
	@classmethod
	def remove(cls, **params):
		url = cls._url_path('remove') 
		return cls._call_api('POST', url, **params)

class Event(APIResource, TamberObject):
	name = 'event'
	def __init__(self, user=None, item=None, behavior=None, value=None, hit=False, context=None, created=None):
		self.user = user
		self.item = item
		self.behavior = behavior
		self.value = value
		self.hit = hit
		self.context = context
		self.created = created

	@classmethod
	def track(cls, **params):
		keys = {'user', 'item', 'behavior', 'value', 'hit', 'context', 'created'}
		return cls._call_api('POST', cls._url_path('track'), keys, **params)

	@classmethod
	def retrieve(cls, **params):
		keys = {'user', 'item', 'behavior', 'created_since', 'created_before', 'number'}
		if 'before' in params:
			params['created_before'] = params['before']
		if 'since' in params:
			params['created_since'] = params['since']
		return cls._call_api('POST', cls._url_path('retrieve'), keys, **params)
	
	@classmethod
	def batch(cls, **params):
		keys = {'events'}
		return cls._call_api('POST', cls._url_path('batch'), keys, **params)

class Discover(APIResource):
	name = 'discover'
	@classmethod
	def recommended(cls, **params):
		keys = {'user', 'number', 'page', 'filter', 'test_events', 'get_properties'}
		return cls._call_api('GET', cls._url_path('recommended'), keys, **params)

	@classmethod
	def similar(cls, **params):
		keys = {'item', 'number', 'page', 'filter', 'test_events', 'get_properties'}
		return cls._call_api('GET', cls._url_path('similar'), keys, **params)

	@classmethod
	def recommendedSimilar(cls, **params):
		keys = {'user', 'item', 'number', 'page', 'filter', 'test_events', 'get_properties'}
		return cls._call_api('GET', cls._url_path('recommended_similar'), keys, **params)

	@classmethod
	def popular(cls, **params):
		keys = {'number', 'page', 'filter', 'get_properties'}
		return cls._call_api('GET', cls._url_path('popular'), keys, **params)

	@classmethod
	def hot(cls, **params):
		keys = {'number', 'page', 'filter', 'get_properties'}
		return cls._call_api('GET', cls._url_path('hot'), keys, **params)

class User(CreateableAPIResource, UpdatableAPIResource):
	name = 'user'

	@classmethod
	def search(cls, **params):
		keys = {'filter'}
		return cls._call_api('GET', cls._url_path('search'), keys, **params)

	@classmethod
	def merge(cls, **params):
		keys = {'from', 'to', 'no_create'}
		return cls._call_api('POST', cls._url_path('merge'), keys, **params)

class Item(CreateableAPIResource, UpdatableAPIResource, RemovableAPIResource):
	name = 'item'

class Behavior(CreateableAPIResource):
	name = 'behavior'
