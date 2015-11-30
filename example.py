import tamber

tamber.api_key = ''
item = tamber.Item(id='', properties={'a': 2}, tags=['1', '2'], created=5)
item.create()

print(item.__dict__)