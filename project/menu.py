def menu():
    print("""Please select an option:
  1) Add student 
  2) List all students
  3) Update score
  4) Delete student
  5) Exit
""")
    valid_option = {1,2,3,4,5}     
    while True  :
        try:
            option = int(input("please select a option : "))
            if option not in valid_option :
                print("answer out of range please try again")
            else:
                return  option
        except ValueError:
            print("invalif input\n this field must be a interger (1-5)")      
                

