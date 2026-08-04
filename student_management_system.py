#===== Student Record Management =====
#1. Add Student
#2. View Students
#3. Search Student
#4. Update Student
#5. Delete Student
#6. Exit

#Student details
#Student ID
#Name
#Age

#1.Add students 
def add_student(student_list):
        student_details = []
        error = False
        id_error = False
        student_id = int(input("Enter the student ID : "))
        student_name = input("Enter the student name : ")
        student_age = int(input("Enter the student age : "))
        for i in range(len(student_list)):
                if student_id != student_list[i][0]:
                    if student_name == "" or student_age <= 0:
                            error = True
                else:
                    id_error = True
        if id_error == False:
            if error == False:
                student_details.append(student_id)
                student_details.append(student_name)
                student_details.append(student_age)
                student_list.append(student_details)
            else:
                print("YOU_HAVE_ENTERED_INVALID_NAME_OR_AGE_!!!")
        else:
            print("STUDENT ID ALREADY EXIST !!!")
        return student_list

#2.Display Students
def display(student_list):
    if student_list:
        print("Student_ID","Student_name","Student_Age",sep = "\t")
        for i in range(len(student_list)):
            print(f"{student_list[i][0]}\t\t",f"{student_list[i][1]}\t\t",f"{student_list[i][2]}\t\t")
    else:
        print("NO_STUDENT_RECORDS_ARE_STORED:(")

#3.Search student
def search_student(target,student_list):
    for i in range(len(student_list)):
        if target == student_list[i][0]:
            return i
        
    
        
#4.Update Student
def update_student(index,student_list):
    update = 0
    if index is not None:
        print("Enter 1 to update Name : ")
        print("Enter 2 to update Age : ")
        print("Enter 3 to update both Name and Age : ")
        update = int(input("What do you like to update : "))
        if update == 1:
            updated_name = input("Enter the new name : ")
            student_list[index][1] = updated_name
        elif update == 2:
            updated_age = int(input("Enter the new age : "))
            student_list[index][2] = updated_age
        elif update == 3:
            updated_name = input("Enter the new name : ")
            updated_age = int(input("Enter the new age : "))
            student_list[index][1] = updated_name
            student_list[index][2] = updated_age                
        else:
            print("INVALID_INPUT!!!")
    else:
        print("Invalid_Student_ID")


#5.Delete Student
def delete_student(index,student_list):
    confirm = ""
    if index is not None:
            confirm = input("Do you want to delete this student record : (Y/N)")
            if confirm == 'Y':
                student_list.pop(index)
                print("Student record deleted.")
            elif confirm == 'N':
                print("Student record not deleted.")
            else:
                print("INVALID_INPUT")
    else:
        print("STUDENT_NOT_FOUND !!! :(")



#Menu function
def menu():
    print("Enter 1 to add new student : ")
    print("Enter 2 to to view students : ")
    print("Enter 3 to search a student : ")
    print("Enter 4 to update student record : ")
    print("Enter 5 to delete student record : ")
    print("Enter 6 to exit : ")

# Main function
def main():
    student_list = []
    task = 0
    target = 0
    student_id = 0
    student_name = ''
    student_age = 0 
    while task != 6:
        menu()
        task = int(input("How can i help you : "))
        if task == 1:
            add_student(student_list) 
        elif task == 2:
            display(student_list)
        elif task == 3:
            target = int(input("Enter the Student ID you want to search : "))
            index = search_student(target,student_list)
            if student_list:
                if index is not None:
                    print(f"Student ID : {student_list[index][0]}")
                    print(f"Student Name : {student_list[index][1]}")
                    print(f"Student Age : {student_list[index][2]}")
                else:
                    print("Invalid input")
            else:
                print("NO_STUDENTS_RECORDS_FOUND")
        elif task == 4:
            target = int(input("Enter the Student ID you want to update : "))
            index = search_student(target,student_list)
            if index is not None:
                update_student(index,target,student_list)
            else:
                print("NO_STUDENTS_RECORDS_FOUND")
        elif task == 5:
            target = int(input("Enter the Student ID you want to delete : "))
            index = search_student(target,student_list)
            if index is not None:
                delete_student(index,target,student_list)
            else:
                print("NO_STUDENTS_RECORDS_FOUND")
        elif task == 6:
            print("Exited")
        else:
            print("Invalid input")

main()