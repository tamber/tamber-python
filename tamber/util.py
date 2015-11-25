# Tamber API Python Client Library
# Authors:
# Mark Canning <argusdusty@tamber.com>

from tamber import api_url, api

class Resource:
	@staticmethod
	def _get_url(resource, command):
		return "%s/%s/%s" % (api_url, resource, command)

	def _get_args(self, params=None, keys=None):
		c = self.__dict__.copy()
		if params:
			c.update(params)
		if keys:
			return dict((k, c[k]) for k in c if k in keys)
		return c

	def _call_api(self, method, url, params=None, keys=None, update=True):
		args = self._get_args(params, keys)
		r = api.call_api(method, url, args)
		if update:
			self.update(**r)
		return self

	def update(self, **params):
		self.__dict__.update(params)