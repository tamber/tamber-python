from tamber import api_url, api
import json
import warnings

def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emmitted
    when the function is used."""
    def newFunc(*args, **kwargs):
        warnings.warn("Call to deprecated function %s." % func.__name__,
                      category=DeprecationWarning)
        return func(*args, **kwargs)
    newFunc.__name__ = func.__name__
    newFunc.__doc__ = func.__doc__
    newFunc.__dict__.update(func.__dict__)
    return newFunc

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
            if isinstance(params[k], dict) or isinstance(params[k], list) or isinstance(params[k], TamberObject):
                params[k] = json.dumps(params[k], cls=TamberJSONEncoder)
        if keys:
            reserved = {'api_url', 'project_key', 'engine_key', 'timeout'}
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

class ListableAPIResource(APIResource):
    @classmethod
    def list(cls, **params):
        url = cls._url_path('list')
        return cls._call_api('POST', url, **params)

# event/track, user/create, user/update, user/retrieve
class GetRecs(TamberObject):
    def __init__(self, number=None, page=None, exclude_items=None, variability=None, filter=None, get_properties=None):
        self.number = number
        self.page = page
        self.exclude_items = exclude_items
        self.variability = variability
        self.filter = filter
        self.get_properties = get_properties

class Event(APIResource, TamberObject):
    name = 'event'
    def __init__(self, user=None, item=None, behavior=None, amount=None, hit=False, context=None, created=None):
        self.user = user
        self.item = item
        self.behavior = behavior
        self.amount = amount
        self.hit = hit
        self.context = context
        self.created = created

    @classmethod
    def track(cls, **params):
        keys = {'user', 'item', 'behavior', 'amount', 'hit', 'context', 'created'}
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

    # Meta methods
    @classmethod
    def metaLike(cls, **params):
        keys = {'user', 'property', 'value', 'amount'}
        return cls._call_api('POST', cls._url_path('meta/like'), keys, **params)

    @classmethod
    def metaUnlike(cls, **params):
        keys = {'user', 'property', 'value'}
        return cls._call_api('POST', cls._url_path('meta/unlike'), keys, **params)


class Discover(APIResource):
    name = 'discover'

    @classmethod
    def recommended(cls, **params):
        keys = {'user', 'number', 'exclude_items', 'variability', 'filter', 'get_properties', 'continuation', 'no_create'}
        return cls._call_api('GET', cls._url_path('recommended'), keys, **params)

    @classmethod
    def next(cls, **params):
        keys = {'user', 'item', 'number', 'exclude_items', 'variability', 'filter', 'get_properties', 'continuation', 'no_create'}
        return cls._call_api('GET', cls._url_path('next'), keys, **params)

    @classmethod
    def weekly(cls, **params):
        keys = {'user', 'number', 'exclude_items', 'filter', 'get_properties', 'no_create'}
        return cls._call_api('GET', cls._url_path('weekly'), keys, **params)

    @classmethod
    def daily(cls, **params):
        keys = {'user', 'number', 'exclude_items', 'filter', 'get_properties', 'no_create'}
        return cls._call_api('GET', cls._url_path('daily'), keys, **params)

    @classmethod
    def meta(cls, **params):
        keys = {'property', 'user', 'item', 'number', 'variability', 'no_create'}
        return cls._call_api('GET', cls._url_path('meta'), keys, **params)

    @classmethod
    def popular(cls, **params):
        keys = {'number', 'page', 'filter', 'get_properties'}
        return cls._call_api('GET', cls._url_path('popular'), keys, **params)

    @classmethod
    def hot(cls, **params):
        keys = {'number', 'page', 'filter', 'get_properties'}
        return cls._call_api('GET', cls._url_path('hot'), keys, **params)

    @classmethod
    def trending(cls, **params):
        """ Beta testing """
        keys = {'period', 'period_mode', 'number', 'page', 'get_properties'}
        return cls._call_api('GET', cls._url_path('trending'), keys, **params)

    @classmethod
    def uac(cls, **params):
        keys = {'number', 'page', 'filter', 'get_properties'}
        return cls._call_api('GET', cls._url_path('uac'), keys, **params)

    @classmethod
    def userPopular(cls, **params):
        keys = {'number', 'page', 'filter', 'get_properties', 'user', 'no_create'}
        return cls._call_api('GET', cls._url_path('user_trend/popular'), keys, **params)

    @classmethod
    def userHot(cls, **params):
        keys = {'number', 'page', 'filter', 'get_properties', 'user', 'no_create'}
        return cls._call_api('GET', cls._url_path('user_trend/hot'), keys, **params)

    @classmethod
    def userUac(cls, **params):
        keys = {'number', 'page', 'filter', 'get_properties', 'user', 'no_create'}
        return cls._call_api('GET', cls._url_path('user_trend/uac'), keys, **params)

    @classmethod
    def basicRecommended(cls, **params):
        keys = {'user', 'number', 'page', 'filter', 'test_events', 'get_properties'}
        return cls._call_api('GET', cls._url_path('basic/recommended'), keys, **params)
        
    @classmethod
    def basicSimilar(cls, **params):
        keys = {'item', 'number', 'page', 'filter', 'test_events', 'get_properties'}
        return cls._call_api('GET', cls._url_path('basic/similar'), keys, **params)

    @classmethod
    def basicRecommendedSimilar(cls, **params):
        keys = {'user', 'item', 'number', 'page', 'filter', 'test_events', 'get_properties'}
        return cls._call_api('GET', cls._url_path('basic/recommended_similar'), keys, **params)


class User(CreateableAPIResource, UpdatableAPIResource, ListableAPIResource):
    name = 'user'

    @classmethod
    @deprecated
    def search(cls, **params):
        keys = {'filter'}
        return cls._call_api('GET', cls._url_path('list'), keys, **params)

    @classmethod
    def merge(cls, **params):
        keys = {'from', 'to', 'no_create'}
        return cls._call_api('POST', cls._url_path('merge'), keys, **params)

class Item(CreateableAPIResource, UpdatableAPIResource, ListableAPIResource):
    name = 'item'
    
    @classmethod
    def hide(cls, **params):
        url = cls._url_path('hide')
        keys = {'id'}
        return cls._call_api('POST', url, **params)

    @classmethod
    def unhide(cls, **params):
        url = cls._url_path('unhide')
        keys = {'id'}
        return cls._call_api('POST', url, **params)

    @classmethod
    def delete(cls, **params):
        url = cls._url_path('delete')
        keys = {'id'}
        return cls._call_api('POST', url, **params)

class Behavior(CreateableAPIResource):
    name = 'behavior'
