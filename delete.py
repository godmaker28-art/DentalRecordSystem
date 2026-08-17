from tabulate import tabulate
dentist_appointments = [
    {"patient": "Ms. San Diego", "dentist": "Dr. Mancion", "date": "August 17,2026", "time": "9:00AM To 1:00PM"},
    {"patient": "Mr. Santos", "dentist": "Dr. Mendoza", "date": "August 18,2026", "time": "10:00AM To 2:00PM"},
]

def delete_appointment():
    print("\n-- Delete Appointment --")

    if not dentist_appointments:
        print("No appointments found to delete.\n")
        return

    custom_headers = {"patient": "Patient Name", "dentist": "Dentist", "date": "Date", "time": "Time"}
    print(tabulate(dentist_appointments, headers=custom_headers, tablefmt="grid", showindex=range(1, len(dentist_appointments) + 1)))

    while True:
        choice = int(input(f"Choose appointment to delete [1-{len(dentist_appointments)}, 0 to return]: "))
        if choice == 0:
            return
        elif 1 <= choice <= len(dentist_appointments):
            removed = dentist_appointments.pop(choice - 1)
            print(f"Appointment for {removed['patient']} has been deleted!\n")
            return
        else:
            print("Invalid Input!")


delete_appointment()