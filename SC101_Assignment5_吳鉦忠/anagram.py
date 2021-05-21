"""
File: anagram.py
Name: Andy Wu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# global variable
dictionary_list = []
total_list = []
def main():
    read_dictionary()
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        s = input('Find anagrams for:')
        if s != EXIT:
            start = time.time()
            find_anagrams(s)
            end = time.time()
            print(str(len(total_list)) + ' anagrams: ' + str(total_list))
            print('Spend time:'+str(end-start)+' seconds')
        else:
            break
def read_dictionary():
    global dictionary_list
    with open(FILE, 'r') as f:
        for line in f:
            dictionary_list.append(line.strip())
def find_anagrams(s):
    find_anagrams_helper(s, [], total_list)
def find_anagrams_helper(s, aim_ch, total_list):
    if len(aim_ch) == len(s):
        word = ''
        for i in aim_ch:
            word += s[int(i)]
        if word in dictionary_list and word not in total_list:
            print('Searching...')
            print('Found: '+str(word))
            total_list.append(word)
    else:
        for j in range(len(s)):
            if j not in aim_ch:  # choose
                aim_ch.append(j)
                # explore
                if has_prefix(s, aim_ch):
                    find_anagrams_helper(s, aim_ch, total_list)
                # Un-choose
                aim_ch.pop()
def has_prefix(s, sub_s):
    ch = ''
    for i in sub_s:
        ch += s[i]
    for word in dictionary_list:
        if word.startswith(ch):
            return True
    return False




if __name__ == '__main__':
    main()

