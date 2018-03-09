#Zachary Zawaideh
#Computer Programming
#2/28/18

def dictionary():#I only use one function, because this a short program.
    inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}#The first thing we need to do is create a variable.
    print(inventory)#This prints the dictionary to the user.
    x= input("What item do you want to change?: ").lower()#I ask the user what they want to change by using an input.
    y= input("How many would you like to take?: ")#This is the input asking how many they want to take from the origianal number in the dictionary.
    for key in inventory:#I use a for loop to check if what the user picked is in the dictionary.
        if key==x:#Used an if statement.
            math= (inventory[x]-int(y))#This does the math.
            print(math)#This prints the amount of fruit the user has when they finish.
            dictionary()#This takes the user back to the top.
    print("Choose a fruit!")#By putting this outside the for loop, if the user's input is not in the dictionary the user is taken back to the top.
    dictionary()#Takes the user back to the top of the function.

        
dictionary()#Starts the program.
