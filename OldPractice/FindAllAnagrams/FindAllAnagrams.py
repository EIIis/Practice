# From the Lyft Webinar "Lyft ETA Program CS Fundamentals"
# Given a list of words and a string, return a list of words that is an anagram of the given string

def list_anagrams(strings, input):
    results = [] 
    input_dict = build_dictionary(input)

    for string in strings:
        string_dict = build_dictionary(string)
        if input_dict == string_dict:
            results.append(string)

    return results

def is_anagram(word1, word2):
    dict1 = build_dictionary(word1)
    dict2 = build_dictionary(word2)
    return dict1 == dict2

def build_dictionary(word):
    dict = {}
    for letter in word:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict

# BONUS
def find_all_anagrams(strings):
    result = {}
    for string in strings:
        result[string] = list_anagrams(strings, string)
    return result

# assert list_anagrams(['race', 'car', 'care', 'taco', 'coat'], 'caot') == ['taco', 'coat']

# assert is_anagram('taco', 'coat') == True
# assert is_anagram('sheesh', 'trash') == False
# assert is_anagram('race', 'care') == True
# assert is_anagram('tar', 'rat') == True
# assert is_anagram('tear', 'care') == False

# BONUS Assert
assert find_all_anagrams(['race', 'car', 'care', 'taco', 'coat']) == {
    'race': ['race', 'care'],
    'car': ['car'],
    'care': ['race', 'care'],
    'taco': ['taco', 'coat'],
    'coat': ['taco', 'coat'],
}

print('All tests passed!')
