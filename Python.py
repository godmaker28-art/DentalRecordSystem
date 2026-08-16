from tabulate import tabulate

# Dentist schedule and appointment structure updated to support multiple bookings per doctor
dentist_appointments = [
    {
        "index": 1, 
        "doctor": "Dr. Mancion", 
        "date": "August 17, 2026", 
        "slots": [
            {"time": "9:00 AM", "patient": None},
            {"time": "1:00 PM", "patient": None}
        ]
    },
    {
        "index": 2, 
        "doctor": "Dr. Mendoza", 
        "date": "August 18, 2026", 
        "slots": [
            {"time": "10:00 AM", "patient": None},
            {"time": "2:00 PM", "patient": None}
        ]
    },
    {
        "index": 3, 
        "doctor": "Dr. Escoto", 
        "date": "August 19, 2026", 
        "slots": [
            {"time": "11:00 AM", "patient": None},
            {"time": "3:00 PM", "patient": None}
        ]
    }
]

# Functions
def create_appointment():
    print("\n-- Appointment Creation --")
    patient_name = input("Patient Name: ").strip()
    if not patient_name:
        print("[ERROR] Patient name cannot be empty.")
        return

    print(f"\nAppointed Patient: {patient_name}\nChoose your Available Dentist:")

    # Prepare data for tabulate view
    table_data = []
    for doc in dentist_appointments:
        # Show only available time slots
        available_slots = [slot["time"] for slot in doc["slots"] if slot["patient"] is None]
        time_str = " / ".join(available_slots) if available_slots else "Fully Booked"
        
        table_data.append({
            "index": doc["index"], 
            "name": doc["doctor"], 
            "date": doc["date"], 
            "time": time_str
        })

    custom_headers = {"index": "No.", "name": "Dentist's Name", "date": "Date Available", "time": "Available Time Slots"}
    print(tabulate(table_data, headers=custom_headers, tablefmt="grid"))

    try:
        dentist_no = int(input("Choice [1-3, 0 to return]: "))
        if dentist_no == 0:
            return
        
        if 1 <= dentist_no <= len(dentist_appointments):
            doc = dentist_appointments[dentist_no - 1]
            
            # Filter available slots for this doctor
            unbooked_slots = [slot for slot in doc["slots"] if slot["patient"] is None]
            
            if not unbooked_slots:
                print(f"[NOTE] {doc['doctor']} has no available time slots left.")
                return
            
            print(f"\nAvailable times for {doc['doctor']}:")
            for i, slot in enumerate(unbooked_slots, 1):
                print(f"[{i}] {slot['time']}")
                
            time_choice = int(input("Choose time slot number: ")) - 1
            if 0 <= time_choice < len(unbooked_slots):
                selected_slot = unbooked_slots[time_choice]
                selected_slot["patient"] = patient_name
                print(f"Appointment booked successfully for {patient_name} with {doc['doctor']} at {selected_slot['time']}!")
            else:
                print("Invalid time slot choice.")
        else:
            print("Invalid dentist choice.")
    except ValueError:
        print("Please enter a valid number.")

def update_records():
    print("\n--- Current Booked Appointments ---")
    
    table_data = []
    for doc in dentist_appointments:
        for slot in doc["slots"]:
            if slot["patient"] is not None:
                table_data.append({
                    "doctor": doc["doctor"],
                    "date": doc["date"],
                    "time": slot["time"],
                    "patient": slot["patient"]
                })
         
    if not table_data:
        print("No active appointments to update.")
        return
        
    custom_headers = {
        "doctor": "Dentist's Name", 
        "date": "Date", 
        "time": "Booked Time",
        "patient": "Patient Name"
    }
    print(tabulate(table_data, headers=custom_headers, tablefmt="grid"))
    print("\nTo rebook or change an appointment, please cancel/create a new one or use the creation menu.")

# Main system loop
print("-- Dental Record System --\n")

while True:
    print("\nChoices:")
    print("1. Create an appointment")
    print("2. View/Update Appointments")
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