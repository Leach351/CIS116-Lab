## Password

incorrect = 0

psswrd = ('123456')

pword = input(str("Please enter your password"))

pGood = False

while(pGood == False):

    pword = input(str("Please enter your password"))
    if (psswrd != pword):

        print ("INNCORRECT")
        incorrect += 1
    else:
        print ("CORRECT!")
        pGood = True


print ("You got the password wrong ", incorrect, " times")  
