import json

class Filter(dict):
    def __init__(self, function=None, *args):
        if function == 'property':
            self[function] = args[0]
        else:
            self[function] = list(args)

    def __str__(self):
        return json.dumps(self)

And = lambda *args: Filter('and', *args)
Or = lambda *args: Filter('or', *args)
Gt = lambda *args: Filter('gt', *args)
Gte = lambda *args: Filter('gte', *args)
Lt = lambda *args: Filter('lt', *args)
Lte = lambda *args: Filter('lte', *args)
Eq = lambda *args: Filter('eq', *args)
Neq = lambda *args: Filter('neq', *args)
Not = lambda arg: Filter('not', arg)
Contains = lambda *args: Filter('contains', *args)
Overlaps = lambda *args: Filter('overlaps', *args)
Property = lambda property: Filter('property', property)
Tags = lambda tags: Filter('tags', *[])