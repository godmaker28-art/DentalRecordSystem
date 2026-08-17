def delete_appointment():
    print("\n-- Delete Appointment --");

    if not dentist_appointments:
        print("No appointments found to delete.\n");
        return;

    custom_headers = {"patient": "Patient Name", "dentist": "Dentist", "date": "Date", "time": "Time"}
    print(tabulate(dentist_appointments, headers=custom_headers, tablefmt="grid", showindex=range(1, len(dentist_appointments) + 1)));

    while True:
        choice = int(input(f"Choose appointment to delete [1-{len(dentist_appointments)}, 0 to return]: "));

        if choice == 0:
            return;
        elif 1 <= choice <= len(dentist_appointments):
            removed = dentist_appointments.pop(choice - 1);
            print(f"Appointment for {removed['patient']} has been deleted!\n");
            return;
        else:
            print("Invalid Input!");
