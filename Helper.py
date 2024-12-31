import os

class Helper:
    @staticmethod
    def clearConsole():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def waitForUser():
        input("Click <Enter> to continue")

    @staticmethod
    def askForString(question):
        isValid = False
        while not isValid:
            uInput = input(question)
            if(uInput == None or uInput == ""):
                print("Invalid input, return a string")
                continue
            else:
                isValid = True
        return uInput