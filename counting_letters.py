#Zachary Zawaideh
#Computer Programming
#3/2/18


def function(word):#Create the function and pass the variable.
    dictionary={}#First make an empty dictionary.
    for c in word:#The for loop runs through the word and checks every variable.
        if c in dictionary.keys():#This checks to see if the letter is in the dictionary, which at first it is not.
            dictionary[c] = dictionary[c] + 1#This adds a value to the key which is the letter.
        else:#The program will always come to this else statement before the if statement.
            dictionary[c]= 1#This create the first key and creates a value for it, then goes back to the if statement.
    print(dictionary)#This prints the dictionary.


function("bob")#This starts the program as well as defines variable.
        
