# The MIT License (MIT)

# Copyright (c) 2015 Tamber, Inc.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

project_key = None
engine_key = None
api_url = 'https://api.tamber.com/v1'

def get_project_key():
	return project_key

def get_engine_key():
	return engine_key

VERSION = (0, 1, 1) # Tamber API Python Client Library v0.1.0
version_str = lambda: 'v' + '.'.join(str(x) for x in VERSION)

from tamber.api import (
	call_api
)

from tamber.resource import (
	Event,
	Discover,
	User,
	Item,
	Behavior
)

from tamber.error import(
	TamberError
)
