from tabulate import tabulate

# Dentist schedule and appointment structure
dentist_appointments = [
    {"index": 1, "doctor": "Dr. Mancion", "date": "August 17, 2026", "available_times": ["9:00 AM", "1:00 PM"], "patient": None, "booked_time": None},
    {"index": 2, "doctor": "Dr. Mendoza", "date": "August 18, 2026", "available_times": ["10:00 AM", "2:00 PM"], "patient": None, "booked_time": None},
    {"index": 3, "doctor": "Dr. Escoto", "date": "August 19, 2026", "available_times": ["11:00 AM", "3:00 PM"], "patient": None, "booked_time": None}
]

# Functions
def create_appointment():
    print("\n-- Appointment Creation --")
    patient_name = input("Patient Name: ").strip()
    print(f"\nAppointed Patient: {patient_name}\nChoose your Available Dentist:")

    # Prepare data for tabulate view
    table_data = []
    for doc in dentist_appointments:
        table_data.append({
            "index": doc["index"], 
            "name": doc["doctor"], 
            "date": doc["date"], 
            "time": " / ".join(doc["available_times"])
        })

    custom_headers = {"index": "No.", "name": "Dentist's Name", "date": "Date Available", "time": "Time Slots"}
    print(tabulate(table_data, headers=custom_headers, tablefmt="grid"))

    try:
        dentist_no = int(input("Choice [1-3, 0 to return]: "))
        if dentist_no == 0:
            return
        
        if 1 <= dentist_no <= len(dentist_appointments):
            doc = dentist_appointments[dentist_no - 1]
            
            # Check if doctor already has an appointment
            if doc["patient"] is not None:
                print(f"[NOTE] {doc['doctor']} already has an appointment booked with {doc['patient']}.")
                return
            
            print(f"\nAvailable times for {doc['doctor']}:")
            for i, time in enumerate(doc["available_times"], 1):
                print(f"[{i}] {time}")
                
            time_choice = int(input("Choose time slot [1 or 2]: ")) - 1
            if 0 <= time_choice < len(doc["available_times"]):
                selected_time = doc["available_times"][time_choice]
                doc["patient"] = patient_name
                doc["booked_time"] = selected_time
                print(f"Appointment booked successfully for {patient_name} with {doc['doctor']} at {selected_time}!")
            else:
                print("Invalid time slot choice.")
        else:
            print("Invalid dentist choice.")
    except ValueError:
        print("Please enter a valid number.")

def update_records():
    print("\n--- Current Booked Appointments ---")
    booked_docs = [doc for doc in dentist_appointments if doc["patient"] is not None]
    
    if not booked_docs:
        print("No active appointments to update.")
        return
        
    table_data = []
    for doc in dentist_appointments:
        if doc["patient"] is not None:
            table_data.append({
                "index": doc["index"],
                "name": doc["doctor"],
                "date": doc["date"],
                "patient": doc["patient"],
                "booked_time": doc["booked_time"]
            })
            
    custom_headers = {
        "index": "No.", 
        "name": "Dentist's Name", 
        "date": "Date", 
        "patient": "Patient Name", 
        "booked_time": "Booked Time"
    }
    print(tabulate(table_data, headers=custom_headers, tablefmt="grid"))
            
    try:
        doc_choice = int(input("Select doctor record index to update [1-3, 0 to return]: "))
        if doc_choice == 0:
            return
            
        doc = next((d for d in dentist_appointments if d["index"] == doc_choice), None)
        
        if doc and doc["patient"] is not None:
            print(f"Updating appointment for {doc['doctor']} (Current Patient: {doc['patient']})")
            new_name = input("Enter new patient name (or press Enter to keep current): ").strip()
            if new_name:
                doc["patient"] = new_name
            
            print(f"\nAvailable times for {doc['doctor']}:")
            for i, time in enumerate(doc["available_times"], 1):
                print(f"[{i}] {time}")
            
            time_choice = int(input("Choose new time slot [1 or 2]: ")) - 1
            if 0 <= time_choice < len(doc["available_times"]):
                doc["booked_time"] = doc["available_times"][time_choice]
                print("Appointment updated successfully!")
            else:
                print("Invalid time slot.")
        else:
            print("Invalid choice or no active appointment for this doctor.")
    except ValueError:
        print("Please enter a valid number.")

# Main system loop
print("-- Dental Record System --\n")

while True:
    print("\nChoices:")
    print("1. Create an appointment")
    print("2. Update Appointment")
    print("0. Exit")
    
    try:
        choice = int(input("Choose an action [1-2, 0 to exit]: "))
        
        if choice == 1:
            create_appointment()
        elif choice == 2:
            update_records()
        elif choice == 0:
            print("Exiting the system...")
            break
        else:
            print("Invalid Input!")
    except ValueError:
        print("Please enter a valid number.")