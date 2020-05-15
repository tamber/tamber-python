# The MIT License (MIT)

# Copyright (c) 2020 Tamber, Inc.

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
api_version = None
timeout = 5.

def get_project_key():
    if project_key is None: return ""
    return project_key

def get_engine_key():
    if engine_key is None: return ""
    return engine_key

def get_api_version():
    return api_version

def get_timeout():
    return timeout

VERSION = (0, 2, 5) # Tamber API Python Client Library v0.2.3
version_str = lambda: 'v' + '.'.join(str(x) for x in VERSION)
api_url = 'https://api.tamber.com/v1'

def get_api_url():
    return api_url

from tamber.api import (
    call_api
)

from tamber.resource import (
    Event,
    Discover,
    User,
    Item,
    Behavior,
    GetRecs
)

from tamber.error import(
    TamberError
)
