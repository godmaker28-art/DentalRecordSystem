print("Group 2 Dentistry\nDental Record System\n");

print(input("Choose an action: [1-2]"));
print("Choices:\n1. Create an appointment\n2. View Records");

match input:
    case 1:
        create_appointment();
    case 2:
        view_records();
    case _:
        print("Invalid Input!");


