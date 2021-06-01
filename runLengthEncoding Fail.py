def runLengthEncoding(string):
	hm = {}
	newStr = ""
	
	for i in string: # Running a for-loop to add characters of the string to the hashmap 
		if i in hm:
			hm[i] += 1
		else:
			hm[i] = 1
	
	for i in string:
		if i in hm:
			if hm[i] > 9:
				hm[i] -= 9
				newStr += str(9) + i
			else:
				newStr += str(hm[i]) + i
				hm.pop(i)
		
	return newStr
		
