import tamber

def basic_test():

	print "event/track\n"

	try:
		tamber.Event.track(
			user='user_jctzgisbru', 
			item='item_i5gq90scc1', 
			behavior='mention'
		)
	except tamber.TamberError as e:
		print e

	print "\ndiscover/recommended\n"

	try:
		d = tamber.Discover.recommended(user='user_jctzgisbru',number=100,)
		print d
		for rec in d:
			print "item:%s  score%s\n" % (rec['item'],rec['score'])
	except tamber.TamberError as e:
		print e

def partial_test():
	try:
		tamber.Event.batch(
			events=[
				tamber.Event(
					user='user_fwu592pwmo', 
					item='item_u9nlytt3w5', 
					behavior='mention',
					value=1
				),
				tamber.Event(
					user='user_jctzgisbru', 
					item='item_i5gq90scc1', 
					behavior='mention',
					value= 1
				)
			]
		)
	except tamber.TamberError as e:
		print e



print "Running Tests...."

tamber.project_key = 'Mu6DUPXdDYe98cv5JIfX'
tamber.engine_key = 'SbWYPBNdARfIDa0IIO9L'

print "Basic Test:\n"

basic_test()

print "Partial Test:\n"

partial_test()


print "\n\n=================\nTesting Complete\n=================\n\n"
