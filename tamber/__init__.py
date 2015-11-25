# Tamber API Python Client Library
# Authors:
# Mark Canning <argusdusty@tamber.com>

api_key = None
api_url = 'https://dev.tamber.com/v1'

VERSION = (0, 1) # Tamber API Python Client Library v0.1
version_str = lambda: 'v' + '.'.join(str(x) for x in VERSION)

from tamber.item import Item
from tamber.actor import Actor
from tamber.discover import Discover
from tamber.behavior import Behavior
from tamber.property import Property
from tamber.filter import Filter

from tamber.api import (
	call_api
)

from tamber.util import (
	Resource
)