"""
Input 4x4 letters and output any word in the 4x4 letter.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

# global variable
dictionary_list = []




def main():
	"""
	Make the input letters as the 4x4 matrix according to the function(find_the_word).
	"""
	read_dictionary()
	a = (input('1 row of letters: ')).lower()
	if len(a.strip()) != 7:
		print('Illegal input')
		return False
	b = (input('2 row of letters: ')).lower()
	if len(b.strip()) != 7:
		print('Illegal input')
		return False
	c = (input('3 row of letters: ')).lower()
	if len(c.strip()) != 7:
		print('Illegal input')
		return False
	d = (input('4 row of letters: ')).lower()
	if len(d.strip()) != 7:
		print('Illegal input')
		return False
	list_a = [a.split(), b.split(), c.split(), d.split()]
	aim = find_the_words(list_a)
	print('There are '+str(len(aim))+' words in total.')


def find_the_words(lst):
	aim_lst = []
	for x in range(4):
		for y in range(4):
			helper(lst, str(lst[x][y]), x, y, [(x, y)], aim_lst)
	return aim_lst


def helper(lst_l, word, x, y, choose_list, aim_lst):
	for i in range(-1, 2):
		for j in range(-1, 2):
			if 0 <= x + i < 4:
				if 0 <= y + j < 4:
					if (x+i, y+j) not in choose_list:
						# choose
						ch = lst_l[x+i][y+j]
						choose_tuple = (x+i, y+j)
						choose_list.append(choose_tuple)
						word += ch
						if word not in aim_lst and word in dictionary_list and len(word) >= 4:
							aim_lst.append(word)
							print('Found \"'+str(word)+'\"')
						# explore
						if has_prefix(word):
							helper(lst_l, word, x+i, y+j, choose_list, aim_lst)
						# un-choose
						word = word[:len(word) - 1]
						choose_list.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global dictionary_list
	with open(FILE, 'r') as f:
		for line in f:
			dictionary_list.append(line.strip())


def has_prefix(ch):
	"""
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary_list:
		if word.startswith(ch):
			return True
	return False


if __name__ == '__main__':
	main()
