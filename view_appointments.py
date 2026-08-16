
from tabulate import tabulate

def view_records(appointment_list):
    print("\n -- Dental Clinic Records --")
    filtered_records = [app for app in appointment_list if app]
    if not filtered_records:
        print("Empty Set - No Active patien's appointment yet. \n")
        input("Press Enter to Go back to the main menu...")
        return
    custom_headers = {
        "patient":"Patient's Name",
        "dentist":"Dentist's Name",
        "date":"Date",
        "time":'Time'
    }

    print(tabulate(filtered_records, headers=custom_headers, tablefmt="grid"))
    print("\n")

    input("Press Enter to Go back to the main menu...")
