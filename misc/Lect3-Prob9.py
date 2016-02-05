print "Please think of a number between 0 and 100!"
low = 0
high = 100
ans = 0

while (high-low) > 0:
    guess = (low + high)/2
    print ("Is your secret number " + str(guess) + "?")
    correct_input = False
    while correct_input == False:
        inp = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
        if inp in ["h", "l", "c"]:
            correct_input = True
        else:
            print ("Sorry, I did not understand your input.")
            print ("Is your secret number " + str(guess) + "?")
    if inp == "h":
        high = guess
    elif inp == "l":
        low = guess
    else:
        print ("Game over. Your secret number was: " + str(guess))
        break
