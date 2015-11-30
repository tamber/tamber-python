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

example.py

```python
import tamber

tamber.api_key = '80r2oX10Uw4XfZSxfh4O'
item = tamber.Item(id='68753A444D6F', properties={'height': 23.4}, tags=['amazing', 'rustic'], created=1446417346)
item.create()

print(item.__dict__)
```

See [examples.py](https://github.com/tamber/tamber-python/blob/master/examples.py) for more examples.

