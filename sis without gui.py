import csv


record_fields = ['ID Number', 'First Name','Last Name',
                 'Middle Name','Gender','Course',
                 'Year Level']
csv_database = 'students_list.csv'

def menu():
    print("========================================")
    print("Ilimitary Skul Student Management System")
    print("========================================")
    print("1. Add New Student")
    print("2. View Student's List")
    print("3. Search Student")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Quit")
    
def create_record():
    print("========================")
    print("Add Student Information")
    print("========================")
    global record_fields
    global csv_database
    student_data = []
    for field in record_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(csv_database, "a", encoding="utf-8", newline = '') as f:
        writer = csv.writer(f)
        writer.writerows([student_data])
    print("Data saved successfully")
    input("Press any key to continue")
    return
def fixed(text, length):
    if len(text)> length:
        text = text[:length]
    elif len(text) < length:
        text = (text + " " * length)[:length]
    return text
    
def display_list():
    global record_fields
    global csv_database
    print("======Student Records======")
    with open(csv_database,"r",encoding="utf-8") as f:
        reader = csv.reader(f)
        for k in record_fields:
            print(fixed(k,11),end = "  |")
        print('\n' + "=" * 100)
        for row in reader:
            for item in row:
                print(fixed(item,11),end = "  |")
            print()
    input("Press any key to continue")

def search():
    global record_fields
    global csv_database
    print("=" * 10 + "Search Student by ID"+"=" * 10)
    roll = input("Enter ID number to search: ")
    with open(csv_database, "r",encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("========== Student Found ===========")
                    print("ID Number: ", row[0])
                    print("First Name: ", row[1])
                    print("Last Name: ", row[2])
                    print("Middle Name: ", row[3])
                    print("Gender: ", row[4])
                    print("Course: ", row[5])
                    print("Year Level ", row[6])
                    break
        else:
            print("ID Number not Found")
    input("Press any key to continue")

def update():
    global record_fields
    global csv_database

    print("=========== Update Student ============")
    roll = input("Enter ID Number to Update: ")
    idx_student = None
    update_rec = []
    with open(csv_database, "r", encoding ="utf-8", newline = '') as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    idx_student = counter
                    print("Student Found: ")
                    student_data = []
                    for field in record_fields:
                        value = input("Enter new " + field + ": ")
                        student_data.append(value)
                    update_rec.append(student_data)
            else:
                update_rec.append(row)
            counter += 1

    if idx_student is not None:
        with open(csv_database, "w", encoding="utf-8", newline = '') as f:
            writer = csv.writer(f)
            writer.writerows(update_rec)
    else:
        print("ID Number Does Not EXIST")

    input("Press any key to continue")

def delete_student():
    global record_fields
    global csv_database

    print("========= Delete Student =========")
    roll = input("Enter ID number to delete: ")
    student_location = False
    update_rec = []
    with open(csv_database, "r",encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                      update_rec.append(row)
                      counter += 1
                else:
                    student_location = True
    if student_location is True:
        with open(csv_database, "w", encoding = "utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(update_rec)
        print("Student, ", roll, "Deleted")
    else:
        print("ID Number not found")
    input("Press any key to continue")

while True:
    menu()
    option = input("Select your option: ")
    if option == '1':
        create_record()
    elif option == '2':
        display_list()
    elif option == '3':
        search()
    elif option == '4':
        update()
    elif option == '5':
        delete_student()
    else:
        break


print("Thank you, GoodBye")

        
                          
                      







        








    
