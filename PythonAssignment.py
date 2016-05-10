#This is my assignment for the koch function
#This is for class CSCI 333
#The author of this is: Joe Dandan
#There are no bugs
#Note* to display the koch snowflakes, please uncomment the lines
#in the commented funcation calls below at the end of the function

#Also if all commented function calls at the end of the three functions
#are uncommented you can view the program run all three functions in 1 execution

#We begin by importing in the turtle library
import turtle

#Next we make a new turtle called turtle
turtle = turtle.Turtle()

#This is our function called koch that takes in a turtle a sidelength and a generation
def koch (turtle, sidelength, generation):
    #This is a string that is going to be used to define our turtles moves
    #Our directions are as follows F = forward R = right L = left
    turtlemoves = "FRFRF"

    #If we are at generation 0 we are going to draw a triangle
    if (generation == 0):
        #We are going to have to follow our turtle moves directions to draw a triangle
        for directions in turtlemoves:
            #If our directions tell us that we need to move forward
            if directions == "F":
                #We move our turtle forward our sidelength
                turtle.forward(sidelength)
            #If our directions tell us to move right   
            elif directions == "R":
                    #We move our turtle right 120 degrees
                    turtle.right(120)
        #This is a text statement prompting the user to hit enter to exit
        #This allows for a user to view there turtle drawing
        texttoexit = raw_input('Press Enter To Exit and go on to the next function:')

    #If we are not in generation 0 we are begining to draw the snowflake        
    else:
        #Since our generation is not 0 we want to work with that generation number
        for value in range(generation):
            #everytime we see a F in our turtlemoves we want to replace it
            #with a new set of moves to make the triangle points
            turtlemoves = turtlemoves.replace("F","FLFRFLF")
        #We are going to have to follow our turtle moves directions to draw 
        for directions in turtlemoves:
                #If our directions tell us that we need to move forward
                if directions == "F":
                    #We set x to be our sidelength over our generation times 3
                    #We do this to keep the star sidelengths small enough
                    #to see on the screen when generating a star
                    x = sidelength/(generation*3)
                    #We move the turtle forward x
                    turtle.forward(x)
                #If our directions tell us to move left
                elif directions == "L":
                    #We move the turtle left 60 degrees
                    turtle.left(60)
                #If our directions tell us to move right   
                elif directions == "R":
                    #We move the turtle right 120 degrees
                    turtle.right(120)
        #We prompt the user to press enter to exit giving them time
        #to look at the drawing
        texttoexit = raw_input('Press Enter to Exit and go onto the next function:')


#The following lines are examples of funcation calls that can be uncommented to
#test the program
#koch(turtle, 50, 0)
#koch(turtle, 50, 1)
#koch(turtle, 50, 2)
#koch(turtle, 50, 3)
#koch(turtle, 50, 4)


#This is my assignment for the rock paper scissors lizard spock game
#This is for class CSCI 333
#The author of this is : Joe Dandan
#there are no bugs
#Note to start this game please uncomment the line below at the end of this function
#and the 2 following ones below that. You will see a stared out section to show were function
#calls are commented out.

#we import the libraries we use
import random

#this is where we define our function
def rockPaperScissorsLizardSpock():

    #from that point on we want to define our choices
    Choices = ['r', 'p', 'sc', 'l', 'sp', ]


    #these are two variables that will be used in the game to
    #see how many games you have won
    ready = 0
    space = 0

 
    #we prompt the user to play the game
    print('Are you ready to play (r)ock, (p)aper, (sc)issors, (l)izard, (sp)ock?')

    #while none of our variables are at 5, which is our max amounts of games you can win
    while ( ready!= 5 and space !=5):
        #we prompt the user to enter a choice and enter that
        #into the myresponse as a rawinput
        myResponse = raw_input('Please enter the choice you would like to go with'
                               + ' in full text: ')
        #we move everything to a lowercase value to help with checking
        myResponse = myResponse.lower()
        #we then generate a random response for the computer
        computerResponse = random.choice(Choices)
        #we let the user know what the computer has picked
        print('Computer picked:', computerResponse)
        

        #we check to see if the user and the computer has picked the same value
        if (myResponse == computerResponse):
                #if they have we print out that its a tie game
                print('Tie Game')
            
        #else we go to our big an or statements to figure out if the user
        #wins the game from our choices        
        elif (myResponse == 'r' and computerResponse == 'sc' or

                    myResponse == 'r' and computerResponse == 'l' or
      
                    myResponse == 'p' and computerResponse == 'r' or

                    myResponse == 'p' and computerResponse == 'sp' or

                    myResponse == 'sc' and computerResponse == 'p' or

                    myResponse == 'sc' and computerResponse == 'l' or
        
                    myResponse == 'l' and computerResponse == 'p' or

                    myResponse == 'l' and computerResponse == 'sp' or
      
                    myResponse == 'sp' and computerResponse == 'sc' or

                    myResponse == 'sp' and computerResponse == 'r'):
                    
                    #we let the user know that they won a game out of five 
                    print('Congratulations, You won y/5 games')
                    #we want to let the user know how many games they have won
                    print('y=')
                    #we add 1 to our value that we use to track how many games
                    #the user has won
                    ready = ready +1
                    #we print the value of how many times the user has won
                    print(ready)
                     
        else:
                    #we tell the user that the computer has beat them
                    print('Im sorry, You lost x/5 games')
                    #we want to let the user know how many times they have lost
                    print('x=')
                    #we add 1 to our value to track how many times the user has lost
                    space = space +1
                    #we print out how many times the user lost
                    print(space)    
    endgame = raw_input('Please press Enter to End the game and go on to the next fuction:')     



#This line is the function call to start our game
    
#rockPaperScissorsLizardSpock()
    
#Please Uncomment the function call to start        


#This is my assignment for the middleEnglish function
#This is for class CSCI 333
#The author of this is: Joe Dandan
#There are no bugs
#Note* to translate text please enter in the text you wish
#to translate in the commented function call below

#We define our function middleEnglish that takes a parameter of a sentence
def middleEnglish(sentence):

    #This is our dictionary that is going to change the words to
    #middle english from that sentence
    dict = {'how':'hath','why':'hath','when':'hath','where':'whence',
            'you':'thou','your':'thine','quickly':'verily','the':'ye',
            'are':'art','between':'betwixt','does':'dost','never':'nary',
            'here':'hither','beg':'beseech','please':'prithee','will':'wilt',
            'there':'tither', 'were':'wert', 'shall':'shalt','near':'nigh', 'enter':'entereth',
            'text':'texts',
            }
         
    #This is a print statement to prompt the user that there text has been translated
    print('The following is text translated into Middle English:')

   
    #First thing we want to do is set all the text to lowercase
    sentence = sentence.lower()
    
    #After that we want to split the text 
    splitText = sentence.split()
    
    #We have an array we want to store the text into
    newText = []

    #We need a variable to hold a int value to help us with adding e to words
    i=1
    
    #For every word that is split into text in splittext
    for everyword in splitText:

        #If our variable is divisable by 4 
        if(i %4 ==0):
            
            #We add 1 to our variable to continue forward
            i = i+1

            #We then want to add to our array the text we are going to store plus the letter e
            #We use get on our dictionary and replace the words and add e to the end
            newText.append(dict.get(everyword,everyword) + "e")
            
        #Since our variable is not divisable by 4
        else:

            #We still add 1 to our variable to continue forward
            i = i +1
            
            #So we appended our dictionary that gets an item from our dictionary to replace the original word
            newText.append(dict.get(everyword,everyword))
        
    #We want to print the new text and we use join to do that
    print " ".join(newText)

    #This is used to promt the user to exit the program
    texttoexit = raw_input('Press Enter to End the translation:')





#This line is the function call to start our game
    
#middleEnglish('Enter text to be translated please before you run out of time');
    
#Please Uncomment the function call to start       




