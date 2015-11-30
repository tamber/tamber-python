import tamber

tamber.api_key = '80r2oX10Uw4XfZSxfh4O'
item = tamber.Item(id='68753A444D6F', properties={'height': 23.4}, tags=['amazing', 'rustic'], created=1446417346)
item.create()

print(item.__dict__)