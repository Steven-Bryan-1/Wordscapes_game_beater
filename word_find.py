
letters_to_find = input("enter the letters that you are looking for:")


#lists of 3,4, and 5 from the dictionary
list3 = []
list4 = []
list5 = []
list6 = []

# lists of words that match criteria
list3_updated = []
list4_updated = []
list5_updated = []
list6_updated = []

count = 0

text_file = open(r'C:\path\to\Dictionary\Oxford.txt', 'r')
lines = text_file.readlines()

#one more because of the way its stored.  so 4 instead of 3 for a 3 letter word
for word in lines:
	if len(word) == 4:
		list3.append(word.strip())
	if len(word) == 5:
		list4.append(word.strip())
	if len(word) == 6:
		list5.append(word.strip())
	if len(word) == 7:
		list6.append(word.strip())



for new_word in list3:
	count = 0
	for letter in new_word:
		if letter not in letters_to_find:
			count = 1
		if count == 1: 
			break
	if count == 0:
		list3_updated.append(new_word)


#for new_word in list3:
#	count = 0
#	for letter in letters_to_find:		
#		if letter in new_word:
#			count = count + 1
			
#		if count == 3:
#			list3_updated.append(new_word)
#			count = 0
	

for new_word in list4:
	count = 0
	for letter in new_word:
		if letter not in letters_to_find:
			count = 1
		if count == 1: 
			break
	if count == 0:
		list4_updated.append(new_word)

for new_word in list5:
	count = 0
	for letter in new_word:
		if letter not in letters_to_find:
			count = 1
		if count == 1: 
			break
	if count == 0:
		list5_updated.append(new_word)

for new_word in list6:
	count = 0
	for letter in new_word:
		if letter not in letters_to_find:
			count = 1
		if count == 1: 
			break
	if count == 0:
		list6_updated.append(new_word)

	

print("3 letter words:")
print(list3_updated)
print("4 letter words:") 
print(list4_updated)
print("5 letter words:")
print(list5_updated)
print("6 letter words:")
print(list6_updated)
