while True:
    numbers = [1,2,3,4,5,6,7,8,9,10]
    user = int(raw_input("How many numbers are less than this: "))
    new = []

    for element in numbers:
        if user < numbers[0]:
            print "There are no numbers smaller than that sorry"
        if element < user:
            new.append(element)
    print new
