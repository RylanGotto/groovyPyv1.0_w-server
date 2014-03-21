def split(message):
	print message
	val = message.index('$')
	subval = val
	subval -= 1
	val += 1
	instruction = message[val:]
	terms = message[:subval]
	return {'instruction': instruction, 'terms': terms }