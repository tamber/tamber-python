from tamber import util

class Item(util.Resource):
	def __init__(self, id=None, properties=None, tags=None, created=None):
		self.id = id
		self.properties = properties
		self.tags = tags
		self.created = created

	@classmethod
	def _url(cls, command):
		return cls._get_url('item', command)

	def create(self, **params):
		self._call_api('POST', self._url('create'), params)

	def addProperties(self, **params):
		keys = {'id', 'properties'}
		self._call_api('POST', self._url('addProperties'), params, keys)

	def removeProperties(self, **params):
		keys = {'id', 'properties'}
		self._call_api('POST', self._url('removeProperties'), params, keys)

	def addTags(self, **params):
		keys = {'id', 'tags'}
		self._call_api('POST', self._url('addTags'), params, keys)

	def removeTags(self, **params):
		keys = {'id', 'tags'}
		self._call_api('POST', self._url('removeTags'), params, keys)

	def retrieve(self, **params):
		keys = {'id'}
		self._call_api('GET', self._url('retrieve'), params, keys)

	def remove(self, **params):
		keys = {'id'}
		self._call_api('POST', self._url('remove'), params, keys)