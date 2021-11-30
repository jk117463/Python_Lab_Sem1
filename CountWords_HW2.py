file_path= 'Words.txt' # File name

my_file = open(file_path, 'r') #Open File
lines = my_file.readlines() #Read lines

wordlist = {'_filtered_out':0}
i=0
valid = False
print('\nInput Lines')
for line in lines:
    print('{}: {}'.format(i,line), end='')
    linesplit = line.split() #Split lines
    for word in linesplit:
        valid = False
        if (word.isalpha()): #If split is all letters its valid word
            valid = True
        else:
            word_new = ''
            for c in word:
                if (c.isalpha() or (c == '\'' and word[0] != '\'')): #Else compare letter wise within split and format (replace special characters)
                    word_new = word_new + c
                    valid = True
                else:
                    break
            word = word_new
        if (len(word) == 1): #if length of formatted word is one its invalid
            valid = False
        if(valid == True):
            word = word.lower() # convert all to lower
            if word in wordlist: #if word was identified before then add to count. In dictionary - Count is value, word is the key
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
    print('{}:{}'.format(k,wordlist[k])) # Print dictionary with word and its count