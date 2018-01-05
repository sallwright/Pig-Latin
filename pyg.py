pyg = "ay"

original = raw_input("Enter the word you would like to transform here: ")
if len(original) > 0 and original.isalpha():
    latin = original[1:] + original[0] + pyg
    print latin.lower()
if not len(original) > 0:
    print "You need to write something"
if not original.isalpha():
    print "There is a number in there, and this is a word game"
