# Tamber API Python Client Library
# Authors:
# Mark Canning <argusdusty@tamber.com>

from tamber import util

class Property(util.Resource):
	def __init__(self, name=None, type=None, created=None):
		self.name = name
		self.type = type
		self.created = created

	@classmethod
	def _url(cls, command):
		return cls._get_url('property', command)

	def create(self, **params):
		self._call_api('POST', self._url('create'), params)

	def retrieve(self, **params):
		keys = {'name'}
		self._call_api('GET', self._url('retrieve'), params, keys)

	def remove(self, **params):
		keys = {'name'}
		self._call_api('POST', self._url('remove'), params, keys)