from tabulate import tabulate # pip install tabulate 

# Dentist schedule and appointment structure
dentist_schedule = [
    {"index": 1, "name":"Dr. Mancion","date":"August 17,2026","time":"9:00AM To 1:00PM"},
    {"index": 2, "name":"Dr. Mendoza","date":"August 18,2026","time":"10:00AM To 2:00PM"},
    {"index": 3, "name":"Dr. Escoto","date":"August 19,2026","time":"11:00AM To 3:00PM"}
]
dentist_appointments = [
    {}
]

# Functions
def new_appointment(patient_name, index):
    pass

def create_appointment():
    print("-- Appointment Creation --");
    patient_name = input("Patient Name: ");
    print (f"\nAppointed Patient: {patient_name}\nChoose your Available Dentist:");

    custom_headers = {"index":"No.", "name":"Dentist's Name", "date":"Date Available", "time":"Time"}
    print(tabulate(dentist_schedule, headers=custom_headers, tablefmt="grid"));

    dentist_no = int(input("Choice [1-3, 0 to return]: "));

    while True:
        match dentist_no:
                case 1:
                    new_appointment(patient_name,0);
                case 2:
                    new_appointment(patient_name,1);
                case 3:
                    new_appointment(patient_name,2);
                case 0:
                    return;
                case _:
                    print("Invalid Input!");


# main starts here!
print("-- Dental Record System --\n");

print("Choices:\n1. Create an appointment\n2. View Records");
choice = int((input("Choose an action [1-2, 0 to exit]: ")));

while True:
    match choice:
        case 1:
            create_appointment();
        case 2:
            view_records();
        case 0:
            print("Exiting the system...");
            break;
        case _:
            print("Invalid Input!");


