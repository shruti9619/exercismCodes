transdict={'G':'C','C':'G','T':'A','A':'U'}

dna=list(raw_input("Enter the strand value : "))

#checks if the value is in list or not and if not then prints x

for node in dna:
    if node.upper() in transdict:
        print transdict.get(node.upper())
    else:
        print 'X'