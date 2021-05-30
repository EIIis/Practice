# https://www.algoexpert.io/questions/First%20Non-Repeating%20Character
def firstNonRepeatingCharacter(string):
	hm = {}
	for i in string:
		if i in hm:
			hm[i] += 1
		else:
			hm[i] = 1
		
	i = 0
	for letter in string:
		if hm[letter] == 1:
			return i
		i += 1
	return -1