## Password



psswrd = ('123456')

pword = input(str("Please enter your password"))

pGood = False

while(pGood == False):

    pword = input(str("Please enter your password"))
    if (psswrd != pword):

        print ("INNCORRECT")
    else:
        print ("CORRECT!")
        pGood = True
## Test
