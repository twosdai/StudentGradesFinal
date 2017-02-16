def add_student(List, name, mid, final, hw1, hw2, hw3): #Used in the add student section
    List[name] = mid,final,hw1,hw2,hw3
def print_grades(List):
    for k in List:
        x=list(List[k])
        print(k,"Midterm:" +str(x[0]), "Final:" +str(x[1]), "Homework1:" +str(x[2]), "Homework2:" +str(x[3]), "Homework3:" +str(x[4])) 
def save_grades(List, Filename): #Used in Save Grades section
    out_file = open(filename, "wt")
    for k in List:
        x= list(List[k])
        out_file.write(k+","+str(x[0:5])+ "\n")
    print("File Saved")
        
        
def remove_student(List, name): #Used in the Remove student section
    if name in List:
        del List[name]
        print("Student Removed")
    else:
        print(name, "was not found")
def lookup_student(List, name): #Used in the lookup a student section
    if name in List:
        x=list(List[name])
        print(name,"Midterm:" +str(x[0]), "Final:" +str(x[1]), "Homework1:" +str(x[2]), "Homework2:" +str(x[3]), "Homework3:" +str(x[4])) 
    else:
        return name + " was not found"
def load_grades(List,filename): #Used to load grades from file
    in_file= open(filename, "rt")
    while True:
        in_line= in_file.readline()
        if not in_line:
            break
        in_line =in_line[:-1]
        name, mid, final, hw1, hw2, hw3 = in_line.split(",")
        List[name] = mid,final,hw1,hw2,hw3
    in_file.close()
    print("File Loaded")

def PrintMenu():#For the menu 

    print( "Enter a number 1-7 to complete a corresponding action Enter 8 to quit")
    print ("See the menu a list of actions")
    print ("1. Add a Student Record")
    print ("2. Remove a Student Record") 
    print ("3. Lookup a Student") 
    print ("4. Load Grades") 
    print ("5. Save Grades")
    print ("6. Print Grades") 
    print ("7. Print Menu") 
    print ("8. Quit")
    print()
PrintMenu()
menu_choice = 0
Grades={}
while True:
            menu_choice = int(input("Type in a number (1-8) (7 is the menu): "))
            if menu_choice == 1:
                print("Add a Student Record")
                name = input("Name(Last First):")
                Midterm= input("Midterm:")
                Final = input("Final:")
                Hw1 = input("Homework1:")
                Hw2 = input("Homework2:")
                Hw3 = input("Homeowork3:")
                add_student(Grades, name, Midterm, Final, Hw1, Hw2, Hw3)
                
            elif menu_choice == 2:
                print("Remove a Student from the Record")
                name = input("Name(Last First): ")
                remove_student(Grades, name)

            elif menu_choice == 3:
                print("Look up Student")
                name = input("Name(Last First): ")
                print (lookup_student(Grades, name ))
            elif menu_choice == 4:
                filename = input("Filename to load: ")
                load_grades(Grades,filename)

            elif menu_choice == 5:
                filename = input("Filename to save: ")
                save_grades(Grades, filename)
            elif menu_choice == 6:
                print_grades(Grades)
            elif menu_choice == 7:
                PrintMenu()
            elif menu_choice == 8:
                break
           
            else:
                PrintMenu()

                
