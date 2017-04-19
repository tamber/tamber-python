import tamber

tamber.project_key = 'Mu6DUPXdDYe98cv5JIfX'

# Track an Event
try:
	event = tamber.Event.track(
		user='user_rlox8k927z7p',
		behavior='like',
		item='item_wmt4fn6o4zlk'
	)
	print(event)
except tamber.TamberError as err:
	print(err)

tamber.engine_key = 'SbWYPBNdARfIDa0IIO9L'

# Get Recommendations
try:
	recs = tamber.Discover.recommended(
		user='user_rlox8k927z7p',
	)
	for rec in recs:
    	print("item:%s  score%s\n" % (rec['item'], rec['score']))
    	
except tamber.TamberError as err:
	print(err)