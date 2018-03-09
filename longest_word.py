#Zachary Zawaideh 
#Computer Programming
#3/6/18

def longest_word():#Even though the task is complex the program is small enough for one function.
    lists=[]#We need to have empty brackets in order to create a list if we need to.
    long=""#We create an empty set of "" in order to have a len to use in an if statement later.
    file=open("alice (3).txt","r")#The first step of action is to open the file.
    read=file.readlines()#It is necessary to read the file lines.
    for this in read:#We need to use a for loop to split the file script.
        this=this.split()
        for pencil in this:#This for loop is used to put the text into brackets and make it a list.
            lists.append(pencil)#Puts the text into a list in the for loop.
    for this in lists:#Runs through the script again, but this time it is using an if statment in the for loop.
        if len(this)>len(long):#Uses length and a greater than statment to to find the longest word. 
            long=this#Sets long equal to this.
    print("Longest word: "+long+"")#Prints the longest word in Alice and Wonderland.
    print("Amount of characters: "+str(len(long))+" ")#Prints how many characters it has.

longest_word()#Starts the program
