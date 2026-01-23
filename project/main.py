from db import list_students , add_student ,delete_student , update_score
from menu import menu


def main():
    
    while True :
        option = menu()
        if option == 1:
            add_student()
            input("pres enter to return to the menu puta")
        if option == 2 :
            list_students()
            input("pres enter to return to the menu puta")
        if option == 3 :
            input("pres enter to return to the menu puta")
        if option == 4:
            delete_student()
            input("pres enter to return to the menu puta")
        elif option == 5:
            break



if __name__ == "__main__":
    main()


