from tamber import util

class Actor(util.Resource):
	def __init__(self, id=None, behaviors=None, created=None):
		self.id = id
		self.behaviors = behaviors
		self.created = created

	@classmethod
	def _url(cls, command):
		return cls._get_url('actor', command)

	def create(self, **params):
		self._call_api('POST', self._url('create'), params)

	def addBehaviors(self, **params):
		keys = {'id', 'behaviors', 'getRecs'}
		self._call_api('POST', self._url('addBehaviors'), params, keys)

	def removeBehaviors(self, **params):
		keys = {'id', 'behaviors', 'getRecs'}
		self._call_api('POST', self._url('removeBehaviors'), params, keys)

	def retrieve(self, **params):
		keys = {'id', 'getRecs'}
		self._call_api('GET', self._url('retrieve'), params, keys)

	def remove(self, **params):
		keys = {'id'}
		self._call_api('POST', self._url('remove'), params, keys)