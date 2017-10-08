

file_name = input('Simply press Enter to read the Text file\n>> ')
if len(file_name) < 1:
    file_name = 'text.txt'
    text = open(file_name)

    wordfreq = []
    for line in text:
        wordfreq.append(text.count(line))

print ('freq is' + str(wordfreq) +'\n')

        #'''words = line.split()
