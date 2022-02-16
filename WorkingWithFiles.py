import os

def checkPath(path):
    if not os.path.isdir(path):
        return False
    else:
        return True

fileName = input("Name of file?: ")
path = ""

#Get valid directory path
while(checkPath(path) == False):
    path = input("Path for directory?: ")
    if(checkPath(path) == False):
        print("DIRECTORY DOES NOT EXIST")
        
#Runs when directory exists
print("DIRECTORY EXISTS")

#Get user input and combine
name = input("Name: ")
address = input("Address: ")
phoneNumber = input("Phone Number: ")
fileText = name + ", " + address + ", " + phoneNumber

#Get path and file name toghether
completePath = os.path.join(path, fileName)

#Write to file and close
file = open(completePath, "w")
file.write(fileText)
file.close()

#Open file to read
file = open(completePath, "r")
print(file.read())

