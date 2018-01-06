while True:
    original = raw_input("Please enter the word you would like to count: ")
    vowels = 0
    if original.isalpha() and len(original) > 0:
        for i in original:
            if i == "a" or i =="e" or i =="i" or i =="o" or i =="u":
                vowels = vowels + 1
        print "The number of vowels is: "
        print vowels
    if not original.isalpha():
        print "The word cannot contain numbers"
    if not len(original) > 0:
        print "You need to enter some letters"
