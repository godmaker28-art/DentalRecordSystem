from tabulate import tabulate
from view_appointments import view_records
from create import create_appointment
def update_records(appointment_list, dentist_schedule):
    
    print("\n -- Dental Clinic Records --")
    filtered_records = [app for app in appointment_list if app]
    dentist_sched = dentist_schedule
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
    while True:
        try:
            update_choice = int(input(f"Choose appointment to update [1-{len(filtered_records)}, 0 to return]: "))

            if update_choice == 0:
                    return
            elif 1 <= update_choice <= len(appointment_list):
                    print("\n --- Enter Details for Rescheduling ---")
                    result = create_appointment(dentist_sched)

                    if result is not None:
                        new_patient_name, new_dentist_index = result

                        dentist_name = dentist_schedule[new_dentist_index]["name"]
                        dentist_date = dentist_schedule[new_dentist_index]["date"]
                        dentist_time = dentist_schedule[new_dentist_index]["time"]

                        updated_app = {
                                "patient": new_patient_name,
                                "dentist": dentist_name,
                                "date": dentist_date,
                                "time": dentist_time
                            }
                        appointment_list[update_choice - 1] = updated_app
                        print("Success - Appointment Successfully Updated!")
                        break
            
            else:
                print("Out Of Range! Please try again.")

        except ValueError:
            print("Invalid Input!")

