## Password

incorrect = 0

psswrd = '123456'

pGood = False

while(pGood == False):

    pword = input(str("Please enter your password"))

    if (pword == psswrd):
        print ("CORRECT!")
        pGood = True
        

    else:
        print ("INNCORRECT")
        incorrect += 1


print ("You got the password wrong ", incorrect, " times")  
