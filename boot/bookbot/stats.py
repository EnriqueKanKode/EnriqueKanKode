def sort_on(items: tuple[str, int]) -> int:
    return items[1]

def sort_list(char_count):
	char_list = []
	for char in char_count:
		char_list.append({"name" : char, "num" : char_count[char]})
	
	char_list.sort(reverse=True, key=sort_on)
	return char_list

def wordcount(bookcontent):
	wordlist = bookcontent.split()
	wordcount = int(len(wordlist))
	return wordcount 

def char_count(bookcontent):
	char_count = {}
	content_lower = bookcontent.lower()
	for char in content_lower:
		if char.isalpha():
			if char not in char_count:
				char_count[char] = 1
			else:
				char_count[char] += 1
	return sort_list(char_count)



