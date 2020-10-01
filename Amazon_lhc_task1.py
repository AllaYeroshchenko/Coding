# #----------  problem  ----------#
# Given a pattern of letters (ex: "aba"), and a sentence fragment (ex: "arm over arm"),
# write a method which outputs true if the sentence matches the pattern and false otherwise.

# #----------  method signature  ----------#
# public boolean sentenceMatchesPattern(String pattern, String sentence)

# #----------  examples  ----------#

# pattern: "aa"
# sentence: "hey hey"
# output: true

# pattern: "aaa"
# sentence: "hey hey hey"
# output: true

# pattern: "abc"
# sentence: "how are you"
# output: true

# pattern: "aba"
# sentence: "arm over arm"
# output: true

# pattern: "abcdefab"
# sentence: "next time there won't be a next time"
# output: true

# pattern: "ab"
# sentence: "hey hey"
# output: false

# pattern: "aba"
# sentence: "how are you"
# output: false

def sentenceMatchesPattern(pattern, sentence):
	pattern_list=list(pattern)
	sentence_list=sentence.split(" ")
	if len(pattern_list)!=len(sentence_list):
		return False
	associations={}
	associations[pattern_list[0]]=sentence_list[0]
	for i in range(1, len(pattern_list)):
		if pattern_list[i] in associations:
			if associations[pattern_list[i]]!=sentence_list[i]:
				return False	
		else:
			if sentence_list[i] not in associations.values(): 	
				associations[pattern_list[i]]=sentence_list[i]
			else:
				return False	

	return True



print(sentenceMatchesPattern("abcdefab", "next time there won't be a next time"))
print(sentenceMatchesPattern("aa", "bay g bay"))