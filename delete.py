from tabulate import tabulate


def delete_appointment(recorded_appointments):
    records = recorded_appointments
    print("\n-- Delete Appointment --")

    if not records:
        print("No appointments found to delete.\n")
        return

    custom_headers = {"patient": "Patient Name", "dentist": "Dentist", "date": "Date", "time": "Time"}
    print(tabulate(records, headers=custom_headers, tablefmt="grid", showindex=range(1, len(records) + 1)))

    while True:
        choice = int(input(f"Choose appointment to delete [1-{len(records)}, 0 to return]: "))
        if choice == 0:
            return
        elif 1 <= choice <= len(records):
            removed = records.pop(choice - 1)
            print(f"Appointment for {removed['patient']} has been deleted!\n")
            return
        else:
            print("Invalid Input!")



