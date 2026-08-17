from tabulate import tabulate  # pip install tabulate

# Dentist schedule and appointment structure
dentist_schedule = [
    {"index": 1, "name": "Dr. Mancion", "date": "August 17, 2026", "time": "9:00AM To 1:00PM"},
    {"index": 2, "name": "Dr. Mendoza", "date": "August 18, 2026", "time": "10:00AM To 2:00PM"},
    {"index": 3, "name": "Dr. Escoto", "date": "August 19, 2026", "time": "11:00AM To 3:00PM"}
]

# Initialize with an empty list instead of a list containing an empty dict
dentist_appointments = []


# Functions
def new_appointment(patient_name, index):
    selected_dentist = dentist_schedule[index]
    appointment = {
        "patient": patient_name,
        "dentist": selected_dentist["name"],
        "date": selected_dentist["date"],
        "time": selected_dentist["time"]
    }
    dentist_appointments.append(appointment)
    print("\nAppointment Successfully Added!\n")


def create_appointment():
    print("\n-- Appointment Creation --")
    patient_name = input("Patient Name: ").strip()
    
    if not patient_name:
        print("Patient name cannot be empty!\n")
        return

    print(f"\nAppointed Patient: {patient_name}\nChoose your Available Dentist:")

    custom_headers = {"index": "No.", "name": "Dentist's Name", "date": "Date Available", "time": "Time"}
    print(tabulate(dentist_schedule, headers=custom_headers, tablefmt="grid"))

    while True:
        try:
            dentist_no = int(input("Choice [1-3, 0 to return]: "))
            
            if dentist_no == 0:
                return
            elif 1 <= dentist_no <= len(dentist_schedule):
                # Pass index-1 to match the 0-based list index
                new_appointment(patient_name, dentist_no - 1)
                break
            else:
                print("Invalid Input! Please choose between 1-3 or 0 to return.")
        except ValueError:
            print("Invalid Input! Please enter a valid number.")


def view_records(appointment_list):
    print("\n-- Dental Clinic Records --")
    
    # Filter out any empty dictionaries if they exist
    filtered_records = [app for app in appointment_list if app]
    
    if not filtered_records:
        print("Empty Set - No active patient appointments yet.\n")
        input("Press Enter to go back to the main menu...")
        return
        
    custom_headers = {
        "patient": "Patient's Name",
        "dentist": "Dentist's Name",
        "date": "Date",
        "time": "Time"
    }

    print(tabulate(filtered_records, headers=custom_headers, tablefmt="grid"))
    print("\n")

    input("Press Enter to go back to the main menu...")


# Main loop starts here!
if __name__ == "__main__":
    while True:
        print("\n-- Dental Record System --\n")
        print("Choices:\n1. Create an appointment\n2. View Records\n0. Exit")
        
        try:
            choice = int(input("Choose an action [1-2, 0 to exit]: "))
            
            match choice:
                case 1:
                    create_appointment()
                case 2:
                    view_records(dentist_appointments)
                case 0:
                    print("Exiting the system...")
                    break
                case _:
                    print("Invalid Input! Please choose a valid option.\n")
        except ValueError:
            print("Invalid Input! Please enter a number.\n")