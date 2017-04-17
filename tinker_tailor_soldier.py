

def next_child(children, current_child):
	if current_child == children[-1] or current_child == None: 
		return children[0]
	
	else:
		child_index = children.index(current_child)
		return children[child_index + 1]

def rhyme(children, number_of_syllables, current_child):
	for syllable in range(number_of_syllables - 1):
		current_child = next_child(children, current_child)
	return current_child

def game(number_of_children, number_of_syllables):
	children = range(1, number_of_children + 1)
	current_child = children[0]
	losers = []
	while len(children) > 0:
		loser = rhyme(children, number_of_syllables, current_child)
		current_child = next_child(children, loser)
		children.remove(loser)
		losers.append(loser)
	return losers

print(game(5, 3))





