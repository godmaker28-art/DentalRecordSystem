from tabulate import tabulate
def create_appointment(dentist_schedule):
    dentist_sched = dentist_schedule
    print("-- Appointment Creation --");
    patient_name = input("Patient Name: ");
    print (f"\nAppointed Patient: {patient_name}\nChoose your Available Dentist:");

    custom_headers = {"index":"No.", "name":"Dentist's Name", "date":"Date Available", "time":"Time"}
    print(tabulate(dentist_sched, headers=custom_headers, tablefmt="grid"));

    dentist_no = int(input("Choice [1-3, 0 to return]: "));

    while True:
        match dentist_no:
                case 1:
                    return patient_name,0
                    break
                case 2:
                    return patient_name,1
                    break
                case 3:
                    return patient_name,2
                    break
                case 0:
                    return;
                case _:
                    print("Invalid Input!");
    return patient_name, dentist_no