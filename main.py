from tabulate import tabulate # pip install tabulate 
from view_appointments import view_records
from create import create_appointment
from delete import delete_appointment
# Dentist schedule and appointment structure
dentist_schedule = [
    {"index": 1, "name":"Dr. Mancion","date":"August 17,2026","time":"9:00AM To 1:00PM"},
    {"index": 2, "name":"Dr. Mendoza","date":"August 18,2026","time":"10:00AM To 2:00PM"},
    {"index": 3, "name":"Dr. Escoto","date":"August 19,2026","time":"11:00AM To 3:00PM"}
]
dentist_appointments = []

# Functions
def new_appointment(patient_name, index):
    dentist_name = dentist_schedule[index]["name"]
    dentist_date = dentist_schedule[index]["date"]
    dentist_time = dentist_schedule[index]["time"]
    new_app = {
        "patient": patient_name,
        "dentist": dentist_name,
        "date": dentist_date,
        "time": dentist_time
    }

    dentist_appointments.append(new_app)
    print("\nSuccess - Appointment Scheduled!\n")
    return 0





# main starts here!
while True:
    print("-- Dental Record System --\n");

    print("Choices:\n1. Create an appointment\n2. View Records\n3. Delete Appointment");
    try:
        choice = int((input("Choose an action [1-2, 0 to exit]: ")));

            
        match choice:
                    case 1:
                        result = create_appointment(dentist_schedule)

                        if result is not None:
                            patient_name, index = result
                            new_appointment(patient_name, index) 
                    case 2:
                        view_records(dentist_appointments)
                    case 3:
                        delete_appointment(dentist_appointments)
                    case 0:
                        print("Exiting the system...")
                        break
                    case _:
                        print("Invalid Input!")
    except ValueError:
        print("Invalid Input!")


