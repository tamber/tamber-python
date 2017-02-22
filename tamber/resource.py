from tamber import api_url, api
import urllib
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
	@classmethod
	def class_name(cls):
		return str(urllib.quote_plus(cls.__name__.lower()))

	@classmethod
	def class_method_url(cls, method):
		cls_name = cls.class_name()
		return "%s/%s/%s" % (api_url,cls_name,method)

	@staticmethod
	def _get_url(resource, command):
		return "%s/%s/%s" % (api_url, resource, command)

	@classmethod
	def _get_args(cls, params=None, keys=None):
		for k in params:
			if isinstance(params[k], dict) or isinstance(params[k], list):
				params[k] = json.dumps(params[k], cls=TamberJSONEncoder)
		if keys:
			return dict((k, params[k]) for k in params if k in keys)
		return params

	@classmethod
	def _call_api(cls, method, url, params=None, keys=None):
		args = cls._get_args(params, keys)
		return api.call_api(method, url, args)

# item, user, behavior
class CreateableAPIResource(APIResource):

	@classmethod
	def create(cls, **params):
		url = cls.class_method_url('create') 
		return cls._call_api('POST', url, params)

	@classmethod
	def retrieve(cls, **params):
		url = cls.class_method_url('retrieve') 
		return cls._call_api('GET', url, params)

# item, user
class UpdatableAPIResource(APIResource):

	@classmethod
	def update(cls, **params):
		url = cls.class_method_url('update') 
		return cls._call_api('POST', url, params)

# item
class RemovableAPIResource(APIResource):
	@classmethod
	def remove(cls, **params):
		url = cls.class_method_url('remove') 
		return cls._call_api('POST', url, params)



class Event(APIResource, TamberObject):
	def __init__(self, user=None, item=None, behavior=None, value=None, created=None):
		self.user = user
		self.item = item
		self.behavior = behavior
		self.value = value
		self.created = created

	@classmethod
	def _url(cls, command):
		return cls._get_url('event', command)

	@classmethod
	def track(cls, **params):
		keys = {'user', 'item', 'behavior', 'value', 'created'}
		return cls._call_api('POST', cls.class_method_url('track'), params, keys)
	
	@classmethod
	def retrieve(cls, **params):
		keys = {'user', 'item', 'created_since', 'created_before', 'number'}
		cls._call_api('POST', self.class_method_url('retrieve'), params, keys)
	
	@classmethod
	def batch(cls, **params):
		keys = {'events'}
		cls._call_api('POST', cls.class_method_url('batch'), params, keys)


class Discover(APIResource):

    @classmethod
    def _url(cls, command):
        return cls._get_url('discover', command)

    @classmethod
    def recommended(cls, **params):
        keys = {'user', 'number', 'page', 'filter', 'test_events'}
        return cls._call_api('GET', cls._url('recommended'), params, keys)

    @classmethod
    def similar(cls, **params):
        keys = {'item', 'number', 'page', 'filter', 'test_events'}
        return cls._call_api('GET', cls._url('similar'), params, keys)

    @classmethod
    def recommendedSimilar(cls, **params):
        keys = {'user', 'item', 'number', 'page', 'filter', 'test_events'}
        return cls._call_api('GET', cls._url('recommended_similar'), params, keys)

    @classmethod
    def popular(cls, **params):
        keys = {'number', 'page', 'filter'}
        return cls._call_api('GET', cls._url('popular'), params, keys)

    @classmethod
    def hot(self, **cls):
        keys = {'number', 'page', 'filter'}
        return cls._call_api('GET', cls._url('hot'), params, keys)

class User(CreateableAPIResource, UpdatableAPIResource):
	pass

class Item(CreateableAPIResource, UpdatableAPIResource, RemovableAPIResource):
	pass

class Behavior(CreateableAPIResource):
	pass
