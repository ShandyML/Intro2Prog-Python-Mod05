# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Minghsuan Liu,5/11/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json
from io import TextIOWrapper
# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
first_name: str = '' 
last_name: str = ''  
course_name: str = ''  
json_data: str ='' 
file: TextIOWrapper = None  
menu_choice: int ='' #define as int, practice ValueError
student_data: dict = {}  
students: list = [] 

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

try: 
    file= open(FILE_NAME,'r')
    try:
        json_data = json.load(file)
        if not json_data:
            raise Exception("No Content in the file")
    except Exception as e:
        print("Please add initial content in the file")
    file.close()
except FileNotFoundError as e:
    print("File doesn't exist! Try to create one")
except Exception as e:
    print("There was an error open the document")
    print(e,e.__doc__)

    




# Present and Process the data
while json_data:
    # Present the menu of choices
    print(MENU)
    # in case user input not in the choice of menu
    try: 
        menu_choice=int(input("What would you like to do: "))
        if menu_choice>4 or menu_choice<1 :
            raise Exception("Please input 1~4 !")
    except ValueError as e:
        print("Please eneter valid choice (1~4)")
    except Exception as e:
        print(e)
        

    # Input user data
    if menu_choice == 1:
            while True:     
                try:
                    first_name = input("Please Enter Student's First Name: ")
                    last_name = input("Please Enter Student's Last Name: ")
                    
                    if not first_name.isalpha() or not last_name.isalpha():
                        raise ValueError("Name can only have alphabetic characters!")
                    course_name = input("Please Enter Course Name: ")
                    student_data={"FirstName":first_name,"LastName":last_name,"CourseName":course_name}
                    json_data.append(student_data)
                    input("Press \"Enter\" to continue...")
                    break
                except ValueError as e:
                    print("User Entered invalid information! ")
        # Present the current data
    elif menu_choice == 2:
            if first_name:
                for line in json_data:
                    print(f'{line["FirstName"]} {line["LastName"]} is registered for course {line["CourseName"]}\n')
                
                input("Press \"Enter\" to continue...")
            else:
                print("No data was input, Please select Opt.1 to input data!")
                input("Press \"Enter\" to continue...")
        # Save the data to a file
    elif menu_choice == 3:
            if first_name:
                try:
                    file=open(FILE_NAME,"w")
                    json.dump(json_data,file,indent=2)
                    file.close()
                   
                    print("Your Info is registered in the system\n")
                    first_name=""
                    last_name=""
                    course_name=""
                    input("Press \"Enter\" to continue...")
                except FileNotFoundError as e:
                    print("File doesn't exist! Try to create one")
                except Exception as e:
                    print("There was an error open the document")
                    print(e,e.__doc__)    
            else:
                print("No data was input, Please select Opt.1 to input data!")
                input("Press \"Enter\" to continue...")
        # Stop the loop
    elif menu_choice == 4:
            print("Thanks for using Registration System, Goodbye! ")
            break

        