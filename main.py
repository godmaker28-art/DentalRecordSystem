# Functions


# main starts here!
print("-- Dental Record System --\n");

print("Choices:\n1. Create an appointment\n2. View Records");
choice = int((input("Choose an action [1-2]: ")));

match choice:
    case 1:
        create_appointment();
    case 2:
        view_records();
    case _:
        print("Invalid Input!");


