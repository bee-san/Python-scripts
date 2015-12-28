for num in xrange(1, 101):
    # for every number in range of 1 to 101
    msg = ''  # creates empty string
    if num % 3 == 0:
        msg += 'Fizz'  # augmented assignment
    if num % 5 == 0:
        msg += 'Buzz'  # augmented assignment
    print msg or num  # boolean algebra, if msg != True, try num
