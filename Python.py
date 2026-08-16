# Dentist Appointment System with CRUD functionality

dr = ["[1] Mendoza", "[2] Mancion", "[3] Escoto"]

# Storing appointments in a structured list
dentist_appointments = [
    {"doctor": "Dr. Mendoza", "available_times": ["9:00 AM", "1:00 PM"], "patient": None, "booked_time": None},
    {"doctor": "Dr. Mancion", "available_times": ["10:00 AM", "2:00 PM"], "patient": None, "booked_time": None},
    {"doctor": "Dr. Escoto", "available_times": ["11:00 AM", "3:00 PM"], "patient": None, "booked_time": None}
]

def show_menu():
    print("\n--- Dentist Appointment Logs (CRUD System) ---")
    print("[1] Create (Book Appointment)")
    print("[2] Read (View Appointments)")
    print("[3] Update (Reschedule Appointment)")
    print("[4] Delete (Cancel Appointment)")
    print("[5] Exit")

while True:
    show_menu()
    action = input("Choose an action [1-5]: ").strip()

    # CREATE: Book an appointment
    if action == '1':
        patient_name = input("Enter patient name: ").strip()
        print(f"\nWelcome, {patient_name}! Let's schedule an appointment.")
        print("Available dentists: " + ", ".join(dr))
        
        try:
            choice2 = int(input("Choose Dentist to book [1, 2, 3]: ")) - 1
            if 0 <= choice2 < len(dentist_appointments):
                doc = dentist_appointments[choice2]
                
                # Check if doctor already has a patient
                if doc["patient"] is not None:
                    print(f"[NOTE] {doc['doctor']} already has an appointment booked with {doc['patient']}. Please choose another doctor or update the existing one.")
                    continue
                
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

    # READ: View all appointment logs
    elif action == '2':
        print("\n--- Current Appointment Logs ---")
        for i, doc in enumerate(dentist_appointments, 1):
            status = f"Booked by {doc['patient']} at {doc['booked_time']}" if doc["patient"] else "Available"
            print(f"[{i}] {doc['doctor']} -> Status: {status}")

    # UPDATE: Reschedule or change patient details
    elif action == '3':
        print("\n--- Current Booked Appointments ---")
        booked_docs = [doc for doc in dentist_appointments if doc["patient"] is not None]
        
        if not booked_docs:
            print("No active appointments to update.")
            continue
            
        for i, doc in enumerate(dentist_appointments, 1):
            if doc["patient"]:
                print(f"[{i}] {doc['doctor']} - Patient: {doc['patient']} ({doc['booked_time']})")
                
        try:
            doc_choice = int(input("Select doctor record to update [1-3]: ")) - 1
            if 0 <= doc_choice < len(dentist_appointments):
                doc = dentist_appointments[doc_choice]
                if doc["patient"] is None:
                    print("This doctor has no active appointment to update.")
                    continue
                
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
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

    # DELETE: Cancel an appointment
    elif action == '4':
        print("\n--- Cancel an Appointment ---")
        for i, doc in enumerate(dentist_appointments, 1):
            if doc["patient"]:
                print(f"[{i}] {doc['doctor']} - Patient: {doc['patient']} ({doc['booked_time']})")
        
        try:
            doc_choice = int(input("Select doctor record to cancel appointment [1-3]: ")) - 1
            if 0 <= doc_choice < len(dentist_appointments):
                doc = dentist_appointments[doc_choice]
                if doc["patient"] is None:
                    print("No appointment exists for this doctor.")
                else:
                    print(f"Canceling appointment for {doc['patient']} with {doc['doctor']}...")
                    doc["patient"] = None
                    doc["booked_time"] = None
                    print("Appointment cancelled successfully!")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

    # EXIT
    elif action == '5':
        print("\nExiting system. Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 5.")