'''from collections import defaultdict

dicto = defaultdict(int)

with open('yourfile.txt') as f:
    for line in f:
        s_line = line.rstrip().split(',') #assuming ',' is the delimiter
        for ele in s_line:
            dicto[ele] += 1

 #dicto contians words as keys, word counts as values

 for k,v in dicto.iteritems():
     print k,v'''


'''wordstring = 'it was the best of times it was the worst of times '
wordstring += 'it was the age of wisdom it was the age of foolishness'

wordlist = wordstring.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(zip(wordlist, wordfreq)))'''

file_name = input('Simply press Enter to read the Text file\n>> ')
if len(file_name) < 1:
    file_name = 'text.txt'
    text = open(file_name)

    wordfreq = []
    for line in text:
        wordfreq.append(text.count(line))

print ('freq is' + str(wordfreq) +'\n')

        #'''words = line.split()
