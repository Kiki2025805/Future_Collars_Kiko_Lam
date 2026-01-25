# ============================================================
# ======================== EXERCISES =========================
# ============================================================

# Initialize empty lists to store our database records
students = []
teachers = []
homeroom_teachers = []

while True:
    print("\nMain Menu:")
    print("Available commands: create, manage, end")
    command = input("Enter command: ").strip().lower()

    # 1. HANDLE CREATE COMMAND
    if command == "create":
        while True:
            print("\nUser Creation Process:")
            print("Options: student, teacher, homeroom teacher, end")
            user_type = input("Enter user type: ").strip().lower()

            if user_type == "student":
                name = input("Enter student first and last name: ")
                class_name = input("Enter class name: ")
                students.append([name, class_name])

            elif user_type == "teacher":
                name = input("Enter teacher first and last name: ")
                subject = input("Enter subject: ")
                classes_taught = []
                while True:
                    c = input("Enter class name (or leave empty to finish): ")
                    if c == "":
                        break
                    classes_taught.append(c)
                teachers.append([name, subject, classes_taught])

            elif user_type == "homeroom teacher":
                name = input("Enter homeroom teacher first and last name: ")
                class_name = input("Enter class they lead: ")
                homeroom_teachers.append([name, class_name])

            elif user_type == "end":
                break
            else:
                print("Invalid user type.")

    # 2. HANDLE MANAGE COMMAND
    elif command == "manage":
        while True:
            print("\nUser Management Process:")
            print("Options: class, student, teacher, homeroom teacher, end")
            option = input("Enter option: ").strip().lower()

            if option == "class":
                target_class = input("Enter class name: ")
                print("Students in class {}:".format(target_class))
                for s in students:
                    if s[1] == target_class:
                        print("- {}".format(s[0]))
                for ht in homeroom_teachers:
                    if ht[1] == target_class:
                        print("Homeroom teacher: {}".format(ht[0]))

            elif option == "student":
                target_student = input("Enter student name: ")
                for s in students:
                    if s[0] == target_student:
                        s_class = s[1]
                        print("Attending class: {}".format(s_class))
                        print("Teachers of this class:")
                        for t in teachers:
                            if s_class in t[2]:
                                print("- {} (Subject: {})".format(t[0], t[1]))

            elif option == "teacher":
                target_teacher = input("Enter teacher name: ")
                for t in teachers:
                    if t[0] == target_teacher:
                        print("Classes taught by this teacher: {}".format(t[2]))

            elif option == "homeroom teacher":
                target_ht = input("Enter homeroom teacher name: ")
                for ht in homeroom_teachers:
                    if ht[0] == target_ht:
                        h_class = ht[1]
                        print("Leading class: {}".format(h_class))
                        print("List of students:")
                        for s in students:
                            if s[1] == h_class:
                                print("- {}".format(s[0]))

            elif option == "end":
                break
            else:
                print("Invalid option.")

    # 3. HANDLE END COMMAND
    elif command == "end":
        print("Program terminated.")
        break

    else:
        print("Invalid command. Please try again.")