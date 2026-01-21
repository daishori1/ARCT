def menu(arr=None):
    print("Please select a option to execute \n 1) Add student score \n 2) List all scores \n 3) Update score \n 4) Delete score \n 5) exit ")
    question = [1,2,3,4,5]     
    while True  :
        try:
            arr = int(input("please select a option : "))
            if arr not in question :
                print("answer out of range please try again")
            else:
                return f"correct {arr} "
        except ValueError:
            print("please put a valid character \n this field must be a interger (1-5)")      
                
print(menu())
