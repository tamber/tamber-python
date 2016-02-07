# Tamber API Client for Python

You can sign up for a Tamber account at https://tamber.com.

For full API documentation, refer to https://tamber.com/docs/api.

Installation
============

```sh
pip install --upgrade tamber
```

or

```sh
easy_install --upgrade tamber
```

See http://www.pip-installer.org/en/latest/index.html for instructions
on installing pip. If you are on a system with easy_install but not
pip, you can use easy_install instead. If you're not using virtualenv,
you may have to prefix those commands with `sudo`. You can learn more
about virtualenv at http://www.virtualenv.org/


Compatibility
=============

We are compatible with Python 2.6+, Python 3.1+ and PyPy


Usage
=====

Track Events in real time:

```python
import tamber

tamber.api_key = '80r2oX10Uw4XfZSxfh4O'

try:
	event = tamber.Event.track(
		user='user_rlox8k927z7p',
		behavior='like',
		item='item_wmt4fn6o4zlk'
	)
	print event
except tamber.TamberError as err:
	print err
```

Get recommendations:

```python
import tamber

tamber.api_key = '80r2oX10Uw4XfZSxfh4O'

try:
	recs = tamber.Discover.recommended(
		user='user_rlox8k927z7p',
	)
	for rec in recs:
    	print "item:%s  score%s\n" % (rec['item'], rec['score'])
    	
except tamber.TamberError as err:
	print err
```

See [test.py](https://github.com/tamber/tamber-python/blob/master/test/test.py) for more examples.

