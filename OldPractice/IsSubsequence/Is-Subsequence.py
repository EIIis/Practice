# https://leetcode.com/problems/is-subsequence/
# Valid String Subsequence
def isSubsequence(self, s, t):
    arr = 0
    seq = 0
    while arr < len(t) and seq < len(s):
        if t[arr] == s[seq]:
            seq += 1
        arr += 1
    return seq == len(s)

# https://www.algoexpert.io/questions/Validate%20Subsequence
# Valid Array Subsequence
def isValidSubsequence(array, sequence):
    sequenceIndx = 0 # Creating an int variable to keep count of which inde
    for i in array: # Iterating through our main array strating from the start
		if sequenceIndx == len(sequence): # Compares out sequence index to the length of the subarray
			break
		elif sequence[sequenceIndx] == i:
			sequenceIndx += 1
    return sequenceIndx == len(sequence)
