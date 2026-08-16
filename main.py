
# List of Dictionaries
dentist_schedule = [
    {"name":"Dr. Mancion","date":"August 17,2026","time":"9:00AM To 1:00PM"},
    {"name":"Dr. Mendoza","date":"August 18,2026","time":"10:00AM To 2:00PM"},
    {"name":"Dr. Escoto","date":"August 19,2026","time":"11:00AM To 3:00PM"}
]

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


