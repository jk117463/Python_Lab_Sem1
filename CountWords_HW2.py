file_path= 'Words.txt'

my_file = open(file_path, 'r')
lines = my_file.readlines()

wordlist = {'_filtered_out':0}
i=0
valid = False
print('\nInput Lines')
for line in lines:
    print('{}: {}'.format(i,line), end='')
    linesplit = line.split()
    for word in linesplit:
        valid = False
        if (word.isalpha()):
            valid = True
        else:
            word_new = ''
            for c in word:
                if (c.isalpha() or (c == '\'' and word[0] != '\'')):
                    word_new = word_new + c
                    valid = True
                else:
                    break
            word = word_new
        if (len(word) == 1):
            valid = False
        if(valid == True):
            word = word.lower()
            if word in wordlist:
                wordlist[word] = wordlist[word] + 1
            else:
                wordlist.update({word: 1})
        else:
            wordlist['_filtered_out'] = wordlist['_filtered_out'] + 1
    i = i+1
my_file.close()
print('\n\nOutput - word counts')
wordlist.pop('_filtered_out')
for k in wordlist.keys():
    print('{}:{}'.format(k,wordlist[k]))