
def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    problem5()

# Create a function that returns an array from 0 to 100.
# Print the array in another function.

def problem1():
    numberarray =[]
    for x in range(0,101):
       return numberarray.append(x)
    def printarray():
        print(numberarray)
    printarray()

# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q',
# ask them to input another string.

def problem2():
    userinput = input("the escape letter is q just get out of here")
    while(True):
        if(userinput.lower() == "q"):
            break
        else:
            userinput = input("what are you still doing here?")



# Create a function with the variable below.
# After you create the variable do the instructions below that.
#
# listNames = [“John”, “Paul”, “George”, “Pete”]
# a) Print Pete’s name from the list
#
# b) Change Pete’s name to ‘Ringo’, print the list
#
# c) Add the name ‘Yoko’ to the list and print

def problem3():
    listNames = ["John", "Paul", "George", "Pete"]
    print(listNames[3])
    listNames.remove("Pete")
    listNames.insert(3,"Ringo")
    print(listNames)
    listNames.append("Yoko")
    print(listNames)

# Create a function that contains a collection of information for the following.
# After you create the collection do the instructions below that.
#
# Vocals/Robert
# Guitar/Jimmy
# Bass/John
# Drums/Bonzo
# a) Print the collection
#
# b) Print who plays guitar

def problem4():
    band = {"Vocals": "Robert","Guitar":"Jimmy","Bass":"John","Drums":"Bonzo"}
    print(band)
    print(band["Guitar"])

# Create a function that will have a hard coded array of Kenn, Kevin, and Erin several times in the array.
# Print out how many times Kenn, Kevin, or Erin appears in an array.

def problem5():
    teacherlist =("Kenn","Kevin","Erin","Kenn","Kevin","Erin","Kenn","Kevin","Erin","Kenn","Kevin","Erin",)
    print(teacherlist.count("Erin"))


if __name__ == '__main__':
    main()