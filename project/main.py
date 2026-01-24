from db import list_students , add_student ,delete_student , update_score
from menu import menu


def main():
    
    while True :
        option = menu()
        if option == 1:
            add_student()
            input("press enter to return to the menu ")
        if option == 2 :
            list_students()
            input("press enter to return to the menu ")
        if option == 3 :
            update_score()
            input("press enter to return to the menu ")
        if option == 4:
            delete_student()
            input("press enter to return to the menu ")
        elif option == 5:
            confirm = input(f"Are you sure you want to delete? (yes/no): ")
            if confirm.lower() != 'yes':
                print("cancelled,return to menu")
            else :
                break



if __name__ == "__main__":
    main()


