from tabulate import tabulate  # pip install tabulate

# Dentist schedule and slot structure
dentist_schedule = [
    {
        "index": 1, 
        "doctor": "Dr. Mendoza", 
        "date": "August 17, 2026", 
        "slots": [
            {"time": "9:00 AM", "patient": None},
            {"time": "1:00 PM", "patient": None}
        ]
    },
    {
        "index": 2, 
        "doctor": "Dr. Mancion", 
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


def create_appointment():
    print("\n-- Appointment Creation --")
    patient_name = input("Patient Name: ").strip()
    
    if not patient_name:
        print("[ERROR] Patient name cannot be empty.\n")
        return

    print(f"\nAppointed Patient: {patient_name}\nChoose your Available Dentist:")

    table_data = []
    for doc in dentist_schedule:
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

    while True:
        try:
            dentist_no = int(input("Choice [1-3, 0 to return]: "))
            if dentist_no == 0:
                return
            
            if 1 <= dentist_no <= len(dentist_schedule):
                doc = dentist_schedule[dentist_no - 1]
                unbooked_slots = [slot for slot in doc["slots"] if slot["patient"] is None]
                
                if not unbooked_slots:
                    print(f"[NOTE] {doc['doctor']} has no available time slots left.\n")
                    return
                
                print(f"\nAvailable times for {doc['doctor']}:")
                for i, slot in enumerate(unbooked_slots, 1):
                    print(f"[{i}] {slot['time']}")
                    
                time_choice = int(input("Choose time slot number: ")) - 1
                if 0 <= time_choice < len(unbooked_slots):
                    selected_slot = unbooked_slots[time_choice]
                    selected_slot["patient"] = patient_name
                    print(f"\nAppointment successfully booked for {patient_name} with {doc['doctor']} at {selected_slot['time']}!\n")
                    break
                else:
                    print("Invalid time slot choice.")
            else:
                print("Invalid dentist choice. Please choose between 1-3 or 0 to return.")
        except ValueError:
            print("Invalid Input! Please enter a valid number.")


def view_records():
    print("\n-- Dental Clinic Records --")
    
    # Flatten active appointments from dentist schedules
    active_records = []
    for doc in dentist_schedule:
        for slot in doc["slots"]:
            if slot["patient"] is not None:
                active_records.append({
                    "patient": slot["patient"],
                    "dentist": doc["doctor"],
                    "date": doc["date"],
                    "time": slot["time"]
                })
    
    if not active_records:
        print("Empty Set - No active patient appointments yet.\n")
        input("Press Enter to go back to the main menu...")
        return
        
    custom_headers = {
        "patient": "Patient's Name",
        "dentist": "Dentist's Name",
        "date": "Date",
        "time": "Time"
    }

    print(tabulate(active_records, headers=custom_headers, tablefmt="grid"))
    print("\n")
    input("Press Enter to go back to the main menu...")


def update_appointment():
    print("\n-- Update Appointment --")
    
    # Gather all booked slots with an incremental index for easy selection
    booked_slots_list = []
    for doc in dentist_schedule:
        for slot in doc["slots"]:
            if slot["patient"] is not None:
                booked_slots_list.append({
                    "doctor_obj": doc,
                    "slot_obj": slot,
                    "patient": slot["patient"],
                    "doctor": doc["doctor"],
                    "date": doc["date"],
                    "time": slot["time"]
                })
                
    if not booked_slots_list:
        print("No active appointments found to update.\n")
        return
        
    table_data = []
    for idx, item in enumerate(booked_slots_list, 1):
        table_data.append({
            "record_no": idx,
            "patient": item["patient"],
            "doctor": item["doctor"],
            "date": item["date"],
            "time": item["time"]
        })
        
    custom_headers = {
        "record_no": "No.",
        "patient": "Patient Name",
        "doctor": "Dentist's Name",
        "date": "Date",
        "time": "Time"
    }
    
    print(tabulate(table_data, headers=custom_headers, tablefmt="grid"))
    
    try:
        choice = int(input("Enter the Record No. to update/rebook (0 to return): "))
        if choice == 0:
            return
            
        if 1 <= choice <= len(booked_slots_list):
            selected_record = booked_slots_list[choice - 1]
            old_doc = selected_record["doctor_obj"]
            old_slot = selected_record["slot_obj"]
            patient_name = old_slot["patient"]
            
            print(f"\nUpdating appointment for: {patient_name} (Currently with {old_doc['doctor']} at {old_slot['time']})")
            print("Choose a new dentist/slot:")
            
            # Show available options just like creation
            table_data = []
            for doc in dentist_schedule:
                available_slots = [slot["time"] for slot in doc["slots"] if slot["patient"] is None]
                # If it's the current doctor, their current slot is also available to keep
                time_str = " / ".join(available_slots) if available_slots else "Fully Booked"
                
                table_data.append({
                    "index": doc["index"], 
                    "name": doc["doctor"], 
                    "date": doc["date"], 
                    "time": time_str
                })

            print(tabulate(table_data, headers={"index": "No.", "name": "Dentist's Name", "date": "Date Available", "time": "Available Time Slots"}, tablefmt="grid"))
            
            dentist_no = int(input("Choose new dentist [1-3, 0 to cancel]: "))
            if dentist_no == 0:
                return
                
            if 1 <= dentist_no <= len(dentist_schedule):
                new_doc = dentist_schedule[dentist_no - 1]
                unbooked_slots = [slot for slot in new_doc["slots"] if slot["patient"] is None or slot == old_slot]
                
                if not unbooked_slots:
                    print("[NOTE] Selected doctor has no available time slots left.\n")
                    return
                    
                print(f"\nAvailable times for {new_doc['doctor']}:")
                for i, slot in enumerate(unbooked_slots, 1):
                    current_tag = " (Current)" if slot == old_slot else ""
                    print(f"[{i}] {slot['time']}{current_tag}")
                    
                time_choice = int(input("Choose time slot number: ")) - 1
                if 0 <= time_choice < len(unbooked_slots):
                    new_slot = unbooked_slots[time_choice]
                    
                    # Free up old slot and assign new slot
                    old_slot["patient"] = None
                    new_slot["patient"] = patient_name
                    print(f"\nAppointment successfully updated for {patient_name} with {new_doc['doctor']} at {new_slot['time']}!\n")
                else:
                    print("Invalid time slot choice.")
            else:
                print("Invalid dentist choice.")
        else:
            print("Invalid record number selection.")
    except ValueError:
        print("Invalid Input! Please enter a valid number.")


# Main loop starts here!
if __name__ == "__main__":
    while True:
        print("\n-- Dental Record System --\n")
        print("Choices:\n1. Create an appointment\n2. View Records\n3. Update Appointment\n0. Exit")
        
        try:
            choice = int(input("Choose an action [1-3, 0 to exit]: "))
            
            match choice:
                case 1:
                    create_appointment()
                case 2:
                    view_records()
                case 3:
                    update_appointment()
                case 0:
                    print("Exiting the system...")
                    break
                case _:
                    print("Invalid Input! Please choose a valid option.\n")
        except ValueError:
            print("Invalid Input! Please enter a number.\n")