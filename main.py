from tabulate import tabulate # pip install tabulate 

# List of Dictionaries
dentist_schedule = [
    {"index": 1, "name":"Dr. Mancion","date":"August 17,2026","time":"9:00AM To 1:00PM"},
    {"index": 2, "name":"Dr. Mendoza","date":"August 18,2026","time":"10:00AM To 2:00PM"},
    {"index": 3, "name":"Dr. Escoto","date":"August 19,2026","time":"11:00AM To 3:00PM"}
]

dentist_appointments = [
]

# Functions
def new_appointment(patient_name,index):
    new_appointment = {"patient": patient_name, "dentist": dentist_schedule[0]["name"], "date": dentist_schedule[0]["date"], "time": dentist_schedule[0]["time"]};
    dentist_appointments.append(new_appointment);
    print("Appointment Successfully Added!\n\n");

def create_appointment():
    print("\n-- Appointment Creation --");
    patient_name = input("Patient Name: ");
    print (f"\nAppointed Patient: {patient_name}\nChoose your Available Dentist:");

    custom_headers = {"index":"No.", "name":"Dentist's Name", "date":"Date Available", "time":"Time"}
    print(tabulate(dentist_schedule, headers=custom_headers, tablefmt="grid"));

    while True:
        dentist_no = int(input("Choice [1-3, 0 to return]: "));
        match dentist_no:
                case 1:
                    new_appointment(patient_name,0); 
                    break;
                case 2:
                    new_appointment(patient_name,1); 
                    break;
                case 3:
                    new_appointment(patient_name,2); 
                    break;
                case 0:
                    return;
                case _:
                    print("Invalid Input!");


# main starts here!
while True:
    print("-- Dental Record System --\n");

    print("Choices:\n1. Create an appointment\n2. View Records");
    choice = int((input("Choose an action [1-2, 0 to exit]: ")));
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


