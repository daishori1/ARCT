from db import list_students
from menu import menu


def main():
    
    while True :
        option = menu()
        
        if option == 2 :
            list_students()
            input("pres enter to return to the menu puta")
        elif option == 5:
            break



if __name__ == "__main__":
    main()


