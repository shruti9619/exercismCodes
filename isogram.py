#isogram is a special category of word in which any letter can occur only once and not again

word=raw_input("Enter a word")
wordlist= list(word)
#print wordlist
wordsort=sorted(wordlist)
print "sorted letters : ",sorted(wordlist)

flag=False

i=0
while i < len(word)-1:
    if wordsort[i]==wordsort[i+1]:
        flag=True
        break
    i+=1
if flag==True:
    print "It is not isogram"
else:
    print "It is isogram"


