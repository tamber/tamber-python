# Tamber API Python Client Library
# Authors:
# Mark Canning <argusdusty@tamber.com>

from tamber import util

class Discover(util.Resource):
	def __init__(self, number=None, page=None, filter=None):
		self.number = number
		self.page = page
		self.filter = filter
		pass

	@classmethod
	def _url(cls, command):
		return cls._get_url('discover', command)

	def getRecommended(self, **params):
		keys = {'id', 'number', 'page', 'filter'}
		self._call_api('GET', self._url('getRecommended'), params, keys)

	def getSimilar(self, **params):
		keys = {'id', 'number', 'page', 'filter'}
		self._call_api('GET', self._url('getSimilar'), params, keys)

	def getRecommendedSimilar(self, **params):
		keys = {'actor', 'item', 'number', 'page', 'filter'}
		self._call_api('GET', self._url('getRecommendedSimilar'), params, keys)

	def getPopular(self, **params):
		keys = {'number', 'page', 'filter'}
		self._call_api('GET', self._url('getPopular'), params, keys)

	def getHot(self, **params):
		keys = {'number', 'page', 'filter'}
		self._call_api('GET', self._url('getHot'), params, keys)