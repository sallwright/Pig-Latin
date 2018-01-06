pyg = "ay"

original = raw_input("Enter the word you would like to transform here: ")
if len(original) > 0 and original.isalpha():
    new_word = original[1:] + original[0] + pyg
    print new_word.lower()
if len(original) == 0:
    print "You need to write something"
if not original.isalpha():
    print "There is a number in there, and this is a word game"
