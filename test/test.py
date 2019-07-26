import tamber

def basic_test():
    print("event/track\n")

    try:
        e = tamber.Event.track(
            user='user_jctzgisbru', 
            item='item_i5gq90scc1', 
            behavior='mention',
            hit=True,
            context={
                "page": "detail-view",
                "section": "recommended"
            }
        )
        print(e)
    except tamber.TamberError as e:
        print(e)


    print("\ndiscover/recommended\n")

    try:
        d = tamber.Discover.recommended(user='user_jctzgisbru',number=10)
        print(d)
        for rec in d:
            print("item:%s  score:%s\n" % (rec['item'],rec['score']))
    except tamber.TamberError as e:
        print(e)

    print("\ndiscover/next\n")

    try:
        d = tamber.Discover.next(user='user_jctzgisbru',item='item_i5gq90scc1',number=20)
        print(d)
        for rec in d:
            print("item:%s  score:%s\n" % (rec['item'],rec['score']))
    except tamber.TamberError as e:
        print(e)

def partial_test():
    try:
        print(tamber.Item.create(
            id='item_faa666arma',
            properties={
                'clothing_type': 'pants',
                'stock':         90,
            },
            tags=['casual', 'feminine']
        ))
    except tamber.TamberError as e:
        print(e)

    try:
        print(tamber.Item.retrieve(
            id='item_faa666arma',
        ))
    except tamber.TamberError as e:
        print(e)

    try:
        print(tamber.Item.update(
            id='item_faa666arma',
            updates={
                'add': {
                    'properties': {'stock': 89}
                }
            }
        ))
    except tamber.TamberError as e:
        print(e)

    # try:
    #     print(tamber.User.search(filter={'age': 30}))
    # except tamber.TamberError as e:
    #     print(e)


print("Running Tests...")

tamber.project_key = 'Mu6DUPXdDYe98cv5JIfX'
tamber.engine_key = 'SbWYPBNdARfIDa0IIO9L'

print("Basic Test:\n")

basic_test()

print("Partial Test:\n")

partial_test()

print("\n\n=================\nTesting Complete\n=================\n\n")
